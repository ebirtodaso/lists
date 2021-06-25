from django.views import generic
from django.urls import reverse_lazy
from .models import listItem
from .forms import doneForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

class IndexView(generic.ListView):
    template_name = 'list/index.html'
    context_object_name = 'list'

    def get_queryset(self):
        """Return the all items in list."""
        return listItem.objects.all()

class CreateView(generic.edit.CreateView):
  template_name = 'list/create.html'
  model = listItem
  fields = ['item']
  success_url = reverse_lazy( 'lists:index')

class UpdateView(generic.edit.UpdateView):
    template_name =  'list/update.html'
    model = listItem
    fields = ['item']
    success_url = reverse_lazy( 'lists:index')

class DeleteView(generic.edit.DeleteView):
    template_name =  'list/delete.html' # override default of listItems listItem_confirm_delete.html
    model = listItem
    success_url = reverse_lazy( 'lists:index')

def DoneView(request, pk):
  list_item = get_object_or_404(listItem, pk=pk)
  form = doneForm(request.POST or None)

  if request.method == 'POST':
    if form.is_valid():
      if request.POST.get('done'):
        list_item.isDone = True
        list_item.save()
      else:
        list_item.isDone = False
        list_item.save()

  return HttpResponseRedirect(reverse_lazy('lists:index'))


