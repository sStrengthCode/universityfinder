from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UniversitySerializer
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . forms import CreateUserForm
from . models import *
import random

# Create your views here.


@api_view(['GET'])
def get_data(request):
    data = request.POST.get('data')
    print(data)


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'authenticate/register.html', {'form': form})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'application/welcome.html', {'context': user})
        else:
            messages.info(request, 'Username or password is incorrect')
    return render(request, 'authenticate/login.html')



def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    return render(request, 'application/home.html')


additional = []


@login_required(login_url='login')
def recommend_university(request):

    eng = {'mathan'}
    finance = {'eco'}
    medicine = {'bio'}
    cs = {'cs', 'digital'}
    history = {'history'}
    geography = {'history', 'poli'}
    biology = {'bio'}
    linguistics = {'englisha', 'arabica'}
    psychology = {'psyc', 'poli'}
    interpretation = {'english', 'arabic', 'poli'}
    digital_marketing = {'digital', 'psyc'}
    english = {'englisha'}
    philosophy = {'poli', 'history'}
    nursing = {'bio', 'chem'}
    physics = {'mathan', 'phys'}
    business = {'eco', 'business'}

    if request.method == "POST":
        print(request.POST)
        global additional
        additional = []
        response = []
        if request.POST.get('science'):
            response.extend([item for item in request.POST.getlist('science')])

        if request.POST.get('math'):
            response.extend([item for item in request.POST.getlist('math')])

        if request.POST.get('english'):
            response.extend([item for item in request.POST.getlist('english')])

        if request.POST.get('arabic'):
            response.extend([item for item in request.POST.getlist('arabic')])

        if request.POST.get('IS'):
            response.extend([item for item in request.POST.getlist('IS')])

        if request.POST.get('additional'):
            additional.extend(
                [item for item in request.POST.getlist('additional')])

    context = {}
    if eng.issubset(response):
        context['engineering'] = list(University.objects.filter(majors__name='Engineering').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if finance.issubset(response):
        context['finance'] = list(University.objects.filter(majors__name='Finance').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if medicine.issubset(response):
        context['medicine'] = list(University.objects.filter(majors__name='Medicine').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if cs.issubset(response):
        context['computer science'] = list(University.objects.filter(majors__name='Computer Science').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if history.issubset(response):
        context['history'] = list(University.objects.filter(majors__name='History').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if geography.issubset(response):
        context['geography'] = list(University.objects.filter(majors__name='Geography').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if biology.issubset(response):
        context['biology'] = list(University.objects.filter(majors__name='Biology').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if linguistics.issubset(response):
        context['linguistics'] = list(University.objects.filter(majors__name='Linguistics').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if psychology.issubset(response):
        context['psychology'] = list(University.objects.filter(majors__name='Psychology').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if interpretation.issubset(response):
        context['interpretation'] = list(University.objects.filter(majors__name='Interpretation').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if digital_marketing.issubset(response):
        context['digital marketing'] = list(University.objects.filter(majors__name='Digital Marketing').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if english.issubset(response):
        context['english'] = list(University.objects.filter(majors__name='English').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if philosophy.issubset(response):
        context['philosophy'] = list(University.objects.filter(majors__name='Philosophy').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if nursing.issubset(response):
        context['nursing'] = list(University.objects.filter(majors__name='Nursing').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if physics.issubset(response):
        context['physics'] = list(University.objects.filter(majors__name='Physics').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if business.issubset(response):
        context['business'] = list(University.objects.filter(majors__name='Business').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    # define dummy additonal prices
    living = random.randint(5000, 10000)
    transportation = random.randint(1000, 5000)
    food = random.randint(2000, 5000)
    fees = [living, transportation, food]
    additional = {additional[i]: fees[i] for i in range(len(additional))}
    additional['total'] = sum(additional.values())

    return render(request, 'application/selection.html', {'universities': context})


@login_required(login_url='login')
def selection(request):
    return render(request, 'application/selection.html')


@login_required(login_url='login')
def subjects(request):
    return render(request, 'application/subjects.html')


@login_required(login_url='login')
def final(request):
    if request.method == "POST":
        uni = request.POST.get('uni')
    query = (list(University.objects.filter(name=uni).values_list(
        'extraCost', 'website', flat=False)))
    cost = query[0][0]
    website = query[0][1]
    print(cost, website)

    additional['uni'] = uni
    additional['cost'] = cost + additional['total']
    additional['website'] = website
    return render(request, 'application/final.html', {'context': additional})
