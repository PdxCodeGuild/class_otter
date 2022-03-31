# students/views.py

# articles/views.py
from rest_framework import generics

from src.articles.models import Article
from src.articles.serializer import ArticleSerializer


class ArticleListView(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned articles to given regions,
        by filtering against a `regions` query parameter in the URL.
        """
        regions = self.request.query_params.get("regions", None)

        return Article.objects.by_regions(regions=regions)