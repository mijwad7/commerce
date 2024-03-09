from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create/", views.create, name="create"),
    path("listing/<int:id>", views.listing, name="listing"),
    path("watchlist/<int:id>", views.watchlist, name="watchlist"),
    path("view_watchlist/", views.view_watchlist, name="view_watchlist"),
    path("categories/", views.categories, name="categories"),
    path("category/<str:category>", views.category, name="category"),
    path("close_auction/<int:id>", views.close_auction, name="close_auction"),
    path("comment/<int:id>", views.comment, name="comment"),
    path("add_comment/<int:id>", views.add_comment, name="add_comment")
]
