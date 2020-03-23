from django.contrib import admin
from django.urls import path, include

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('api.urls')),
    path('google/', views.GoogleView.as_view(), name='google')
]
