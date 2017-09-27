"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import views
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name = 'index'),
    url(r'^main$', views.main, name = 'main'),
    url(r'^register$', views.register, name = 'registration'),
    url(r'^clearsession$',views.clearsession, name='logout'),
    url(r'^login$', views.login, name = 'login'),
    url(r'^travels$', views.travels, name = 'travels'),
    url(r'^travels/add_travel$', views.add_travel, name = 'add_travel'),

    url(r'^travels/destination/(?P<trip_id>\d+)$', views.trip_review, name = "trip_review"),
    url(r'^travels/destination/(?P<trip_id>\d+)/join', views.join, name = "join"),
    # url(r'^activity', views.activity, name = 'activity'),
    # url(r'^reset$', views.reset, name = 'reset'),

]
