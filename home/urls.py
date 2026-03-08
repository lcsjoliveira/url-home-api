from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('', include('url_home.urls')),

    path('admin/', admin.site.urls),

]
