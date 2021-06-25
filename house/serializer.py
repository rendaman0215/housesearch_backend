from rest_framework import serializers
from .models import MakerCard, Reviews, Expense, Picture

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

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(many=True, read_only=True)
    
    # ListSerializerと間違えないように注意
    additional_pictures = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False,
    )

    deletable_picture_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True, required=False,
    )

    class Meta:
        model = Expense
        fields = '__all__'
        read_only_fields = ('pk','created_at',)

    def create(self, validated_data):
        additional_pictures = validated_data.pop('additional_pictures', None)
        expense = Expense.objects.create(**validated_data)
        self._create_pictures(expense, additional_pictures)

        return expense

    def update(self, instance, validated_data):
        deletable_picture_ids = validated_data.pop('deletable_picture_ids', None)
        if deletable_picture_ids:
            Picture.objects.filter(pk__in=deletable_picture_ids).delete()

        additional_pictures = validated_data.pop('additional_pictures', None)
        super().update(instance, validated_data)
        self._create_pictures(instance, additional_pictures)

        return instance

    def _create_pictures(self, expense, additional_files):
        if additional_files is None:
            return

        files = []
        for file in additional_files:
            files.append(
                Picture(expense=expense, file=file, name=file.name),
            )
        if files:
            Picture.objects.bulk_create(files)
