from django.shortcuts import redirect,render
from  django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from cancer_detection.models import contactForm

import pandas as pd
from pandas import Series,DataFrame
import numpy as np


cancer_data = pd.read_excel("../cancer/cancer_dectection.xlsx")
pridiction_data = cancer_data.head(10)

# Create your views here.

@login_required
def radius_vs_texture(request):
    radius_mean = pridiction_data['radius_mean'].tolist()
    texture_mean = pridiction_data['texture_mean'].tolist()
    data = {
        'radius_mean':radius_mean,
        'texture_mean':texture_mean,
    }
    return render(request,'cancer_detection/radius_vs_texture.html',context = data)


def registration(request):
    return render(request,'cancer_detection/registration.html')

def user_registration(request):
    first_name = request.GET.get('first_name', None)
    last_name = request.GET.get('last_name', None)
    email = request.GET.get('email', None)
    password = request.GET.get('password', None)

    try:
        user = User.objects.create_user(username=email,
                                    email=email,
                                    password=password,
                                    first_name = first_name,
                                    last_name = last_name)
        data = {
            'message':1
        }
    except:
        data = {
            'message':0
            }
    return JsonResponse(data)


@login_required
def perimeter_vs_area(request):
    # print('***********************************8')
    perimeter_mean = pridiction_data['perimeter_mean'].tolist()
    area_mean = pridiction_data['area_mean'].tolist()
    data = {
        'perimeter_mean':perimeter_mean,
        'area_mean':area_mean,
    }
    return render(request,'cancer_detection/perimeter_vs_area.html',context = data)


@login_required
def smoothness_vs_compactness(request):
    smoothness_mean = pridiction_data['smoothness_mean'].tolist()
    compactness_mean = pridiction_data['compactness_mean'].tolist()
    data = {
        'smoothness_mean':smoothness_mean,
        'compactness_mean':compactness_mean,
    }
    return render(request,'cancer_detection/smoothness_vs_compactness.html',context=data)


@login_required
def concavity_vs_concavepoints(request):
    concavity_mean = pridiction_data['concavity_mean'].tolist()
    concave_points_mean = pridiction_data['concave points_mean'].tolist()
    data = {
        'concavity_mean':concavity_mean,
        'concave_points_mean':concave_points_mean,
    }
    return render(request,'cancer_detection/concavity_vs_concavepoints.html',context=data)


@login_required
def symmetry_vs_fractaldimension(request):
    symmetry_mean = pridiction_data['symmetry_mean'].tolist()
    fractal_dimension_mean = pridiction_data['fractal_dimension_mean'].tolist()
    data = {
        'symmetry_mean':symmetry_mean,
        'fractal_dimension_mean':fractal_dimension_mean,
    }
    return render(request,'cancer_detection/symmetry_vs_fractaldimension.html',context=data)


@login_required
def radius_se_vs_texture_se(request):
    radius_se = pridiction_data['radius_se'].tolist()
    texture_se = pridiction_data['texture_se'].tolist()
    data = {
        'radius_se':radius_se,
        'texture_se':texture_se,
    }
    return render(request,'cancer_detection/radius_se_vs_texture_se.html',context=data)



@login_required
def perimeter_se_vs_area_se(request):
    perimeter_se = pridiction_data['perimeter_se'].tolist()
    area_se = pridiction_data['area_se'].tolist()
    data = {
        'perimeter_se':perimeter_se,
        'area_se':area_se,
    }
    return render(request,'cancer_detection/perimeter_se_vs_area_se.html',context=data)


@login_required
def smoothness_se_vs_compactness_se(request):
    smoothness_se = pridiction_data['smoothness_se'].tolist()
    compactness_se = pridiction_data['compactness_se'].tolist()
    data = {
        'smoothness_se':smoothness_se,
        'compactness_se':compactness_se,
    }
    return render(request,'cancer_detection/smoothness_se_vs_compactness_se.html',context=data)


@login_required
def concavity_se_vs_concavepoints_se(request):
    concavity_se = pridiction_data['concavity_se'].tolist()
    concave_points_se = pridiction_data['concave points_se'].tolist()
    data = {
        'concavity_se':concavity_se,
        'concave_points_se':concave_points_se,
    }
    return render(request,'cancer_detection/concavity_se_vs_concavepoints_se.html',context=data)


@login_required
def symmetry_se_vs_radius_worst(request):
    symmetry_se = pridiction_data['symmetry_se'].tolist()
    fractal_dimension_se = pridiction_data['fractal_dimension_se'].tolist()
    data = {
        'symmetry_se':symmetry_se,
        'fractal_dimension_se':fractal_dimension_se,
    }
    return render(request,'cancer_detection/symmetry_se_vs_fractal_dimension_se.html',context=data)

@login_required
def contact_form(request):
    if request.method == "POST":
        name_data = request.POST['name']
        email_data = request.POST['email']
        mobile_data = request.POST['mob_number']
        message_data = request.POST['message']
        contactForm_data = contactForm(name =name_data,email=email_data,mobile_no=mobile_data,message=message_data)
        contactForm_data.save()
        return redirect('../contact_form')
    return render(request,'cancer_detection/contact_form.html')
