"""askme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from myask import views as ask_views

urlpatterns = [

    url(r'^signup/?',ask_views.signup, name='signup'),
    url(r'^logout/?',ask_views.logout, name='logout'),
    url(r'^question/?', ask_views.question_answer, name='question_answer'),
    url(r'^add_answer/?', ask_views.add_answer, name='add_answer'),
    url(r'^registr/?', ask_views.registr, name='registr'),
    url(r'^new/?', ask_views.new_question, name='new_question'),
    url(r'^/hot/?',ask_views.noauto, name='noauto'),
    url(r'^search/?', ask_views.tagsearch, name='tag_search'),
    url(r'^/?',ask_views.noauto, name='noauto'),
    url(r'^/tag/blabla/?',ask_views.index, name='index'),
    url(r'^admin/', admin.site.urls),
]
