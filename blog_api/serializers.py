# we are defining models here
# what data to serialize, how to structure them
# so that the front-end understands better

from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # which parts of model do we want
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'status')
    