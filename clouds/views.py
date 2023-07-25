from rest_framework import generics
from .serializer import CloudSerializer
from .models import Cloud

class CloudList(generics.ListCreateAPIView):
  queryset = Cloud.objects.all()
  serializer_class = CloudSerializer
  
class CloudDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Cloud.objects.all()
  serializer_class = CloudSerializer