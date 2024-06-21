from rest_framework.response import Response
from rest_framework.views import APIView

# from fdc_corp.models import News
# from fdc_corp.serializers import NewsSerializer

class test(APIView):
    # def get(self, request):
    #     queryset = News.objects.all()
    #     serializer_for_queryset = NewsSerializer(
    #         instance=queryset,
    #         many=True
    #     )
    #     return Response(serializer_for_queryset.data)
    def post(self, request):
        return Response("Post")
