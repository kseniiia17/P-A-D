from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
    path('create_color', views.create_color, name='create_color'),
    path('<int:pk>/delete_color', views.ColorDeleteView, name='color-delete'),
    path('registr', views.register_view, name='registr'),
    path('login', views.login_view, name='login'),
    path('user_logout', views.user_logout, name='logout'),
    path('profile', views.profile_view, name='profile'),
    path('update_user/<int:user_id>/', views.update_user, name='update_user')
]