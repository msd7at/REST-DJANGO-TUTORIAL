from django.urls import path,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url

urlpatterns=[
    path('',views.PersonView.as_view()),
    path('person/<int:id>/destroy',views.PersonRUD.as_view()),
]