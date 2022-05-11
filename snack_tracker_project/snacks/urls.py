import imp
from django.urls import path
from .views import SnackDetailView , SnackListView

urlpatterns = [
    path('snack-list' , SnackListView.as_view() , name = 'snack-list'),
    path('snack-detail/<int:pk>' , SnackDetailView.as_view() , name ='snack-detail')
]