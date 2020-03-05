from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('meets/', views.MeetList.as_view(), name='meet_list'),
    path('meets/<int:pk>', views.MeetDetail.as_view(), name='meet_detail')
]