from reporter.models import ReporterToken
from reporter.serializers import AuthenticateReporterSerializer
from rest_framework import exceptions
from rest_framework.permissions import AllowAny
__author__ = 'agerasym'


import datetime
import logging

import pytz
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from reporter.authentication import ReporterAuthentication

logger = logging.getLogger(__name__)


class AuthenticateReporterView(APIView):
    authentication_classes = (AllowAny, )
    permission_classes = ()
    serializer_class = AuthenticateReporterSerializer
    model = ReporterToken

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        reporter = serializer.validated_data['user']

        token, _ = self.model.objects.get_or_create(
            user=reporter)
        token.created = datetime.datetime.now(pytz.utc)
        token.save(update_fields=['created'])

        return Response({"status": 200, "data": {"token": token.key}})


class AuthLogoutReporterView(APIView):
    authentication_classes = (ReporterAuthentication, )
    permission_classes = (IsAuthenticated, )
    model = ReporterToken


    def post(self, request, *args, **kwargs):
        try:
            token = self.model.objects.get(user=request.user)
            token.delete()
        except self.model.DoesNotExist:
            raise exceptions.NotAcceptable()
        else:
            return Response({'status': 200})
