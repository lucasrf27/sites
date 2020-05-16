from .views import MP4View, HomeView, MP4create, MP4update, TutorialView, MP4delete
from .views import Tutorialcreate, TutorialDelete, TutorialUpdate
from django.urls import path
from .import views

urlpatterns = [
    # c2vconfig/
    path('', HomeView.as_view(), name='home'),
    # c2vconfig/MP4
    path('MP4', MP4View.as_view(), name='MP4'),
    # c2vconfig/MP4.amp
    path('MP4.amp', views.ampView, name='MP4.amp'),
    # c2vconfig/MP4/add/
    path('MP4/add/', MP4create.as_view(), name='add'),
    # c2vconfig/MP4/update/id
    path('MP4/update/<int:pk>', MP4update.as_view(), name='update'),
    # c2vconfig/MP4/delete/id
    path('MP4/delete/<int:pk>', MP4delete.as_view(), name='delete'),
    # c2vconfig/tutorial
    path('tutorial/', TutorialView.as_view(), name='tutorial'),
    # c2vconfig/tutorial/add
    path('tutorial/add', Tutorialcreate.as_view(), name='tutorial-add'),
    # c2vconfig/tutorial/update/id
    path('tutorial/update/<int:pk>', TutorialUpdate.as_view(), name='tutorial-update'),
    # c2vconfig/tutorial/delete/id
    path('tutorial/delete/<int:pk>', TutorialDelete.as_view(), name='tutorial-delete'),
]
