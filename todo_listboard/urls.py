from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'todo_listboard'

urlpatterns = [
    url(r'^$', views.Todo_listBoard.as_view(), name='todo_listboard'),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)