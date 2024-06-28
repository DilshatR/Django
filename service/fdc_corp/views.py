from rest_framework.response import Response
from rest_framework.views import APIView

from fdc_corp.models import News, MainMenu, FooterMenu, Languages, Pages
from fdc_corp.serializers import NewsSerializer, MainMenuSerializer, FooterMenuSerializer, LanguagesSerializer, PagesSerializer

class news(APIView):
    def post(self, request):
        queryset = News.objects.all()
        serializer_for_queryset = NewsSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)

class mainMenu(APIView):
    def post(self, request):
        queryset = MainMenu.objects.all()
        serializer_for_queryset = MainMenuSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)

class footerMenu(APIView):
    def post(self, request):
        queryset = FooterMenu.objects.all()
        serializer_for_queryset = FooterMenuSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)

class pages(APIView):
    def post(self, request):
        queryset = Pages.objects.all()
        serializer_for_queryset = PagesSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)

class lang(APIView):
    def post(self, request):
        queryset = Languages.objects.all()
        serializer_for_queryset = LanguagesSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)
