from rest_framework import serializers

from users.models import User

from axes.handlers.proxy import AxesProxyHandler

class UserSerializer(serializers.ModelSerializer):

    is_blocked = serializers.SerializerMethodField()

    def get_is_blocked(self, obj):
        request = self.context['request']
        return AxesProxyHandler.is_locked(request, {'username': obj})
    
    class Meta:

        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'last_login',
            'is_staff',
            'is_active',
            'required_password_change',
            'password_change_date',
            'is_blocked'
        ]