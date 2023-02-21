from posts.models import Comment, Group, Post
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(
        read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')
        read_only_fields = ('author',)

        validators = [
            UniqueTogetherValidator(
                queryset=Post.objects.all(),
                fields=('text', 'author'),
                message='А вы точно не создавали такой пост раньше?'
            )
        ]
