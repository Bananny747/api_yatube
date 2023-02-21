from django.core.exceptions import PermissionDenied
from posts.models import Comment, Group, Post
from rest_framework import viewsets

from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Чужое не трожь!')
        serializer.save()

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Чужое не трожь!')
        instance.delete()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.kwargs.get('post_id'))
        serializer.save(
            author=self.request.user,
            post=post)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Чужое не трожь!')
        post = Post.objects.get(id=self.kwargs.get('post_id'))
        serializer.save(post=post)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Чужое не трожь!')
        instance.delete()
