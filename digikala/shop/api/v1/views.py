from django.shortcuts import get_object_or_404
from shop.models import Product
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(["get", "post"])
@permission_classes([IsAuthenticatedOrReadOnly])
def product_list_api_view(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["get", "put", "delete"])
def product_detail_api_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        product.delete()
        return Response(
            {"deleted": "successfully deleted"}, status=status.HTTP_204_NO_CONTENT
        )
