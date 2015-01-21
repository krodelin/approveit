from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User
from django_fsm import FSMField
from rest.models import Project, PersonRequest


class UserSerializer(serializers.HyperlinkedModelSerializer):
    manager = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=False, source='profile.manager',
                                                  queryset=User.objects.all())
    subordinates = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True, many=True)

    # requester_requests = serializers.HyperlinkedRelatedField(view_name='request-detail', read_only=True, many=True)
    # requestee_requests = serializers.HyperlinkedRelatedField(view_name='request-detail', read_only=True, many=True)

    class Meta:
        model = User
        fields = ('url', 'username',
                  # 'requester_requests', 'requestee_requests',
                  'manager', 'subordinates',
        )

    def create(self, validated_data):
        manager_ = validated_data['profile']['manager']
        del validated_data['profile']
        instance = super(serializers.HyperlinkedModelSerializer, self).create(validated_data)
        instance.profile.manager = manager_
        instance.profile.save()
        return instance

    def update(self, instance, validated_data):
        manager_ = validated_data['profile']['manager']
        del validated_data['profile']
        instance = super(serializers.HyperlinkedModelSerializer, self).update(instance, validated_data)
        instance.profile.manager = manager_
        instance.profile.save()
        return instance


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    requests = serializers.HyperlinkedRelatedField(view_name='personrequest-detail', read_only=True, many=True)


    class Meta:
        model = Project
        fields = ('url', 'title', 'notes', 'requests')


class PersonRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonRequest
        fields = ('url', 'title', 'notes', 'project', 'requester', 'requestee', 'status')
        read_only_fields = ('status',)