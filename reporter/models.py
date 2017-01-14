from django.db import models
from core.models import CoreBaseUser, TokenModel


_app_label = 'reporter'


class Reporter(CoreBaseUser):

    class Meta:
        db_table = 'reporters_reporter'
        app_label = _app_label


class ReporterToken(TokenModel):
    user = models.ForeignKey(Reporter, related_name='reporter')
    class Meta:
        db_table = 'reporters_token'
        app_label = _app_label