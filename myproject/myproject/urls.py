from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.views import generic



urlpatterns = [
    url(r'^twitter/', include('twitter.urls')),
    url(r'^admin/', admin.site.urls),
]
