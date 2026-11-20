from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class ProductViewSet(ViewSet):
    """
    Product CRUD API
    """

    def list(self, request):
        return Response({"message": "상품 목록"})

    def retrieve(self, request, pk=None):
        return Response({"message": f"{pk}번 상품 상세"})

    def create(self, request):
        return Response({"message": "상품 생성"}, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        return Response({"message": f"{pk}번 상품 수정"})

    def destroy(self, request, pk=None):
        return Response(status=status.HTTP_204_NO_CONTENT)
