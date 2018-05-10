"""
@author: Aman Kumar

"""


from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class UserListingSerializer(serializers.ModelSerializer):
    """ User listing data  serializer for the user """

    class Meta:
        model = User
        fields = ('id', 'first_name', 'username', 'is_superuser', 'is_staff', 'is_active',)


class UserDeleteSerializer(serializers.Serializer):
    """ user delete multiple users """
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)


class UserActivateSerializer(serializers.Serializer):
    """ user activate serializer """
    users = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        many=True
    )


class UserDeActivateSerializer(serializers.Serializer):
    """ user activate serializer """
    users = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        many=True
    )