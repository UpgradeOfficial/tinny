from rest_framework import serializers
from .models import URLShortener


class URLShortenerSerializer(serializers.ModelSerializer):

    class Meta:
        model = URLShortener
        fields = ('name', 'url', 'unique_id')