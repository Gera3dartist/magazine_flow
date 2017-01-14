from django.contrib.auth.models import Permission
from django.db import models
from core.models import CoreBaseUser, TokenModel


_app_label = 'moderator'


class Moderator(CoreBaseUser):

    class Meta:
        db_table = 'moderators_moderator'
        app_label = _app_label


class ModeratorToken(TokenModel):
    user = models.ForeignKey(Moderator, related_name='reporter')
    class Meta:
        db_table = 'moderators_token'
        app_label = _app_label