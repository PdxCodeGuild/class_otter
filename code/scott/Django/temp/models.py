# articles/models.py
from django.db import models

from src.articles.models import Article
from src.articles.serializer import ArticleSerializer


class ArticleManager(models.Manager):
    def by_regions(self, regions, region_separator=","):
        """
        Restricts the returned articles to given regions
        """
        if regions:
            qs = self.prefetch_related("regions")
            for region in regions.split(region_separator):
                qs = qs.filter(regions__code=region)

            return qs

        return self.all()


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    regions = models.ManyToManyField(
        "Region", related_name="articles", blank=True
    )

    objects = ArticleManager()

    def __str__(self):
        return self.title

    ...