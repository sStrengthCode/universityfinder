from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . forms import CreateUserForm
from . models import *
import random

# Create your views here.



# Function to handle the register page, usercreation and saving
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST) # Create a form with the data from the request, this is a an existing django form
        if form.is_valid(): # Check if the form is valid
            form.save() # Save the form
            user = form.cleaned_data.get('username') # Get the username from the form
            messages.success(request, 'Account was created for ' + user) # Display a success message
            return redirect('login') # Redirect to the login page
    return render(request, 'authenticate/register.html', {'form': form}) # Reload the register page if something goes wroing


# Function to handle the login page, user authentication and login
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username') # Get the username from the form
        password = request.POST.get('password') # Get the password from the form

        user = authenticate(request, username=username, password=password) # Authenticate the user, this is an existing django function

        if user is not None: # Meaning if the user exists and authenticated
            login(request, user) # Login the user, this is an existing django function

            return render(request, 'application/welcome.html', {'context': user}) # Redirect to the home page
        
        else: # Meaning if the user does not exist or the password is incorrect
            messages.info(request, 'Username or password is incorrect') # Display an error message

    return render(request, 'authenticate/login.html') # Reload the login page if something goes wrong
 

# Function to handle the logout functionality, user logout
def logoutUser(request): 
    logout(request) # Logout the user, this is an existing django function
    return redirect('login') # Redirect to the login page


@login_required(login_url='login') # This means the user must be logged in to access the home page
def subjects(request): # Function to handle the home page
    return render(request, 'application/subjects.html') # Render the home page



@login_required(login_url='login') # This means the user must be logged in to access the recommend university page
def recommend_university(request): # Function to handle the recommend university page

    eng = {'mathan'} # engineering requires mathan
    finance = {'eco'} # finance requires eco
    medicine = {'bio'} # medicine requires bio
    cs = {'cs', 'digital'} # computer science requires cs and digital
    history = {'history'} # history requires history
    geography = {'history', 'poli'} # geography requires history and political science
    biology = {'bio'} # biology requires bio
    linguistics = {'englisha', 'arabica'} # linguistics requires englisha and arabica
    psychology = {'psyc', 'poli'} # psychology requires psyc and political science
    interpretation = {'english', 'arabic', 'poli'} # interpretation requires english, arabic and political science
    digital_marketing = {'digital', 'psyc'} # digital marketing requires digital and psyc
    english = {'englisha'} # english requires englisha
    philosophy = {'poli', 'history'} # philosophy requires political science and history
    nursing = {'bio', 'chem'} # nursing requires bio and chem
    physics = {'mathan', 'phys'} # physics requires mathan and phys
    business = {'eco', 'business'} # business requires eco and business

    if request.method == "POST":
        global additional # define global variable means it can be accessed from another function which is "final" function
        additional = [] # define empty list, and futher will be used to store the additional prices
        subjects = [] # define empty list, and futher will be used to store the selected subjects

        if request.POST.get('science'): # if the user selected science
            subjects.extend([item for item in request.POST.getlist('science')]) # add the selected subjects to the list
        # the syntax of the above line is called list comprehension, it is a python syntax to add items to a list
        # [item for item in request.POST.getlist('science')] means for each item in the list of selected subjects, add it to the list of subjects
        # same logic for other subjects

        if request.POST.get('math'):
            subjects.extend([item for item in request.POST.getlist('math')])

        if request.POST.get('english'):
            subjects.extend([item for item in request.POST.getlist('english')])

        if request.POST.get('arabic'):
            subjects.extend([item for item in request.POST.getlist('arabic')])

        if request.POST.get('IS'):
            subjects.extend([item for item in request.POST.getlist('IS')])

        if request.POST.get('additional'):
            additional.extend(
                [item for item in request.POST.getlist('additional')])

    context = {} # this is where we will store the universities that match the selected subjects
    if eng.issubset(subjects):
        context['engineering'] = list(University.objects.filter(majors__name='Engineering').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))
        # Filter the universities that offer engineering and the country is the selected country
        # Same logic for other subjects

    if finance.issubset(subjects):
        context['finance'] = list(University.objects.filter(majors__name='Finance').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if medicine.issubset(subjects):
        context['medicine'] = list(University.objects.filter(majors__name='Medicine').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if cs.issubset(subjects):
        context['computer science'] = list(University.objects.filter(majors__name='Computer Science').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if history.issubset(subjects):
        context['history'] = list(University.objects.filter(majors__name='History').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if geography.issubset(subjects):
        context['geography'] = list(University.objects.filter(majors__name='Geography').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if biology.issubset(subjects):
        context['biology'] = list(University.objects.filter(majors__name='Biology').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if linguistics.issubset(subjects):
        context['linguistics'] = list(University.objects.filter(majors__name='Linguistics').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if psychology.issubset(subjects):
        context['psychology'] = list(University.objects.filter(majors__name='Psychology').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if interpretation.issubset(subjects):
        context['interpretation'] = list(University.objects.filter(majors__name='Interpretation').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if digital_marketing.issubset(subjects):
        context['digital marketing'] = list(University.objects.filter(majors__name='Digital Marketing').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if english.issubset(subjects):
        context['english'] = list(University.objects.filter(majors__name='English').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if philosophy.issubset(subjects):
        context['philosophy'] = list(University.objects.filter(majors__name='Philosophy').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if nursing.issubset(subjects):
        context['nursing'] = list(University.objects.filter(majors__name='Nursing').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if physics.issubset(subjects):
        context['physics'] = list(University.objects.filter(majors__name='Physics').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    if business.issubset(subjects):
        context['business'] = list(University.objects.filter(majors__name='Business').filter(
            country=request.POST.get('destination')).values_list('name', 'extraCost', 'website', flat=False))

    # define dummy additonal prices
    living = random.randint(5000, 10000) #living price, random number between 5000 and 10000
    transportation = random.randint(1000, 5000) #transportation price, random number between 1000 and 5000
    food = random.randint(2000, 5000) #food price, random number between 2000 and 5000
    fees = [living, transportation, food] # combine them all in a list
    additional = {additional[i]: fees[i] for i in range(len(additional))} # add the additional prices which we defined earlier to the list of additional prices
    additional['total'] = sum(additional.values()) # calculate the total of the additional prices

    return render(request, 'application/selection.html', {'universities': context}) # show the selection page with the universities that match the selected subjects (the list of university page)

@login_required(login_url='login')
def final(request): # Function to handle the final page (the page that shows the selected university and the total cost)
    if request.method == "POST":
        uni = request.POST.get('uni') # get the selected university from the list of universities page
    query = (list(University.objects.filter(name=uni).values_list(
        'extraCost', 'website', flat=False))) # get the website and dummy cost of the selected university
    cost = query[0][0] # sotre the dummy cost in a variable
    website = query[0][1] # store the website in a variable

    additional['uni'] = uni # add the selected university to the final page context
    additional['cost'] = cost + additional['total'] # calculate the total cost
    additional['website'] = website # add the website to the final page context
    return render(request, 'application/final.html', {'context': additional}) # show the final page with the selected university and the total cost
