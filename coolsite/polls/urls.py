from django.urls import path

from .views import ViewHome

app_name = 'polls'
urlpatterns = [
    path('', ViewHome.as_view(), name='home')
]

