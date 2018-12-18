from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$', views.index, name='home'),
    url(r'^image/$', views.new_image, name='upload_image'),
    url(r'^search/$', views.search_user, name='search_profile'),
    url(r'^comment/(?P<image_id>\d+)', views.comment, name='comment'),
    url(r'^like/(?P<image_id>\d+)', views.like, name='like')
    url(r'^profile/', views.profile, name='profile'),
    url(r'^user/(\d+)$', views.profile, name='profile'),
    url(r'^updateprofile/(?P<id>\d+)', views.update_profile, name='updateprofile')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
