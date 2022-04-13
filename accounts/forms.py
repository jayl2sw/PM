from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


class CustomUser(UserCreationForm):
    pass

class CustomUserChangeForm(UserChangeForm):

    password = None
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')