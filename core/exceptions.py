from rest_framework import exceptions

__author__ = 'agerasym'


class NotFoundException(exceptions.APIException):
    pass


class ValidationException(exceptions.APIException):
    pass
