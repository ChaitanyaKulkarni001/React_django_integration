from .models import Movie
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
    
    
    
    
# class MovieSerializer(serializers.Serializer):
    # name = serializers.CharField(max_length=30)
    # desc = serializers.CharField(max_length=100)
    # img_url = serializers.URLField()
    # rating = serializers.IntegerField()