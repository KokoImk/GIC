from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model


class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, email=None, password=None, **kwargs):
        UserModel = get_user_model()

        if username:
            try:
                user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                return None
        elif email:
            try:
                user = UserModel.objects.get(email=email)
            except UserModel.DoesNotExist:
                return None
        else:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
