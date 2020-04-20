from django.shortcuts import render
from .models import Symptoms, Disease, Examine
from dnswrl_app.jsgfParser import jsgfParser


def choice(request):
    inputText = request.POST['inputText']
    matching, tags = jsgfParser.findTags(inputText)
    disease_list = Disease.objects.all()
    possible_diseases_list = []
    possible_other_symptoms = ''
    need_to_check = ''
    if len(tags) > 0:
        for disease in disease_list:
            if tags[0] in disease.manifestation_text.split('|'):
                possible_diseases_list.append(disease.disease_text)
                if possible_other_symptoms is not '':
                    possible_other_symptoms += '|'+disease.symptoms_text
                else:
                    possible_other_symptoms += disease.symptoms_text
                if need_to_check is not '':
                    need_to_check += '|'+disease.examine_text
                else:
                    need_to_check += disease.examine_text

    possible_other_symptoms_list = possible_other_symptoms.split('|')
    symptoms_list_all = Symptoms.objects.all()
    symptoms_list = []
    for other_symptoms in possible_other_symptoms_list:
        for symptoms in symptoms_list_all:
            if other_symptoms == symptoms.characterization_text:
                if symptoms not in symptoms_list:
                    symptoms_list.append(symptoms)


    need_to_check_list = need_to_check.split('|')
    examines_list_all = Examine.objects.all()
    examines_list = []
    for to_check in need_to_check_list:
        for examines in examines_list_all:
            if to_check == examines.department_text:
                if examines not in examines_list:
                    examines_list.append(examines)

    context = {
        'symptoms_list': symptoms_list,
        'examines_list': examines_list,
        'possible_diseases_list': possible_diseases_list,
        'inputText': inputText,
    }
    return render(request, 'dnswrl/choice.html', context)
    # return HttpResponse(template.render(context, request))

def result(request):
    # inputText = request.POST['choice1'].split('/')[0]
    symptomsList = []
    symptoms_list = []
    examineList = []
    examine_list = []
    post = request.POST
    postList = post.lists()

    for pos in postList:
        if 'choice' in pos[0]: symptomsList.append(pos[1])
        if 'examine' in pos[0]: examineList.append(pos[1])
        # symptomsList.append(pos)

    characterization_text = ''
    symptomsList_all = Symptoms.objects.all()
    for symptom in symptomsList:
        symptom_text = symptom[0].split('/')[0]
        symptom_res = symptom[0].split('/')[1]
        symptoms_list.append(symptom_text+'\t\t'+symptom_res)
        if symptom_res == '是':
            for symptoms in symptomsList_all:
                if symptom_text == symptoms.symptoms_text:
                    if characterization_text != '':
                        characterization_text += '|' + symptoms.characterization_text
                    else:
                        characterization_text += symptoms.characterization_text

    department_text = ''
    examineList_all = Examine.objects.all()
    for examine in examineList:
        examine_text = examine[0].split('/')[0]
        examine_res = examine[0].split('/')[1]
        examine_list.append(examine_text+'\t\t'+examine_res)
        if examine_res != '正常' or symptom_res != '否':
            for examines in examineList_all:
                if examine_text == examines.examine_text:
                    if department_text != '':
                        department_text += '|' + examines.department_text
                    else:
                        department_text += examines.department_text

    diseaseList_all = Disease.objects.all()
    disease_posible_set = {}
    for disease in diseaseList_all:
        it = 0
        for every_characterization_text in characterization_text.split('|'):
            if every_characterization_text == disease.symptoms_text:
                it += 1
        for every_department_text in department_text.split('|'):
            if every_department_text == disease.examine_text:
                it += 1
        disease_posible_set[disease.disease_text] = it

    if len(disease_posible_set) != 0:
        disease_possible_list = sorted(disease_posible_set.items(), key=lambda disease_posible_set: disease_posible_set[1])
        most_possible_disease = disease_possible_list[-1][0]
    else:
        most_possible_disease = '你的疾病可能暂时不在我们的疾病库中哦~'

    diseaseList_all = Disease.objects.all()
    treatment_text = ''
    for disease in diseaseList_all:
        if most_possible_disease == disease.disease_text:
            treatment_text = disease.treatment_text


    inputText = post['possible_disease']

    # for i in range(1, len(post)):
    #     symptom = request.POST['choice'+str(i)].split('/')[1] + request.POST['choice'+str(i)].split('/')[2]
    #     symptomsList.append(symptom)

    context = {
        'inputText': inputText,
        'symptomsList': symptoms_list,
        'examineList': examine_list,
        'characterization_text': characterization_text,
        'department_text': department_text,
        'most_possible_disease': most_possible_disease,
        'treatment_text': treatment_text,
        'post': post,
        # 'get':get,
    }
    return render(request, 'dnswrl/result.html', context)

def inputText(request):
    return render(request, 'dnswrl/input.html')