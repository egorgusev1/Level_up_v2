from django.urls import path
from app.views import (
    ArticleListView,
    ArticleCreateView,
    ArticleDeleteView,
    ArticleUpdateView,
)


# Define the URL patterns for the article app
urlpatterns = [
    path("",ArticleListView.as_view(), name = "home"),
    path("create/",ArticleCreateView.as_view(), name = "create_article"),
    
    # <int:pk> captures the primary key (ID) of the article to update
    path("<int:pk>/update/",ArticleUpdateView.as_view(), name = "update_article"),
    path("<int:pk>/delete/",ArticleDeleteView.as_view(), name = "delete_article"),
]