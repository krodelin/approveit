from rest_framework.decorators import api_view

from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User

from rest.models import Project
from rest.serializers import UserSerializer, ProjectSerializer


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'projects': reverse('project-list', request=request, format=format)
    })


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer





