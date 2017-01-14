from core.backends import  CoreAuthBackend
from moderator.models import Moderator

__author__ = 'agerasym'



class ModeratorAuthBackend(CoreAuthBackend):
    model = Moderator

