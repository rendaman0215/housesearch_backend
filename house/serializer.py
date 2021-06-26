from rest_framework import serializers
from .models import MakerCard, Reviews, Expense

class MakerCardSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = MakerCard
        fields = ('pk', 'name', 'name_hira', 'name_kata', 'name_eng', 'image_url', 'get_review_count', 'get_expense_count', 'get_expense_avg', 'get_landarea_avg', 'get_rateavg', 'ratetostr', 'get_costavg', 'get_designavg', 'get_layoutavg', 'get_specavg', 'get_guaranteeavg', 'get_salesavg')
        read_only_fields = ('pk','created_at',)
    def get_image_url(self, maker):
        request = self.context.get('request')
        image_url = maker.images.url
        return request.build_absolute_uri(image_url)
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('pk','author', 'status', 'costrate', 'costcomment', 'designrate', 'designcomment', 'layoutrate', 'layoutcomment', 'specrate', 'speccomment', 'guaranteerate', 'guaranteecomment', 'salesrate', 'salescomment', 'avgrate', 'get_rateavg', 'maker_name', 'create_date')
        read_only_fields = ('pk','created_at',)

class ExpenseSerializer(serializers.ModelSerializer):
    expimage_url = serializers.SerializerMethodField()
    layoutimage_url = serializers.SerializerMethodField()

    class Meta:
        model = Expense
        fields =  ('pk','author', 'status', 'cost', 'landarea', 'gradecomment', 'costupcomment', 'costdowncomment', 'hid', 'expimage_url', 'layoutimage_url', 'maker_name', 'create_date')
        read_only_fields = ('pk','created_at','hid', )

    def get_expimage_url(self, expense):
        request = self.context.get('request')
        expimage_url = ""
        if expense.expimage:
            expimage_url = request.build_absolute_uri(expense.expimage.url)
        return expimage_url

    def get_layoutimage_url(self, expense):
        request = self.context.get('request')
        layoutimage_url = ""
        if expense.layoutimage:
            layoutimage_url = request.build_absolute_uri(expense.layoutimage.url)
        return layoutimage_url