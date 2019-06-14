from django.shortcuts import render

# Create your views here.
from .models import notedata
from .serializer import notedataModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response



class noteViewSet(ModelViewSet):
	model=notedata
	serializer_class=notedataModelSerializer
	permission_classes=()
	queryset=notedata.objects.all()


def get_query(self):
	if 'ntopic' in self.request.GET:
		return notedata.objects.filter(ntopic=self.request.GET['ntopic']).values()

	else:
		return notedata.objects.all().values()


