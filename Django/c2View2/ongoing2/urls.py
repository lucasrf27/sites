from .views import HomeView, DetailView, OngoingCreate, OngoingUpdate
from . import views
from .views import OngoingDelete
from django.urls import path


urlpatterns = [
    path('', HomeView.as_view(), name='home2'),
    path('amp', views.index, name='home3'),
    path('detail/<int:pk>', DetailView.as_view(), name='detail2'),
    path('ADD', OngoingCreate.as_view(), name='add2'),
    path('update/<int:pk>', OngoingUpdate.as_view(), name='update2'),
    path('delete/<int:pk>', OngoingDelete.as_view(), name='delete2'),
]
