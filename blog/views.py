from .models import Post, Comment, Category
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = serializers.PostSerializer


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def create(self, request, *args, **kwargs):
        super(PostCreateView, self).create(request, *args, **kwargs)
        response = {
            "status_code" : status.HTTP_200_OK,
            "message" : "Succesfully created",
            "result" : request.data
        }

        return Response(response)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        super(PostDetailView, self).retrieve(request, *args, **kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Succesfully retrieved",
            "result": data
        }

        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(PostDetailView, self).patch(request, *args, **kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data

        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Succesfully retrieved",
            "result": data
        }

    def delete(self, request, *args, **kwargs):
        super(PostDetailView, self).delete(request, *args, **kwargs)
        
        data = serializer.data

        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Succesfully deleted",
            "result": data
        }

        return Response(response)

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def create(self, request, *args, **kwargs):
        super(CommentCreateView, self).create(request, *args, **kwargs)
        response = {
            "status_code" : status.HTTP_200_OK,
            "message" : "Succesfully created",
            "result" : request.data
        }

        return Response(response)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer



class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        super(CategoryDetailView, self).retrieve(request, *args, **kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Succesfully retrieved",
            "result": data
        }

        return Response(response)

