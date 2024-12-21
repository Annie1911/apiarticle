from django.shortcuts import render
from rest_framework import viewsets
from .models import Article
from .serializers import *



class ArticleSerializer(viewsets.ModelViewSet):

    list_serializer_article = ArticleListSerializer

    detail_serializer_article = DetailArticleSerializer 

    def get_serializer_class(self):

        if self.action =='retrieve':
            return self.detail_serializer_article
        return super().get_serializer_class