from blogpost.models import BlogPost
from reporter.backend import ReporterAuthBackend
from reporter.models import Reporter
from rest_framework import serializers
import logging

__author__ = 'agerasym'

logger = logging.getLogger(__name__)


class AuthenticateReporterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = ReporterAuthBackend().authenticate(**attrs)
        if user and user.check_password(attrs['password']):
            attrs['user'] = user
            return attrs
        logger.debug('Authentication Failed %s (%s)'
                     % (attrs.get('email', 'No email'),
                        ", ".join(map(lambda x: str(x), attrs.items()))))
        raise serializers.ValidationError('Authentication error')


class ReporterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reporter
        exclude = ('password', )


class BlogPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
