import logging
import datetime
from blogpost.models import BlogPost
from blogpost.serializers import BlogPostModeratorConfirmSerializer
from core.exceptions import NotFoundException
from moderator.models import ModeratorToken
from moderator.authentication import ModeratorAuthentication
from moderator.serializers import AuthenticateModeratorSerializer
import pytz
from rest_framework import exceptions
from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

logger = logging.getLogger(__name__)

__author__ = 'agerasym'




# from rest_framework import generics
# from rest_framework.decorators import list_route
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.response import Response
from rest_framework.pagination import PaginationSerializer
# from reporter.authentication import ReporterAuthentication
# from blogpost.models import BlogPost
from blogpost.serializers import BlogPostListSerializer, BlogPostModeratorConfirmSerializer
from core.pagination import ModelViewGetter



class BlogPostModeratorListView(ModelViewGetter):

    model = BlogPost
    authentication_classes = (ModeratorAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = BlogPostListSerializer
    pagination_serializer_class = PaginationSerializer
    paginate_by = 25

    def get_queryset(self):
        return self.model.objects.all()

    def list(self, request, *args, **kwargs):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        return self.list_or(request, queryset, *args, **kwargs)

    @detail_route(methods=['post'],
                serializer_class=BlogPostModeratorConfirmSerializer,
                url_path=r'confirm',
                **{})
    def create_blogpost(self, request, pk, *args, **kwargs):
        blogpost = self.model.objects.filter(id=pk).first()
        if not blogpost:
            raise NotFoundException('Not Found')
        serializer = self.serializer_class(instance=blogpost, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 200})


class BlogPostModeratorConfirm(APIView):
    authentication_classes = (ModeratorAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = BlogPostModeratorConfirmSerializer
    model = ModeratorToken

    def post(self, request, pk,  *args, **kwargs):
        blogpost = self.model.filter(id=pk).first()
        if not blogpost:
            raise NotFoundException('Not Found')
        serializer = self.serializer_class(instance=blogpost, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 200})


class AuthenticateModeratorView(APIView):
    authentication_classes = (AllowAny, )
    permission_classes = ()
    serializer_class = AuthenticateModeratorSerializer
    model = ModeratorToken

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        moderator = serializer.validated_data['user']

        token, _ = self.model.objects.get_or_create(
            user=moderator)
        token.created = datetime.datetime.now(pytz.utc)
        token.save(update_fields=['created'])

        return Response({"status": 200, "data": {"token": token.key}})


class AuthLogoutModeratorView(APIView):
    authentication_classes = (ModeratorAuthentication, )
    permission_classes = (IsAuthenticated, )
    model = ModeratorToken

    def post(self, request, *args, **kwargs):
        try:
            token = self.model.objects.get(user=request.user)
            token.delete()
        except self.model.DoesNotExist:
            raise exceptions.NotAcceptable()
        else:
            return Response({'status': 200})
