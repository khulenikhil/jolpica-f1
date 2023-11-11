"""URL configuration for formulastat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers

from . import views

criteria = [
    r"(circuits/(?P<circuit_ref>[a-zA-Z0-9_]+)/)",
    r"(constructors/(?P<team_ref>[a-zA-Z0-9_]+)/)",
    r"(drivers/(?P<driver_ref>[a-zA-Z0-9_]+)/)",
    r"(grid/(?P<grid_position>[a-zA-Z0-9_]+)/)",
    r"(results/(?P<race_position>[a-zA-Z0-9_]+)/)",
    r"(status/(?P<status_id>[a-zA-Z0-9_]+)/)",
]
regex_criteria = f"({'|'.join(criteria)})*"

router = routers.DefaultRouter()
router.register(f"{regex_criteria}/?seasons", views.SeasonViewSet, basename="season")

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]