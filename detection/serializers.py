from rest_framework import serializers
from detection.models import PredictionRecord

class CancerDetectionSerializer(serializers.Serializer):
    age = serializers.IntegerField()
    gender = serializers.CharField()

    # breast
    protein1 = serializers.FloatField()
    protein2 = serializers.FloatField()
    protein3 = serializers.FloatField()
    protein4 = serializers.FloatField()
    tumour_stage = serializers.CharField()
    histology = serializers.CharField()
    er_status = serializers.CharField()
    pr_status = serializers.CharField()
    her2_status = serializers.CharField()

    # liver
    total_bilirubin = serializers.FloatField()
    direct_bilirubin = serializers.FloatField()
    alkaline_phosphotase = serializers.FloatField()
    alamine_aminotransferase = serializers.FloatField()
    aspartate_aminotransferase = serializers.FloatField()
    total_protiens = serializers.FloatField()
    albumin = serializers.FloatField()
    albumin_and_globulin_ratio = serializers.FloatField()

    # lung
    family_history = serializers.CharField()
    smoking_status = serializers.CharField()
    bmi = serializers.FloatField()
    cholesterol_level = serializers.IntegerField()
    hypertension = serializers.IntegerField()
    asthma = serializers.IntegerField()

class PredictionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionRecord
        fields = "__all__"