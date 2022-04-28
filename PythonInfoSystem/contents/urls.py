from django.urls import path

from . import views

app_name = 'contents'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:topic_id>/', views.topic_detail, name='detail')
]

url(r'^register/$', views.register, name='register'),
