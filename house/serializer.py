from rest_framework import serializers
from .models import MakerCard, Reviews, Expense
from django.contrib.auth.models import User

class MakerCardSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = MakerCard
        fields = '__all__' 
    def get_image_url(self, maker):
        request = self.context.get('request')
        image_url = maker.images.url
        return request.build_absolute_uri(image_url)
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__' 


class ExpenseSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Expense()
        fields = '__all__' 
    def get_image_url(self, expense):
        request = self.context.get('request')
        image_url = ""
        if expense.image:
            image_url = request.build_absolute_uri(expense.image.url)
        return image_url
