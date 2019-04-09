from django.conf.urls import url
from . import  views
from django.urls import path

app_name = "spam"
urlpatterns=[
url(r'^',views.hompage,name='hompage'),

]