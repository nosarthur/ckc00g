from rest_framework import serializers

from api.models import MyUser


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MyUser
        fields = ('url', 'email', 'first_name', 'last_name',
                  'gender', 'phone', 'employer',)



class PasswordSerializer:
    pass
