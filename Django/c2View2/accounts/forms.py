from django import forms
from django.contrib.auth import get_user_model, authenticate

# user MODEL GERAL USADO como no models.py #
User = get_user_model()
# formulario de login#


class LoginForm (forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        # id e senha conferem!!!#
        if username and password:
            user = authenticate(username=username, password=password)
        # id e senha nao conferem#
        if not user:
            raise forms.ValidationError('usuário incorreto')
        # senha nao confere#
        if not user.check_password(password):
            raise forms.ValidationError('senha incorreta')
        # usuario desativado#
        if not user.is_active:
            raise forms.ValidationError('usuário não ativo')
        return super(LoginForm, self).clean(*args, **kwargs)


class RegisterForm (forms.ModelForm):
    email = forms.EmailField(label='email')
    email2 = forms.EmailField(label='confirm email')
    password = forms.CharField(widget=forms.PasswordInput)
    # os de cima são os campos modificados, mas nao necessitava ###

    class Meta:
        model = User
        fields = ['username', 'email', 'email2', 'password']

    # checando o confirm email #
    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError('e-mail nao confere')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('e-mail em uso')
        return super(RegisterForm, self).clean(*args, **kwargs)
