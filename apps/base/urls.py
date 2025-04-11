# django
from django.urls import path
# third
# own
from apps.base.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
]