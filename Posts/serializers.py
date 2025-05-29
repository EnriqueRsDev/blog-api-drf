from rest_framework.serializers import ModelSerializer
from .models import Posts


class PostSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = ['id','title','content','author','publish_date',]
        read_only_fields = ['id','author', 'publish_date']