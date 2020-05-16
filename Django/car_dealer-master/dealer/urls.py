from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    url(r'^cars$', CarList.as_view()),
    url(r'^cars/(?P<pk>[0-9]+)$', Car.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
