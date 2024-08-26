from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import login  , authenticate, logout
from django.contrib import messages
from .forms import LoginForm , CustomerSignUpForm
from .models import *
from .forms import *
import uuid
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required


def user_register_view(request):

    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save to the database yet
            user.is_customer = True  # Set any additional attributes if needed
            user.is_staff = False  
            user.is_email_verified = False
            user.email_verification_token = str(uuid.uuid4())
            user.save()  # Save the user using the manager of your custom User model

            # making profile during registration
            profile = UserProfile.objects.create(
                user=user,
                name=user.name,
                username=user.username,
                email=user.email,
            )

            current_site = get_current_site(request)
            subject = 'Activate Your Account'
            activation_link = f'http://{current_site}/users/verify_email/{user.email_verification_token}/'
            message = f'click the link to activate your account:{activation_link}'
            email_from = settings.DEFAULT_FROM_EMAIL
            recipeient_list = [user.email]
            send_mail(subject, message, email_from, recipeient_list)

            messages.success(request, "Thank you for registering! Please check your email to verify your account before logging in.")

            return redirect('users:user_login_view')
        else:
            print("Form is not valid:", form.errors)
    else:
        form = CustomerSignUpForm()
    return render(request , "users/login.html", {'form':form})

def verify_email_view(request , token):
    try:
        user = User.objects.get(email_verification_token = token)
        if user:
           user.is_email_verified = True
           user.email_verification_token = None
           user.save()
           return redirect('users:user_login_view')
    except:
        return HttpResponse("Activation Link is Invalid")

def user_login_view(request):
    msg = None
    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Authenticate user
            user = authenticate(username=username, password=password)
            
            if user is not None and user.is_email_verified:
                login(request, user)
                return redirect('books:home_view')
            else:
                messages.success(request, 'Invalid Credentials')
            
        else:   
            print(form.errors)
    else:
        form = LoginForm()
    return render(request , 'users/login.html', {'form':form})

def user_logout_view(request):
    logout(request)
    return redirect('books:home_view')

def user_profile_detail_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    
    return render(request, 'users/profile.html', {'user_profile': user_profile})

@login_required
# Edit Detail view of Profile
def user_profile_edit_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES ,  instance=user_profile)
        if form.is_valid():
            user = form.save(commit=False)
            user_profile.user = request.user  # Ensure the user is set correctly
            user.save()
            user = request.user
            user.name = form.cleaned_data['name']
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.save()
            messages.success(request, 'Profile successfully updated.')
            return redirect('users:user_profile_detail_view')
        else:
            print("Form is not valid:", form.errors)
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'users/profile.html', {'form': form})

