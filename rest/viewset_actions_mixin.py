from django_fsm import has_transition_perm
from rest_framework.decorators import detail_route
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response


def can_transition(user, transition_method, object):
    return has_transition_perm(transition_method, user) and object.can_transition(user, transition_method)


def get_transition_viewset_method(model, transition_name):
    @detail_route(methods=['post'])
    def inner_func(self, request, pk=None):
        object = self.get_object()
        transition_method = getattr(object, transition_name)
        if not can_transition(request.user, transition_method, object):
            raise PermissionDenied
        transition_method()

        if self.save_after_transition:
            object.save()

        serializer = self.get_serializer(object)
        return Response(serializer.data)

    return inner_func


def get_viewset_transition_actions_mixin(model):
    instance = model()

    class Mixin(object):
        save_after_transition = True

    transitions = instance.get_all_status_transitions()
    transition_names = set(x.name for x in transitions)
    for transition_name in transition_names:
        setattr(
            Mixin,
            transition_name,
            get_transition_viewset_method(model, transition_name)
        )

    return Mixin

