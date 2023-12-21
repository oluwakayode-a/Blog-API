
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('blog.urls', 'blog'))),
    path('api/', include('rest_framework.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
