from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    manager = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True, source="employee.manager")
    subordinates = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True, many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'manager', 'subordinates')