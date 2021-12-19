from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls'), name="lettings"),
    path('profiles/', include('profiles.urls'), name="profiles"),
    # path('lettings/', lettings_views.index, name='lettings_index'),
    # path('lettings/<int:letting_id>/', lettings_views.letting, name='letting'),
    # path('profiles/', profiles_views.index, name='profiles_index'),
    # path('profiles/<str:username>/', profiles_views.profile, name='profile'),
    path('admin/', admin.site.urls),
]
