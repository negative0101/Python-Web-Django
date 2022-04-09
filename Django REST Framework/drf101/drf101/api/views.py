from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins as api_mixins
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView

from drf101.api.models import Product, Category


class CategoryForProductSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class ProductSerializer(ModelSerializer):
    #Nested serializer.
    category = CategoryForProductSerializer()
    class Meta:
        model = Product
        fields = "__all__"


class ManualProductsListView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)


"""
ListAPIView
RetrieveAPIView
CreateAPIView
DestroyAPIView
UpdateAPIView

"""


class ProductsListViews(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SingleProductView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RandomView(ListAPIView, api_mixins.DestroyModelMixin):
    pass
