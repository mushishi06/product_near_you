from django.urls import path, re_path

from shops import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.search_shops_near, name='Search By position'),
    re_path(r'(?P<pk>[a-zA-z]+)/$', views.search_shops_name, name="Search By Name"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
