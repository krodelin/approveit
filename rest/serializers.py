from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User
from rest.models import Project, Request


class UserSerializer(serializers.HyperlinkedModelSerializer):
    manager = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True, source="employee.manager")
    subordinates = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True, many=True)

    requester_requests = serializers.HyperlinkedRelatedField(view_name='request-detail', read_only=True, many=True)
    requestee_requests = serializers.HyperlinkedRelatedField(view_name='request-detail', read_only=True, many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'manager', 'subordinates', 'requester_requests', 'requestee_requests')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    requests = serializers.HyperlinkedRelatedField(view_name='request-detail', read_only=True, many=True)

    class Meta:
        model = Project
        fields = ('url', 'title', 'notes', 'requests')


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Request
        fields = ('url', 'title', 'notes', 'project', 'requester', 'requestee')