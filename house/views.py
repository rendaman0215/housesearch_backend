# Model, Form, Serializer, Permissionをimport
from .models import MakerCard, Reviews, Expense
from .serializer import MakerCardSerializer, ReviewSerializer, ExpenseSerializer
from .permission import IsAdminOrReadOnly, IsMeOrAdminOrGuestOrOthers

# Django Filter
from django_filters import rest_framework as filters

# REST FRAMEWORK系
from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class isPosted(APIView):
    # ユーザー認証
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None, **kwargs):
        RevPosted = ""
        if Reviews.objects.filter(author=str(request.user), maker_name=self.kwargs['targetmaker']).exists():
            RevPosted = Reviews.objects.filter(author=str(request.user), maker_name=self.kwargs['targetmaker']).values_list('pk', flat=True)
            RevPosted = ', '.join(map(str, RevPosted))
        ExpPosted = ""
        if Expense.objects.filter(author=str(request.user), maker_name=self.kwargs['targetmaker']).exists():
            ExpPosted = Expense.objects.filter(author=str(request.user), maker_name=self.kwargs['targetmaker']).values_list('pk', flat=True)
            ExpPosted = ', '.join(map(str, ExpPosted))
        return Response({'RevPosted':RevPosted, 'ExpPosted':ExpPosted})

class MakerCardViewSet(viewsets.ModelViewSet):
    """ Maker Informations """
    # キーを指定
    lookup_field = "name_eng"
     # モデル
    queryset = MakerCard.objects.all()
    # ユーザー認証
    permission_classes = [IsAdminOrReadOnly]
    # シリアライザー
    serializer_class = MakerCardSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    """ Review Informations """
    # モデル
    queryset = Reviews.objects.order_by('-create_date')
    # ユーザー認証
    permission_classes = (IsMeOrAdminOrGuestOrOthers,)
    # シリアライザー
    serializer_class = ReviewSerializer
    # フィルター
    filter_fields = ('maker_name','author',) 

class ExpenseViewSet(viewsets.ModelViewSet):
    """ Expense Informations """
    # モデル
    queryset = Expense.objects.order_by('-create_date')
    # ユーザー認証
    permission_classes = (IsMeOrAdminOrGuestOrOthers,)
    # シリアライザー
    serializer_class = ExpenseSerializer
    # フィルター
    filter_fields = ('maker_name','author',) 

class PingViewSet(generics.GenericAPIView):
    # ユーザー認証
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        return Response(data={'username': request.user.username}, status=status.HTTP_200_OK)