from rest_framework import mixins
from rest_framework.pagination import PaginationSerializer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

__author__ = 'agerasym'


class StandardResultsSetPagination(PaginationSerializer):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ModelViewGetter(mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):

    instance_code = "0"
    list_code = "0"

    def dispatch(self, request, *args, **kwargs):
        if self.suffix == 'Instance':
            self.method_code = self.instance_code
        if self.suffix == 'List':
            self.method_code = self.list_code
        return super().dispatch(
            request, *args, **kwargs)

    def list_or(self, request, qs, *args, **kwargs):
        instance = self.filter_queryset(qs)
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_pagination_serializer(page)
        else:
            serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)