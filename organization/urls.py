from django.urls import path

from organization.views.article_views import (
    ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleListView
)
from organization.views.city_views import (
    CityListView, CityCreateView, CityUpdateView, CityDeleteView, CityDetailView
)
from organization.views.comment_views import (
    CommentCreateView, CommentDetailView, CommentUpdateView, CommentDeleteView
)
from organization.views.user_views import (
    UserDetailView, UserCreateView, UserUpdateView, UserDeleteView, UserListView
)
from organization.views.views import index


app_name = "organization"

urlpatterns = [
    path("", index, name="index"),

    # City
    path("cities/", CityListView.as_view(), name="city-list"),
    path("cities/create/", CityCreateView.as_view(), name="city-create"),
    path("cities/<int:pk>/update/", CityUpdateView.as_view(), name="city-update"),
    path("cities/<int:pk>/delete/", CityDeleteView.as_view(), name="city-delete"),
    path("cities/<int:pk>/", CityDetailView.as_view(), name="city-detail"),

    # User
    path("users/", UserListView.as_view(), name="user-list"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("users/create/", UserCreateView.as_view(), name="user-create"),
    path("users/<int:pk>/update/", UserUpdateView.as_view(), name="user-update"),
    path("users/<int:pk>/delete/", UserDeleteView.as_view(), name="user-delete"),

    # Article
    path("articles/", ArticleListView.as_view(), name="article-list"),
    path("articles/create/", ArticleCreateView.as_view(), name="article-create"),
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    path("articles/<int:pk>/update/", ArticleUpdateView.as_view(), name="article-update"),
    path("articles/<int:pk>/delete/", ArticleDeleteView.as_view(), name="article-delete"),

    # Comment
    path("comments/create/", CommentCreateView.as_view(), name="comment-create"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),
    path("comments/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
]
