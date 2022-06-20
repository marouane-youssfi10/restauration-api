from django.contrib import admin
from django.urls import path
from django.conf import settings

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls)
]


admin.site.site_header = "Restaurant API Admin"
admin.site.index_title = "Welcome to the Restaurant Haven API Portal"