from rest_framework import serializers

class LanguagesSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    active = serializers.BooleanField()

class MainMenuSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    url = serializers.CharField(max_length=200)
    lang_id = serializers.IntegerField()
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
    description = serializers.TextField()
    key_works = serializers.TextField()
    content = serializers.TextField()
    active = serializers.BooleanField()

class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.TextField()
    date = serializers.DateTimeField()
    image = serializers.CharField(max_length=200)
    active = serializers.BooleanField()