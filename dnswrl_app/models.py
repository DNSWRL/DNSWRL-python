from django.db import models
from django.utils import timezone
import datetime

class Symptoms(models.Model):
    symptoms_text = models.CharField(max_length=500)
    symptoms_log = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.symptoms_text


class SymptomsList(models.Model):
    symptomsList = models.ForeignKey(Symptoms, on_delete=models.CASCADE)
    symptomsList_text = models.CharField(max_length=50)
    symptomsList_log = models.CharField(max_length=10, default=0)
    def __str__(self):
        return self.symptomsList_text


class Examine(models.Model):
    examine_text = models.CharField(max_length=500)
    examine_log = models.CharField(max_length=500, default='')
    department_text = models.CharField(max_length=500, default='')
    def __str__(self):
        return self.examine_text


class ExamineList(models.Model):
    examineList = models.ForeignKey(Examine, on_delete=models.CASCADE)
    examineList_text = models.CharField(max_length=50)
    examineList_log = models.CharField(max_length=10, default=0)
    def __str__(self):
        return self.examineList_text


class Disease(models.Model):
    disease_text = models.CharField(max_length=500)
    symptoms_log = models.CharField(max_length=200, default='')
    examine_log = models.CharField(max_length=200, default='', blank=True)
    manifestation_text = models.CharField(max_length=200, default='')
    treatment_text = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.disease_text
