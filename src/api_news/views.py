from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    RetrieveAPIView,
)

from api_news.models import Post, Comment

from api_news.serializers import (
    PostListSerializer,
    PostCreateSerializer,
    CommentCreateSerializer,
    CommentListSerializer,
)


class PostCreate(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostUpdate(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer


class PostDelete(RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer


class CommentCreate(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer


class CommentList(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer


class CommentUpdate(RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer


class CommentDelete(RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer


class PostUpvote(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def get_object(self):
        obj = super().get_object()
        obj.amount_of_upvotes += 1
        obj.save()
        return obj
