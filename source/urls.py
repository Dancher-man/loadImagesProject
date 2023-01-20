from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/images/', ImagesAPIListView.as_view()),
    path('api/v1/images/<int:pk>', ImagesAPIListView.as_view()),
    path('api/v1/images/filter', ImageFilterView.as_view()),
    path('api/v1/images/search', PeopleNameSearchView.as_view()),
]
