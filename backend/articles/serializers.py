from rest_framework import serializers

from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = Article
        fields = '__all__'

