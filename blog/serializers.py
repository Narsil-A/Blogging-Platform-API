from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    createdAt = serializers.DateTimeField(source='created_at', read_only=True)
    updatedAt = serializers.DateTimeField(source='updated_at', read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'category', 'tags', 'createdAt', 'updatedAt']
