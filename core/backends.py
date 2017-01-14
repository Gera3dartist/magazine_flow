__author__ = 'agerasym'


class CoreAuthBackend(object):
    model = None

    def authenticate(self, email=None, password=None, **kwargs):
        try:
            user = self.model.objects.get(email__iexact=email)
        except self.model.DoesNotExist:
            return None
        else:
            return user

    def get_user(self, user_id):
        try:
            return self.model._default_manager.get(pk=user_id)
        except self.model.DoesNotExist:
            return None
