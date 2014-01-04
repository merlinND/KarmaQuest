from django.shortcuts import render_to_response

def user_profile(request):
    """
    Show the user's profile page.
    """
    return render_to_response('profile.html')
