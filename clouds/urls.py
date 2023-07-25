from django.urls import path
from .views import CloudList, CloudDetail

urlpatterns = [
  path('', CloudList.as_view(), name='cloud_list'),
  path('<int:pk>', CloudDetail.as_view(), name='cloud_detail'),
]