from django.urls import path, include
from .views import CategoryView, ArticleView
from rest_framework import routers

router = routers.DefaultRouter()

router.register('category', CategoryView)
router.register('article', ArticleView)


urlpatterns = [
    path('', include(router.urls)),
]
