from rest_framework import routers

from articles.views import ArticleViewSet

api = routers.DefaultRouter()
api.trailing_slash = '/?'

api.register(r'articles', ArticleViewSet)
