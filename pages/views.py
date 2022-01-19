from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Page
from .forms import PageForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from django.urls import reverse_lazy, reverse

# Create your views here.

# Return List of instances of a model
# def pages(request):
#     pages = get_list_or_404(Page)
#     return render(request, 'pages/pages.html', {'pages':pages})
class StaffRequiredMIxin(object):
    """Este mixin requerira que el usuario sea miembo del staff"""

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        # el decorador suplanta este codigo
        # manage request
        # if not request.user.is_staff:
        #     return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMIxin,self).dispatch(request, *args, **kwargs)



class PageListView(ListView):
    model = Page

# Return an instance of a model
# def page(request, page_id, page_slug):
#     page = get_object_or_404(Page, id=page_id)
#     return render(request, 'pages/page.html', {'page':page})

class PageDetailView(DetailView):
    model = Page

class PageCreate(StaffRequiredMIxin, CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')

class PageUpdate(StaffRequiredMIxin, UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

class PageDelete(StaffRequiredMIxin, DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')