from django.conf.urls import url
from task_app import views

app_name = 'task_app'

urlpatterns=[
    url(r'^other/$',views.other,name='other'),
]
