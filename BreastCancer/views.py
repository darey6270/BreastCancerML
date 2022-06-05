from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
# import tensorflow as tf
import joblib
from sklearn.preprocessing import LabelEncoder
from .forms import PredictForm
import numpy as np
from django.contrib import messages


class AboutWebsite(TemplateView):
    template_name = "BreastCancer/about.html"


class ContactWebsite(TemplateView):
    template_name = "BreastCancer/contact.html"


class PredictWebsite(TemplateView):
    template_name = "BreastCancer/result.html"


class ServiceWebsite(TemplateView):
    template_name = "BreastCancer/service.html"


class HomeWebsite(TemplateView):
    template_name = "BreastCancer/index.html"


def ServiceWebsiteView(request):
    prediction_text = ''
    predictForm = PredictForm()
    if request.method == "POST":
        form = PredictForm(request.POST)
        if form.is_valid():
            radius_mean = form.cleaned_data['radius_mean']
            texture_mean = form.cleaned_data['texture_mean']
            perimeter_mean = form.cleaned_data['perimeter_mean']
            area_mean = form.cleaned_data['area_mean']
            smoothness_mean = form.cleaned_data['smoothness_mean']
            compactness_mean = form.cleaned_data['compactness_mean']
            concavity_mean = form.cleaned_data['concavity_mean']
            concave_points_mean = form.cleaned_data['concave_points_mean']
            symmetry_mean = form.cleaned_data['symmetry_mean']
            radius_se = form.cleaned_data['radius_se']
            perimeter_se = form.cleaned_data['perimeter_se']
            area_se = form.cleaned_data['area_se']
            compactness_se = form.cleaned_data['compactness_se']
            concavity_se = form.cleaned_data['concavity_se']
            fractal_dimension_se = form.cleaned_data['fractal_dimension_se']
            radius_worst = form.cleaned_data['radius_worst']
            texture_worst = form.cleaned_data['texture_worst']
            perimeter_worst = form.cleaned_data['perimeter_worst']
            area_worst = form.cleaned_data['area_worst']
            smoothness_worst = form.cleaned_data['smoothness_worst']
            compactness_worst = form.cleaned_data['compactness_worst']
            concavity_worst = form.cleaned_data['concavity_worst']
            concave_points_worst = form.cleaned_data['concave_points_worst']
            symmetry_worst = form.cleaned_data['symmetry_worst']
            fractal_dimension_worst = form.cleaned_data['fractal_dimension_worst']
            model = joblib.load(open('BreastCancer/BreastCancer.pkl', 'rb'))
            pred_test = np.array(
                [radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean,
                 concavity_mean, concave_points_mean,
                 symmetry_mean, radius_se, perimeter_se, area_se, compactness_se, concavity_se, fractal_dimension_se,
                 radius_worst, texture_worst,
                 perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst,
                 concave_points_worst, symmetry_worst, fractal_dimension_worst,0,0,0,0])
            result = model.predict(pred_test.reshape(1, -1))
            if result[0] == 1:
                prediction_text = "Breast Cancer detected"
            else:
                prediction_text = "Breast Cancer not detected "

            return render(request, "BreastCancer/result.html",
                          {"prediction_text": prediction_text})
        else:
            print(form.errors)
    else:
        predictForm = PredictForm()
    return render(request, "BreastCancer/service.html",
                  {"predictForm": predictForm})
