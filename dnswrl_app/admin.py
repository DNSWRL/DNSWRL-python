from django.contrib import admin

from .models import Symptoms, SymptomsList, Examine, ExamineList, Disease

class SymptomsListInline(admin.TabularInline):
    model = SymptomsList
    extra = 1

class SymptomsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('症状名称', {'fields':['symptoms_text']}),
        ('症状表现', {'fields':['characterization_text']}),
    ]

    inlines = [SymptomsListInline]
    list_filter = ['symptoms_text']
    search_fields = ['symptoms_text']
    list_display = ('symptoms_text', 'characterization_text')

class ExamineListInline(admin.TabularInline):
    model = ExamineList
    extra = 1

class ExamineAdmin(admin.ModelAdmin):
    fieldsets = [
        ('检查项', {'fields': ['examine_text']}),
        ('所属科室', {'fields': ['department_text']}),
    ]
    inlines = [ExamineListInline]
    list_filter = ['department_text']
    search_fields = ['examine_text']
    list_display = ('examine_text', 'department_text',)

class DiseaseAdmin(admin.ModelAdmin):
    fieldsets = [
        ('疾病名称', {'fields': ['disease_text']}),
        ('症状列表(用|分隔)', {'fields': ['symptoms_text']}),
        ('检查科室列表(用|分隔)', {'fields': ['examine_text']}),
        ('表征列表(用|分隔)', {'fields': ['manifestation_text']}),
        ('治疗建议', {'fields': ['treatment_text']}),

    ]
    list_filter = ['disease_text']
    search_fields = ['disease_text']
    list_display = ('disease_text', 'symptoms_text', 'examine_text', 'manifestation_text', 'treatment_text')


admin.site.register(Symptoms, SymptomsAdmin)
admin.site.register(Examine, ExamineAdmin)
admin.site.register(Disease, DiseaseAdmin)