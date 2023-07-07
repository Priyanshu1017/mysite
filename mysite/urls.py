

from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "Login to Developer's Blog"
admin.site.site_title = "Welcome to Developer's Blog"
admin.site.index_title = "Welcome to Developer's Blog"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]