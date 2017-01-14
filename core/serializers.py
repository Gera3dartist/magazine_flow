import logging
from rest_framework import serializers

__author__ = 'agerasym'
logger = logging.getLogger(__name__)

class CoreModelItemSerialize(object):
    """
    Core validate info from the all serializers
    """

    def validate_value(self, value, model, raise_=None):
        try:
            return model.objects.only('id').get(id=value)
        except model.DoesNotExist:
            raise serializers.ValidationError('Non valid value')
