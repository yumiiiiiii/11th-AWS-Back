from .serializers import *

from rest_framework import viewsets, filters

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


    def perform_create(self, serializer):
        serializer.save()
