from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Candidate, Interview,OFFERS_DETAILS,VACANCIES,UserProfile
from .forms import InterviewForm,HiringForm,CandidateForm,vacancyform# Adjust the import statement based on your project structure

def loginpage(request):

    return render(request,'login.html')

def logout(request):

    return render(request,'logout.html')


def registerhere(request):

    return render(request,'register.html')

def reset(request):

    return render(request,'reset.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        workmail = request.POST['workmail']
        password = request.POST['password']

        # Check if the username is unique before creating the user
        if User.objects.filter(username=username).exists():
            # Handle the case where the username is not unique
            # You might want to redirect back to the registration form with an error message
            return render(request, 'register.html', {'error': 'Username is not available'})

        # Create a new user
        user = User.objects.create_user(username=username, email=workmail, password=password)

        # Create a corresponding user profile
        user_profile = UserProfile.objects.create(user=user, bio='Some default bio',username=username, usermail=workmail, password=password)

        # Redirect to a success page or home page
        return redirect('login')

    return render(request, 'register.html')

def loginuser(request):
    if request.method == 'POST':
        email = request.POST['workmail']
        password = request.POST['password']

        # Check if the email is verified
        try:
            user_profile = UserProfile.objects.get(usermail=email)
        except UserProfile.DoesNotExist:
            messages.error(request, 'Email not verified or user does not exist.')
            return redirect('login')

        # Authenticate user
        user = authenticate(request, username=user_profile.user.username, password=password)

        if user is not None:
            # Login successful
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')
        else:
            # Invalid credentials
            messages.error(request, 'Invalid email or password.')
            return redirect('loginpage')

    return render(request, 'login.html')




def board(request):
    pro = Candidate.objects.all()
    order = Interview.objects.all()

    total_applicants = pro.count()

    offers_made =Interview.objects.filter(interview_status='Selected').count()
    print(offers_made)
    offer_accepted =OFFERS_DETAILS.objects.all()

    offer_accepted_count=OFFERS_DETAILS.objects.filter(offers='OFFER ACCEPTED').count()

    offer_rejected =OFFERS_DETAILS.objects.filter(offers='OFFER REJECTED').count()
    
    return render(request, 'base.html',context={'pro':pro,'order':order,'total_applicants':total_applicants,'offers_made':offers_made,'offer_accepted':offer_accepted,'offer_accepted_count':offer_accepted_count,'offer_rejected':offer_rejected})


def Job_openings(request):

    value= VACANCIES.objects.all()

    return render(request,template_name='vacancies.html',context={'value':value})

def Total_applicants(request):

    val = Candidate.objects.all()

    return render(request,template_name='Applicants.html',context={'val':val})

def schedule_interviews(request, pk=None):
    if pk:
        # Update existing interview
        interview_instance = get_object_or_404(Interview, id=pk)
        form = InterviewForm(request.POST or None, instance=interview_instance)
    else:
        # Schedule a new interview
        form = InterviewForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'interview.html', {'form': form})


def delete_interview(request,pk):

    orders=Interview.objects.get(id=pk)

    if request.method=='POST':
        orders.delete()
        return redirect('home')

    return render(request,'delete.html',context={'name':orders})

def Hire(request, pk=None):
    if pk:
        # It's an update operation, retrieve the existing record
        hiring_instance = get_object_or_404(OFFERS_DETAILS, id=pk)
        form = HiringForm(request.POST or None, instance=hiring_instance)
    else:
        # It's a new hire
        form = HiringForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'Hire.html', context={"form": form})

def delete_hire(request,pk):

    ans=OFFERS_DETAILS.objects.get(id=pk)

    if request.method=='POST': 
        ans.delete()
        return redirect('home')

    return render(request,'deletehire.html',context={'name':ans})

def addcandidate(request, pk=None):
    if pk:
        # It's an update operation, retrieve the existing record
        add_instance = get_object_or_404(Candidate, id=pk)
        form = CandidateForm(request.POST or None, request.FILES or None, instance=add_instance)
    else:
        # It's a new hire
        form = CandidateForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('Total_applicants')
        else:
            print(form.errors)
            print(form.cleaned_data)

    return render(request, 'candidate.html', context={'form': form})

def vacant(request, pk=None):
    if pk:
        # It's an update operation, retrieve the existing record
        add_instance = get_object_or_404(VACANCIES, id=pk)
        form = vacancyform(request.POST or None, request.FILES or None, instance=add_instance)
    else:
        # It's a new hire
        form = vacancyform(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.info(request,'Updated sucessfully')
            return redirect('opening')
        else:
            print(form.errors)
            print(form.cleaned_data)

    return render(request, 'vacancy.html', context={'form': form})

def deletecandidate(request,pk):

    val1=Candidate.objects.get(id=pk)

    if request.method=='POST': 
        val1.delete()
        return redirect('Total_applicants')

    return render(request,'deletecandi.html',context={'name':val1})
    