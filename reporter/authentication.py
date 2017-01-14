from core.authentication import TokenCoreAuthentication
from .models import ReporterToken

__author__ = 'agerasym'


class ReporterAuthentication(TokenCoreAuthentication):
    model = ReporterToken
