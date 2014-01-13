import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView
from tasks.models import Task, Organization

def home_feed(request):
    """
    Show the user's home feed.
    """
    return render_to_response('home.html')

class TaskListView(ListView):
    http_method_names = ['get']
    template_name = 'all_tasks.html'
    context_object_name = 'tasks'
    paginate_by = 30

    def get_queryset(self):
        # List only tasks that start today or later
        tasks = Task.objects.filter(start_date__gt=datetime.date.today())
        return tasks.order_by('-start_date')

    def get_context_data(self, **kwargs):
        _super = super(TaskListView, self)
        context = _super.get_context_data(**kwargs)
        adjacent_pages = 2
        page_number = context['page_obj'].number
        num_pages = context['paginator'].num_pages
        startPage = max(page_number - adjacent_pages, 1)
        if startPage <= 3:
            startPage = 1
        endPage = page_number + adjacent_pages + 1
        if endPage >= num_pages - 1:
            endPage = num_pages + 1
        page_numbers = [n for n in range(startPage, endPage) \
                if n > 0 and n <= num_pages]
        context.update({
            'page_numbers': page_numbers,
            'show_first': 1 not in page_numbers,
            'show_last': num_pages not in page_numbers,
            })
        return context
list_all_tasks = TaskListView.as_view()

class TaskDetailView(DetailView):
    model = Task
    pk_url_kwarg = 'task_id'
    template_name = 'task_detail.html'
    context_object_name = 'task'
task_detail = TaskDetailView.as_view()

class OrgDetailView(DetailView):
    model = Organization
    pk_url_kwarg = 'org_id'
    template_name = 'org_detail.html'
    context_object_name = 'organization'
org_detail = OrgDetailView.as_view()

class OrgTasks(DetailView):
    model = Organization
    pk_url_kwarg = 'org_id'
    template_name = 'org_tasks.html'
    context_object_name = 'organization'

    def get_context_data(self, **kwargs):
        _super = super(DetailView, self)
        context = _super.get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(organizer_id=self.object.id)
        return context
org_tasks = OrgTasks.as_view()