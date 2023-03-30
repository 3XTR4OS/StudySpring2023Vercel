# -*- coding: utf8 -*-
import scripts.TestQuestions
import scripts.temperament
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
import scripts
import re

# Create your views here.
def home(request):
    return render(request, "home.html")


def index(request):
    def my_view(request):
        my_data = "Hello, World!"
        return render(request, 'test_href.html', {'info': my_data})

    return render(request, 'test_href.html')


def input_from(request):
    return render(request, 'input_form.html')
    # return render(request, 'test_href.html')


def quest_input(request):
    user_answers = []
    for i, answer in request.POST.items():
        number = re.findall(r'[0-9]+', i)
        if not len(number):
            pass
        else:
            user_answers.append(answer)

    user_answers = [bool(True) if i == 'Да' else bool(False) for i in user_answers]
    extraversion_score, neuroticism_score, lie_score = scripts.temperament.check_answers(user_answers)
    temperament = scripts.temperament.temperament_calculate(extraversion_score, neuroticism_score, lie_score)

    temperament_discritpion = scripts.temperament.get_temperament_text(temperament[0], temperament[-1])
    colleges = scripts.temperament.select_colleges_under_temperament(temperament[0])
    return HttpResponse(f"<div>Ваш тип темперамента: {temperament_discritpion}</div>"
                        f"<div><h3>Ниже представлен список техникумов и профессий, которые вам подходят:<h3></div>"
                        f" <div>{colleges}</div>")
    # return render(request, 'test_href.html', {'info': colleges})
