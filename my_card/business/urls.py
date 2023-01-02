from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from . import views

app_name = 'business'
urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('<int:pk>/', views.detail, name='project'),
    path('reviews/', views.reviews, name='reviews'),]

