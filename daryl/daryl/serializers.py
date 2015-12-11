from rest_framework import serializers
from daryl.models import *


class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields = ('filename','category')

	def create(self, validated_data):
		filename = validated_data.get('filename', None)
		category = validated_data.get('category', None)
		return Image.objects.create(filename=filename, category=category)

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('name','category_id')

	def create(self, validated_data):
		name = validated_data.get('name', None)
		category_id = validated_data.get('category_id', None)
		return Category.objects.create(name=name, category_id=category_id)
