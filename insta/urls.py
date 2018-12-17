from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$', views.index, name='index'),
    url(r'^comment/$', views.add_comment, name='comment'),
    url(r'^like/(?P<image_id>\d+)', views.like, name='like'),
    url(r'^follow/(\d+)$', views.follow, name='follow'),
    url(r'^unfollow/(\d+)$', views.unfollow, name='unfollow')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
