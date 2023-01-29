from django.urls import path

from . import views
from .views import Detail, Home, ResultView

app_name = 'polls'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('<int:pk>/', views.Detail.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]
