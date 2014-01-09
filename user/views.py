import functools
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import views as auth_views
from django.forms.widgets import TextInput, PasswordInput
from django.contrib.auth.decorators import login_required
from django import forms
from django.shortcuts import render_to_response
from django.template import RequestContext


@login_required(login_url='/user/login/')
def user_profile(request):
    """
    Show the user's profile page.
    """
    
    return render_to_response('profile.html', context_instance=RequestContext(request))


# Login/logout
class AuthenticationForm(auth_forms.AuthenticationForm):
    username = forms.CharField(max_length=254,
            widget=TextInput(attrs={
                'placeholder': 'Username',
                'class': 'form-control',
                'required': '',
                }))
    password = forms.CharField(label='Password',
            widget=PasswordInput(attrs={
                'placeholder': 'Password',
                'class': 'form-control',
                'required': '',
                }))

login = functools.partial(auth_views.login,
        template_name='login_form.html',
        authentication_form=AuthenticationForm)
logout = auth_views.logout
