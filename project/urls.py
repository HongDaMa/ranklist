"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from ranklist import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^uploading_score/$',views.Uploading_Score.as_view(),name='uploading_score'),
    url('^select_ranking/(?P<port_id>\d+)/((?P<begin>\d+)-(?P<end>\d+)/)?$',views.Select_Ranking.as_view(),name='select_ranking'),
]
