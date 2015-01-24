from django_fsm import has_transition_perm
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, detail_route, list_route
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.views import APIView

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


class AuthMixin:
    authentication_classes = (TokenAuthentication,
                              SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated,)


class UserViewSet(AuthMixin,
                  viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @list_route(methods=['get'])
    def current(self, request):
        return Response(UserSerializer(request.user, context={'request': request}).data)


class ProjectViewSet(AuthMixin,
                     viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class PersonRequestViewSet(AuthMixin,
                           get_viewset_transition_actions_mixin(PersonRequest),
                           viewsets.ModelViewSet):
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


class DeleteAuthToken(APIView):
    renderer_classes = (JSONRenderer,)

    def get(self, request, format=None):
        return Response({'response': 'success'})

delete_auth_token = DeleteAuthToken.as_view()