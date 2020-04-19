from django.contrib import admin

from .models import Symptoms, SymptomsList, Examine, ExamineList, Disease

class SymptomsListInline(admin.TabularInline):
    model = SymptomsList
    extra = 1

class SymptomsAdmin(admin.ModelAdmin):
    fields = [
        'symptoms_text',
        'characterization_text',
    ]
    inlines = [SymptomsListInline]
    list_filter = ['symptoms_text']
    search_fields = ['symptoms_text']
    list_display = ('symptoms_text', 'characterization_text')

class ExamineListInline(admin.TabularInline):
    model = ExamineList
    extra = 1

class ExamineAdmin(admin.ModelAdmin):
    fields = [
        'examine_text',
        'department_text',
    ]
    inlines = [ExamineListInline]
    list_filter = ['examine_text']
    search_fields = ['examine_text']
    list_display = ('examine_text', 'department_text',)

class DiseaseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['disease_text', 'symptoms_text', 'examine_text', 'manifestation_text', 'treatment_text']})
        # (None, {'fields': ['symptoms_key']})
        # (None, {'fields': ['examine_key']})
    ]
    list_filter = ['disease_text']
    search_fields = ['disease_text']
    list_display = ('disease_text', 'symptoms_text', 'examine_text', 'manifestation_text', 'treatment_text')


admin.site.register(Symptoms, SymptomsAdmin)
admin.site.register(Examine, ExamineAdmin)
admin.site.register(Disease, DiseaseAdmin)