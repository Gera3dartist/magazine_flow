from blogpost.models import BlogPost
from rest_framework import serializers

__author__ = 'agerasym'

class BlogPostReporterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('body', 'title', )


class BlogPostModeratorConfirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('is_confirmed', )


class BlogPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost


class BlogPostListPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('id', 'body', 'title', 'author', 'created')
