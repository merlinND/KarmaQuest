import datetime
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from tasks.models import Task

def home_feed(request):
    """
    Show the user's home feed.
    """
    return render_to_response('home.html')

def list_all_tasks(request):
    """
    List all the active tasks, adding a few features
    """

class ListTasksView(ListView):
    http_method_names = ['get']
    template_name = 'all_tasks.html'
    context_object_name = 'tasks'
    paginate_by = 30

    def get_queryset(self):
        tasks = Task.objects.filter(start_date__gt=datetime.date.today())
        return tasks.order_by('-start_date')

    def get_context_data(self, **kwargs):
        _super = super(ListTasksView, self)
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
        page_numbers = [n for n in xrange(startPage, endPage) \
                if n > 0 and n <= num_pages]
        context.update({
            'page_numbers': page_numbers,
            'show_first': 1 not in page_numbers,
            'show_last': num_pages not in page_numbers,
            })
        return context
list_all_tasks = ListTasksView.as_view()
