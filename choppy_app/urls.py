from django.urls import path
from .views import SupportCompanyListView,AlbumListView


urlpatterns = [
    path('supportcompanys',SupportCompanyListView.as_view()),
    path('albums',AlbumListView.as_view()),
]
