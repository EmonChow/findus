from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q



class AuthenticationModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

     

        try:
            user = UserModel.objects.get(
                Q(username__exact=username) | Q(email__exact=username),
                role__name="ADMIN",
            )
            if user and user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None

        return None
