
from django.urls import path
from . views import *
urlpatterns = [
    path("",home,name='home'),
    path('topics-list/<int:pk>',topics_list,name='topics_list'),
    path('topic-create/',topic_create,name='topic_create'),
    path('create/', create, name='create'),
]