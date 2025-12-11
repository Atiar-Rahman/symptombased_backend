from django.urls import path
from detection.views import CancerDetectionAPI

urlpatterns = [
    path("", CancerDetectionAPI.as_view()),
]
