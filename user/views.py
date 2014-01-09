import functools
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import views as auth_views
from django.forms.widgets import TextInput, PasswordInput
from django.contrib.auth.decorators import login_required
from django import forms
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import DetailView

from user.models import UserInformation

@login_required(login_url='/user/login/')
def user_profile(request):
    """
    Show the user's profile page.
    """
    user_info = UserInformation.objects.get(user_id=request.user.id)
    context = RequestContext(request, {
        'user_info': user_info
        });
    return render_to_response('profile.html', context_instance=context)

#@login_required(login_url='/user/login/')
# class UserProfileView(DetailView):
#     model = UserInformation
#     template_name = 'profile.html'
#     pk_url_kwarg = 'task_id'
#     context_object_name = 'user_info'
# user_profile = UserProfileView.as_view()


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
