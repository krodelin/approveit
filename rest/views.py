from django_fsm import has_transition_perm

from rest_framework.decorators import api_view, detail_route
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404

from rest_framework.reverse import reverse

from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User

from rest.models import Project, PersonRequest
from rest.serializers import UserSerializer, ProjectSerializer, PersonRequestSerializer
from rest.viewset_actions_mixin import get_viewset_transition_actions_mixin


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'projects': reverse('project-list', request=request, format=format),
        'requests': reverse('request-list', request=request, format=format),
    })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class PersonRequestViewSet(get_viewset_transition_actions_mixin(PersonRequest), viewsets.ModelViewSet):
    queryset = PersonRequest.objects.all()
    serializer_class = PersonRequestSerializer

    @detail_route(methods=['post'])
    def approve(self, request, pk):
        person_request = get_object_or_404(PersonRequest, pk=pk)
        self.get_object()
        if not has_transition_perm(person_request.approve, request.user):
            raise PermissionDenied
        person_request.approve()
        person_request.save()
        return Response(PersonRequestSerializer(person_request, context={'request': request}).data)





