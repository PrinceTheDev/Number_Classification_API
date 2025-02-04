from django.urls import path
from .views import Number_Classification


urlpatterns = [
    path('api/classify-number', Number_Classification.as_view(), name='classify-number'),
]
