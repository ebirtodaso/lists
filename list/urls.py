from django.urls import path
from . import views

app_name = 'lists'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new', views.CreateListView.as_view(), name='create'),
    path('additem', views.AddItemView.as_view(), name='additem'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
    path('update/<int:list_id>/<int:pk>', views.UpdateItemView.as_view(), name='updateitem'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
    path('delete/<int:list_id>/<int:pk>', views.DeleteItemView.as_view(), name='deleteitem'),
    path('<int:pk>/done', views.DoneView, name='done'),
    path('register/', views.register, name='register'),
    path('logout', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
]