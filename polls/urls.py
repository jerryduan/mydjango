from django.conf.urls import url, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
router.register(r'choices', views.ChoiceViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^question_list_temp/', views.question_list_temp),
    url(r'^question_list/', views.question_list),
]

