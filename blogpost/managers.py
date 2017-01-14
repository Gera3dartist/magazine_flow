from django.db.models import QuerySet, Manager, Q

__author__ = 'agerasym'


class BlogPostQuerySet(QuerySet):
    pass


class BlogPostManager(
        Manager.from_queryset(BlogPostQuerySet)):

    def search(self, param: str):
        return self.get_queryset().filter(
            Q(title__contains=param) | Q(body__contains=param))