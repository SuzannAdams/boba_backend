from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import MeetSerializer
from .models import Meet

class MeetList(generics.ListCreateAPIView):
    queryset = Meet.objects.all()
    serializer_class = MeetSerializer

class MeetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meet.objects.all()
    serializer_class = MeetSerializer