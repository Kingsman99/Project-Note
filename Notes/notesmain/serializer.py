from rest_framework import serializers
from .models import notedata


# class notedataserializer(serializers.Serializer):
# 	ntopic=serializers.CharField(max_length=100)
# 	ndetail=serializers.CharField(max_length=1000)
# 	ndate=serializers.CharField(max_length=10)


class notedataModelSerializer(serializers.ModelSerializer):
	class Meta:
		model=notedata
		fields='__all__'

