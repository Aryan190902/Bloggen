from django.urls import path
# from . import views
from .views import About, Category, DeletePost, EditPost, HomeView, Article, AddPost, AddCategory, Cat, LikePost, AddComment

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', Article.as_view(), name="articleDetail"),
    path('about/', About.as_view(), name="about"),
    path('add_post/', AddPost.as_view(), name="add_post"),
    path('article/edit/<int:pk>', EditPost.as_view(), name="edit_post"),
    path('article/<int:pk>/delete', DeletePost.as_view(), name="delete_post"),
    path('add_category/', AddCategory.as_view(), name="add_category"),
    path('categories/', Category, name="category"),
    path('categories/<str:cats>/', Cat, name="cats"),
    path('like/<int:pk>', LikePost, name="like_post"),
    path('article/<int:pk>/comment/', AddComment.as_view(), name="add_comment")
]
