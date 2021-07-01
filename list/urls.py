from django.urls import path

from . import views

app_name = 'lists'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new', views.CreateView.as_view(), name='create'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
    path('<int:pk>/done', views.DoneView, name='done'),
    path('register/', views.register, name='register'),
    path("logout", views.logout_request, name='logout'),
    path("login", views.login_request, name="login"),
]