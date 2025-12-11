from django.db import models

class PredictionRecord(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    breast_probability = models.FloatField()
    breast_diagnosis = models.CharField(max_length=50)
    breast_class = models.IntegerField()

    liver_probability = models.FloatField()
    liver_diagnosis = models.CharField(max_length=50)
    liver_class = models.IntegerField()

    lung_probability = models.FloatField()
    lung_diagnosis = models.CharField(max_length=50)
    lung_class = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
