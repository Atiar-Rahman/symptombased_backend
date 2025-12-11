from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from detection.serializers import CancerDetectionSerializer, PredictionRecordSerializer
from detection.prediction import predict_lung, predict_liver, predict_breast
from detection.ml_models.model_loader import breast_model, lung_model, liver_model
from detection.models import PredictionRecord
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class CancerDetectionAPI(APIView):
    def post(self, request):
        serializer = CancerDetectionSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data

            # breast
            breast_features = {
                "Age": data["age"],
                "Gender": data["gender"].upper(),
                "Protein1": data["protein1"],
                "Protein2": data["protein2"],
                "Protein3": data["protein3"],
                "Protein4": data["protein4"],
                "Tumour_Stage": data["tumour_stage"],
                "Histology": data["histology"],
                "ER status": data["er_status"],
                "PR status": data["pr_status"],
                "HER2 status": data["her2_status"],
            }

            breast_result = predict_breast(breast_model, breast_features)

            # liver
            liver_features = {
                "Age": data["age"],
                "Gender": 1 if data["gender"].upper() == "MALE" else 0,
                "Total_Bilirubin": data["total_bilirubin"],
                "Direct_Bilirubin": data["direct_bilirubin"],
                "Alkaline_Phosphotase": data["alkaline_phosphotase"],
                "Alamine_Aminotransferase": data["alamine_aminotransferase"],
                "Aspartate_Aminotransferase": data["aspartate_aminotransferase"],
                "Total_Protiens": data["total_protiens"],
                "Albumin": data["albumin"],
                "Albumin_and_Globulin_Ratio": data["albumin_and_globulin_ratio"],
            }

            liver_result = predict_liver(liver_model, liver_features)

            # lung
            lung_features = {
                "age": data["age"],
                "gender": data["gender"],
                "family_history": data["family_history"],
                "smoking_status": data["smoking_status"],
                "bmi": data["bmi"],
                "cholesterol_level": data["cholesterol_level"],
                "hypertension": data["hypertension"],
                "asthma": data["asthma"],
            }

            lung_result = predict_lung(lung_model, lung_features)

            # save prediction
            record = PredictionRecord.objects.create(
                age=data["age"],
                gender=data["gender"],

                breast_probability=breast_result["cancer_probability"],
                breast_diagnosis=breast_result["final_diagnosis"],
                breast_class=breast_result["prediction_class"],

                liver_probability=liver_result["cancer_probability"],
                liver_diagnosis=liver_result["final_diagnosis"],
                liver_class=liver_result["prediction_class"],

                lung_probability=lung_result["cancer_probability"],
                lung_diagnosis=lung_result["final_diagnosis"],
                lung_class=lung_result["prediction_class"],
            )

            return Response({
                "breast": breast_result,
                "liver": liver_result,
                "lung": lung_result,
                "record_id": record.id,
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PredictionRecordView(viewsets.ModelViewSet):
    queryset  = PredictionRecord.objects.all()
    serializer_class = PredictionRecordSerializer
    permission_classes=[IsAuthenticated]
