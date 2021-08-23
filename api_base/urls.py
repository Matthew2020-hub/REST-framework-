from django import urls
from django.urls import path, include
from .views import (
    article_list, article_detail,
    ArticleApiView, ArticleDetails, 
    GenericAPIView, ArticleViewSet)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename= 'article')


urlpatterns = [
    path('viewset/', include(router.urls)),
    path('art/', article_list),
    path('API/', ArticleApiView.as_view()),
    # path('det/<int:pk>/', article_detail),
    path('det/<int:id>/', ArticleDetails.as_view()),
    path('generic/', GenericAPIView.as_view()),
]
