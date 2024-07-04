from rest_framework import serializers

class LanguagesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    active = serializers.BooleanField()

class MainMenuSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    url = serializers.CharField(max_length=200)
    lang_id_id = serializers.IntegerField()
    position = serializers.IntegerField()
    active = serializers.BooleanField()

class FooterMenuSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    url = serializers.CharField(max_length=200)
    lang_id = serializers.IntegerField()
    position = serializers.IntegerField()
    active = serializers.BooleanField()

class PagesSerializer(serializers.Serializer):
    page_name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    key_works = serializers.CharField(max_length=200)
    content = serializers.CharField(max_length=200)
    active = serializers.BooleanField()

class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    description = serializers.CharField(max_length=200)
    date = serializers.DateTimeField(format="%d-%m-%Y")
    image = serializers.CharField(max_length=100)
    active = serializers.BooleanField()