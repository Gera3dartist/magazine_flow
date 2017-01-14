from moderator.backend import ModeratorAuthBackend
from rest_framework import serializers
import logging

__author__ = 'agerasym'

logger = logging.getLogger(__name__)


class AuthenticateModeratorSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = ModeratorAuthBackend().authenticate(**attrs)
        if user and user.check_password(attrs['password']):
            attrs['user'] = user
            return attrs
        logger.debug('Authentication Failed %s (%s)'
                     % (attrs.get('email', 'No email'),
                        ", ".join(map(lambda x: str(x), attrs.items()))))
        raise serializers.ValidationError('Authentication error')