from django.urls import path
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', views.index, name='index'),
    path('robots.txt', views.robots, name='robots'),
    path('index.html', RedirectView.as_view(url='/', permanent=False), name='index1'),
    path('index.php', RedirectView.as_view(url='/', permanent=False), name='index2'),
    path('services/', views.services, name='services'),
    path('services/<slug>/', views.service, name='service'),
    path('blog/', views.posts, name='posts'),
    path('blog/<slug>/', views.post, name='post'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('projects/<slug>', views.project, name='project'),
    path('callback/', views.callback, name='callback'),
]