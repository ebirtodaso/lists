#Django libraries
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # For user creation
from django.contrib.auth import logout, authenticate, login # User authentication
from django.contrib import messages

#Defined Libraries
from .models import listItem, List
from .forms import doneForm, addItemForm

class IndexView(generic.ListView):
    template_name = 'list/index.html'
    context_object_name = 'list'

    def get_queryset(self):
        """Return the all items in list."""
        return List.objects.all()      

# Create a list
class CreateListView(generic.edit.CreateView):
  template_name = 'list/create.html'
  model = List
  fields = ['list_name']
  success_url = reverse_lazy( 'lists:index')

# Add item to a list
class AddItemView(generic.edit.CreateView):
  template_name = 'list/create.html'
  model = listItem
  fields = ['item', 'list_name']
  success_url = reverse_lazy( 'lists:index')

# Update list
class UpdateView(generic.edit.UpdateView):
    template_name =  'list/update.html'
    model = List
    fields = ['list_name']
    success_url = reverse_lazy( 'lists:index')

# Update list
class UpdateItemView(generic.edit.UpdateView):
    template_name =  'list/update_item.html'
    model = listItem
    fields = ['item', 'isDone']
    success_url = reverse_lazy( 'lists:index')

# Delete list
class DeleteView(generic.edit.DeleteView):
    template_name =  'list/delete.html' # override default of listItems listItem_confirm_delete.html
    model = List
    success_url = reverse_lazy( 'lists:index')

# Delete item
class DeleteItemView(generic.edit.DeleteView):
    template_name =  'list/delete_item.html' # override default of listItems listItem_confirm_delete.html
    model = listItem
    success_url = reverse_lazy( 'lists:index')

# Saves checkbox value after user submits
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

# Registers a user to database
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

# Logout 
def logout_request(request):
  logout(request)
  messages.info(request, "Logged out successfully!")
  return redirect("lists:index")

# Login for authenticated users
def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "list/login.html",
                    context={"form":form})