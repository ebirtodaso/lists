#Django libraries
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm # For user creation
from django.contrib.auth import logout, authenticate, login # User authentication
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


#Defined Libraries
from .models import listItem
from .forms import doneForm

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

def register(request):

    if request.method == "POST":
      form = UserCreationForm(request.POST)
      if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("lists:index")
      else:
        for msg in form.error_messages:
                  print(form.error_messages[msg])

        return render(request = request,
                      template_name = "list/register.html",
                      context={"form":form})
      
    form = UserCreationForm
    return render(request = request,
                  template_name = "list/register.html",
                  context={"form":form})

def logout_request(request):
  logout(request)
  messages.info(request, "Logged out successfully!")
  return redirect("lists:index")

def login_request(request):
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "main/login.html",
                  context={"form":form})