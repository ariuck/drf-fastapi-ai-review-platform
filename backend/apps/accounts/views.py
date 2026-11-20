from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class UserViewSet(ViewSet):

    def list(self, request):
        return Response({"message": "사용자 목록"})

    def retrieve(self, request, pk=None):
        return Response({"message": f"{pk}번 사용자 상세"})
