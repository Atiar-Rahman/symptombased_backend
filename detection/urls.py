from django.urls import path, include
from rest_framework.routers import DefaultRouter
from detection.views import CancerDetectionAPI, PredictionRecordView

router = DefaultRouter()
router.register(r"results", PredictionRecordView, basename="prediction")

urlpatterns = [
    path("", CancerDetectionAPI.as_view(), name="cancer_detection"),
    path("", include(router.urls)),
]
