from django.urls import path

from .views import (
    CountryRecordListCreateAPIView,
    CountryRecordRetrieveDeleteAPIView,
)

urlpatterns = [
    path('countries/', CountryRecordListCreateAPIView.as_view(), name='country-list'),
    path('countries/create/', CountryRecordListCreateAPIView.as_view(), name='country-create'),
    path('countries/<int:pk>/delete/', CountryRecordRetrieveDeleteAPIView.as_view(), name='country-destroy'),
]
