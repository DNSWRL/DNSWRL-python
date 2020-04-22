from django.contrib import admin

from .models import Symptoms, SymptomsList, Examine, ExamineList, Disease

class SymptomsListInline(admin.TabularInline):
    model = SymptomsList
    extra = 0

class SymptomsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('症状名称', {'fields':['symptoms_text']}),
        ('症状标识', {'fields':['symptoms_log']}),
    ]

    inlines = [SymptomsListInline]
    list_filter = ['symptoms_text']
    search_fields = ['symptoms_text']
    list_display = ('symptoms_text', 'symptoms_log')

class ExamineListInline(admin.TabularInline):
    model = ExamineList
    extra = 0

class ExamineAdmin(admin.ModelAdmin):
    fieldsets = [
        ('检查项', {'fields': ['examine_text']}),
        ('标识', {'fields': ['examine_log']}),
        ('所属科室', {'fields': ['department_text']}),
    ]
    inlines = [ExamineListInline]
    list_filter = ['department_text']
    search_fields = ['examine_text']
    list_display = ('examine_text', 'examine_log', 'department_text',)

class DiseaseAdmin(admin.ModelAdmin):
    fieldsets = [
        ('疾病名称', {'fields': ['disease_text']}),
        ('症状列表(用|分隔)', {'fields': ['symptoms_log']}),
        ('检查科室列表(用|分隔)', {'fields': ['examine_log']}),
        ('表征列表(用|分隔)', {'fields': ['manifestation_text']}),
        ('治疗建议', {'fields': ['treatment_text']}),

    ]
    list_filter = ['disease_text']
    search_fields = ['disease_text']
    list_display = ('disease_text', 'symptoms_log', 'examine_log', 'manifestation_text', 'treatment_text')


admin.site.register(Symptoms, SymptomsAdmin)
admin.site.register(Examine, ExamineAdmin)
admin.site.register(Disease, DiseaseAdmin)