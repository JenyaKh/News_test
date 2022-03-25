from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api_news.models import Post, Comment


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "link", "author_name", "comments"]


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["author_name", "content", "post_id"]


class CommentListSerializer(ModelSerializer):
    post = serializers.ReadOnlyField(source="post.title")

    class Meta:
        model = Comment
        fields = "__all__"


class PostListSerializer(ModelSerializer):
    comments = CommentListSerializer(many=True)

    class Meta:
        model = Post
        fields = "__all__"
