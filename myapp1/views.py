from django.shortcuts import render, redirect
from .models import LoginData,Contact
from django.contrib.auth.hashers import make_password, check_password

# def create_resume(request):
#     if request.method == 'POST':
#         resume_form = ResumeForm(request.POST)
#         if resume_form.is_valid():
#             resume = resume_form.save()
#             return redirect(request,'edit_resume.html', resume_id=resume.id)
#     else:
#         resume_form = ResumeForm() 
#     return render(request, 'create_resume.html', {'form': resume_form})

def create(request):
    return render(request, 'create_resume.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = LoginData.objects.filter(email=email).first()

        if user:
         
            if check_password(password, user.password):
                return redirect('myapp1:create_resume') 
            else:
                return render(request, 'login.html', {'error': 'Incorrect password. Please try again.'})
        else:
            
            return redirect('myapp1:signup')

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')  

        if LoginData.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email already exists'})

        hashed_password = make_password(password)  
        LoginData.objects.create(email=email, password=hashed_password)  
        return redirect('myapp1:login')

    return render(request, 'signup.html')


def base(request):
    return render(request, 'base.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        phone = request.POST.get('phone')
        feedback = request.POST.get('feedback')
        if feedback:
            Contact.objects.create(name=name, mail=mail, phone=phone, feedback=feedback)
        return redirect('myapp1:base')
    return render(request,'contact.html')