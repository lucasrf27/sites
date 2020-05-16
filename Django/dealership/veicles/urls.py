from django.urls import path
from . views import DetailView, CategoryView, VeicleUpdate, amp_detail
from . import views



urlpatterns = [
    path('amp_home', views.amp_home, name='amp_home2'),
    path('category', CategoryView.as_view(), name='category2'),
    path('detail/<int:pk>', DetailView.as_view(), name='detail2'),
    path('update/<int:pk>', VeicleUpdate.as_view(), name='update2'),
    path('test', views.test_view, name='test2'),
    path('add', views.veicle_create2, name='add2'),
    path('amp_detail/<int:pk>', amp_detail.as_view(), name='amp_detail2'),
    path('amp_category', views.amp_category, name='amp_category2'),

    #TESTS#
    path('amp_category2', views.amp_category2, name='amp_category22'),
    path('amp_test', views.amp_test, name='amp_test2'),
    path('amp_test2', views.amp_test2, name='amp_test22'),
]
