from rest_framework import serializers, validators
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["title", "content", "author", "date_created"]
        extra_kwargs = {
        "author" : {
            "read_only" : True,
        },
        "date_created" : {
            "read_only" : True,
        }
    }