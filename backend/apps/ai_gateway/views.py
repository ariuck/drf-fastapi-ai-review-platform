from rest_framework.response import Response
from rest_framework.views import APIView


class SentimentAnalysisAPIView(APIView):

    def post(self, request):
        return Response({"message": "감성 분석 요청 접수"})
