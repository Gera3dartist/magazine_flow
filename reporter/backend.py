from core.backends import  CoreAuthBackend
from reporter.models import Reporter

__author__ = 'agerasym'



class ReporterAuthBackend(CoreAuthBackend):
    model = Reporter

