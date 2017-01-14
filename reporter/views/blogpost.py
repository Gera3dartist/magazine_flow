import logging
from core.exceptions import ValidationException
from rest_framework import generics
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.pagination import PaginationSerializer
from reporter.authentication import ReporterAuthentication
from blogpost.models import BlogPost
from blogpost.serializers import BlogPostReporterCreateSerializer, BlogPostListPublicSerializer
from core.pagination import ModelViewGetter
from blogpost.serializers import BlogPostListSerializer


__author__ = 'agerasym'

logger = logging.getLogger(__name__)


class BlogPostListView(ModelViewGetter):

    authentication_classes = (ReporterAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = BlogPostListSerializer
    pagination_serializer_class = PaginationSerializer
    paginate_by = 25


    def get_queryset(self):
        user = self.request.user
        return user.articles.all()

    def list(self, request, *args, **kwargs):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        return self.list_or(request, queryset, *args, **kwargs)

    @list_route(methods=['post'],
                serializer_class=BlogPostReporterCreateSerializer,
                url_path=r'create',
                **{})
    def create_blogpost(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response({'status': 200, 'data': {'id': serializer.instance.id}})


class BlogPostListPublicView(ModelViewGetter):
    authentication_classes = (ReporterAuthentication, )
    permission_classes = (AllowAny, )
    serializer_class = BlogPostListPublicSerializer
    pagination_serializer_class = PaginationSerializer
    paginate_by = 25
    queryset = BlogPost.objects.filter(is_confirmed=True)

    @list_route(methods=['get'],
            serializer_class=BlogPostListPublicSerializer,
            url_path=r'search',
            **{})
    def search(self, request, *args, **kwargs):
        search_param = request.GET.get('search_param', None)
        if not search_param:
            raise ValidationException('bad search param')
        queryset = BlogPost.objects.search(search_param)

        return self.list_or(request, queryset, *args, **kwargs)

