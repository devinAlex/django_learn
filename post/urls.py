from django.conf.urls import url
from post import views
urlpatterns = [
    url(r'^category/$', views.getAllCategory),
    url(r'^category/post/(\d+)$', views.get_post_by_category),
]