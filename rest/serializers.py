import hashlib

from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from django.contrib.auth.models import User

from rest.models import Project, PersonRequest

h = hashlib.new('md5')
h.update("PREFIX".encode("utf-8"))
BOGUS_PASSWORD = h.hexdigest()


class PasswordField(serializers.CharField):
    def to_representation(self, obj):
        return BOGUS_PASSWORD

    def to_internal_value(self, data):
        if data != BOGUS_PASSWORD:
            return make_password(data)
        else:
            instance = self.parent.instance
            return instance.password


class UserSerializer(serializers.HyperlinkedModelSerializer):
    manager = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=False, source='profile.manager',
                                                  queryset=User.objects.all(), allow_null=True)
    subordinates = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True, many=True)
    password = PasswordField()

    # requester_requests = serializers.HyperlinkedRelatedField(view_name='request-detail', read_only=True, many=True)
    # requestee_requests = serializers.HyperlinkedRelatedField(view_name='request-detail', read_only=True, many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password',
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