from .models import Post, Comment, Category
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('name', 'text', 'created', 'post')
        

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False)
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'is_featured', 'created', 'comments', 'id', 'category')
    


class CategorySerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)
    class Meta:
        model = Category
        fields = ('name', 'slug', 'posts')