from django.shortcuts import render

from .forms import SurveyForm


def index(request):
    survey_form = SurveyForm()
    return render(request, 'index.html', {'survey_form': survey_form})
