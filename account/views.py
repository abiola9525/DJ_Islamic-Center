from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone
from datetime import datetime
from hijri_converter import convert, Gregorian
from django.contrib.auth import login, authenticate
from blog.models import Post
from .forms import YouthSignupForm, AdultSignupForm, LoginForm


def home(request):
    current_datetime = timezone.now()
    war = datetime.strptime(str(current_datetime.date()), '%Y-%m-%d').date()
    hijri_date = convert.Gregorian.fromdate(war).to_hijri()
    recent_post = Post.objects.filter(status=1).order_by('-created_at')[:3]
    return render(request, 'home.html', {
        'current_datetime': current_datetime,
        'hijri_date': hijri_date,
        'recent_post': recent_post
        })

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


class YouthSignupView(View):
    def get(self, request):
        form = YouthSignupForm()
        return render(request, 'registration/youth_signup.html', {'form': form})

    def post(self, request):
        form = YouthSignupForm(request.POST)
        if form.is_valid():
            user = form.save_youth()
            login(request, user)
            return redirect('home')  # Redirect to the home page
        return render(request, 'registration/youth_signup.html', {'form': form})

class AdultSignupView(View):
    def get(self, request):
        form = AdultSignupForm()
        return render(request, 'registration/adult_signup.html', {'form': form})

    def post(self, request):
        form = AdultSignupForm(request.POST)
        if form.is_valid():
            user = form.save_adult()
            login(request, user)
            return redirect('home')  # Redirect to the home page
        return render(request, 'registration/adult_signup.html', {'form': form})

# class LoginView(View):
#     def get(self, request):
#         form = LoginForm()
#         return render(request, 'registration/login.html', {'form': form})

#     def post(self, request):
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, email=email, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('home')  # Redirect to the home page
#             else:
#                 form.add_error('username', 'Invalid username or password')
#         return render(request, 'login.html', {'form': form})
    
