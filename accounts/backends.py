from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

#overriding authentication method to use email instead of an username.
class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

    def get_user(self, user_id):
        try:
            User = get_user_model()
            return User.objects.get(id = user.id)
        except:
            return None