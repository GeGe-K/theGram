from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$', views.index, name='index'),
    url(r'^image/$', views.new_image, name='new_image'),
    url(r'^search/$', views.search_user, name='search_profile'),
    url(r'^addcomment/(?P<image_id>\d+)', views.add_comment, name='addcomment'),
    url(r'^like/(?P<image_id>\d+)', views.like, name='like'),
    url(r'^accounts/profile/', views.profile, name='profile'),
    url(r'^profile/(\d+)$', views.user_profile, name='user_profile'),
    url(r'^updateprofile/(?P<id>\d+)', views.update_profile, name='updateprofile'),
    url(r'^like/(?P<image_id>\d+)$', views.like, name='like'),
    url(r'^unlike/(?P<image_id>\d+)$', views.unlike, name='unlike')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
