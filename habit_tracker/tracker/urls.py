from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='tracker/login.html'), name='login'),
    path('home/', views.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add/', views.add_habit, name='add_habit'),
    path('update/<int:habit_id>/', views.update_habit, name='update_habit'),
    path('delete/<int:habit_id>/', views.delete_habit, name='delete_habit'),
]
