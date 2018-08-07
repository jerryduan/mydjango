from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^question_list_temp/', views.question_list_temp),
    url(r'^question_list/', views.question_list),
]