import datetime
from django.utils.timezone import utc
from django.shortcuts import render
from tasks.models import Task

def home_feed(request):
    """
    Show the user's home feed.
    """
    return render(request, 'home.html')

def list_all_tasks(request):
    """
    List all the active tasks, adding a few features
    """
    tasks = Task.objects.filter(start_date__gt=datetime.date.today())
    # the sooner, the better
    tasks = tasks.order_by('-start_date')
    return render(request, 'all_tasks.html', { 'tasks': tasks })
