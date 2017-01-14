from reporter.authentication import ReporterAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from reporter.serializers import ReporterSerializer
from rest_framework.permissions import IsAuthenticated

__author__ = 'agerasym'


class GetInfoReporter(APIView):
    authentication_classes = (ReporterAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = ReporterSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.request.user)
        return Response({'status': 200, 'data': serializer.data})