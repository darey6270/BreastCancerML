from django import forms


class PredictForm(forms.Form):
    radius_mean = forms.FloatField()
    texture_mean = forms.FloatField()
    perimeter_mean = forms.FloatField()
    area_mean = forms.FloatField()
    smoothness_mean = forms.FloatField()
    compactness_mean = forms.FloatField()
    concavity_mean = forms.FloatField()
    concave_points_mean = forms.FloatField()
    symmetry_mean = forms.FloatField()
    radius_se = forms.FloatField()
    perimeter_se = forms.FloatField()
    area_se = forms.FloatField()
    compactness_se = forms.FloatField()
    concavity_se = forms.FloatField()
    fractal_dimension_se = forms.FloatField()
    radius_worst = forms.FloatField()
    texture_worst = forms.FloatField()
    perimeter_worst = forms.FloatField()
    area_worst = forms.FloatField()
    smoothness_worst = forms.FloatField()
    compactness_worst = forms.FloatField()
    concavity_worst = forms.FloatField()
    concave_points_worst=forms.FloatField()
    symmetry_worst = forms.FloatField()
    fractal_dimension_worst = forms.FloatField()


