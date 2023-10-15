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
            return redirect('welcome')
        else:
            messages.info(request, 'Username or password is incorrect')
    return render(request, 'authenticate/login.html')


@login_required(login_url='login')
def welcome(request):
    return render(request, 'application/welcome.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    return render(request, 'application/home.html')


@login_required(login_url='login')
def recommend_university(request):

    eng = {'mathan'}
    finance = {'eco'}
    medicine = {'bio'}
    cs = {'cs', 'digital'}

    if request.method == "POST":
        print(request.POST)
        response = []
        for i in range(1, 56):
            if request.POST.get('c' + str(i)):
                response.append(request.POST.get('c' + str(i)))

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
    print(context)
    for major, universities in context.items():
        print(major)
        for university in universities:
            print(university[0], university[1], university[2])

    return render(request, 'application/selection.html', {'universities': context})


@login_required(login_url='login')
def selection(request):
    return render(request, 'application/selection.html')


@login_required(login_url='login')
def subjects(request):
    return render(request, 'application/subjects.html')
