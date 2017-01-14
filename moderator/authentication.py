from core.authentication import TokenCoreAuthentication
from .models import ModeratorToken

__author__ = 'agerasym'


class ModeratorAuthentication(TokenCoreAuthentication):
    model = ModeratorToken
