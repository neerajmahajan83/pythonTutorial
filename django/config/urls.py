from django.contrib import admin
from django.urls import path, include  # <-- Make sure 'include' is imported here!
from .views import home

urlpatterns = [
    path("", home, name="home"),
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),  # <-- Note the comma at the end!
]


 