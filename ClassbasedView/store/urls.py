from django.urls import path
from .views import (
    IndexView, HomeView, BookDetailView, BookListView,
    BookCreateView, BookUpdateView
    )
# from django.views.generic.base import TemplateView

app_name = "store"

urlpatterns = [
    path("index/", IndexView.as_view(), name="index"),
    # path("home/", TemplateView.as_view(template_name="home.html"), name="home"),
    path("home/<name>", HomeView.as_view(), name="home"),
    path("detail_book/<int:pk>", BookDetailView.as_view(), name="book_detail"),
    path("list_books/", BookListView.as_view(), name="list_books"),
    path("list_books/<name>", BookListView.as_view(), name="list_books"),
    path("add_book/", BookCreateView.as_view(), name="add_book"),
    path("edit_book/<int:pk>", BookUpdateView.as_view(), name="edit_book"),
    path("delete_book/<int:pk>", BookDetailView.as_view(), name="delete_book"),
]
