from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from TPO_App.forms import UserLoginModelForm, UserRegistrationModelForm, UserInfoModelForm
from TPO_App.models import UserInfoModel
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.
@login_required()
def UserLogoutView(request):
    logout(request)
    return render(request,"TPO_App/logout.html")

def UserLoginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active():
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse("CREDENTIALS ARE INCORRECT")
    else:
        return render(request,'TPO_App/UserLogin.html')

def UserRegistrationView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if password == confirm_password:
            user = User.objects.create(username=username, email=email, password=password)
            user.set_password(user.password)
            user.save()
            user_info = UserInfoModel.objects.create(user=user)
            user_info.save()

            login(request, user)

            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse("INVALID CREDENTIALS!")
    else:
        return render(request,'TPO_App/UserRegistration.html')


@login_required()
def UserInfoView(request,username):
    profile_user = User.objects.get(username=username)  # The user whose profile is to be viewed can be the current user or any other user.
    info = UserInfoModel.objects.get(user=profile_user)
    var_dict = {"profile_user": profile_user, "info": info}
    return render(request, "TPO_App/profile.html", context=var_dict)


@login_required()
def UserEditInfoView(request,username):
    user = User.objects.get(username=username)
    info = UserInfoModel.objects.get(user=user)
    if request.method == "POST":
        name = str(request.POST.get("name"))
        if " " in name:
            user.first_name,user.last_name = name.split(" ")
        else:
            user.first_name = name
            user.last_name = ""
        user.email = request.POST.get("email")
        info.roll_no = request.POST.get("roll_no")
        info.passing_year = request.POST.get("passing_year")
        info.branch = request.POST.get("branch")
        info.course = request.POST.get("course")
        info.college = request.POST.get("college")
        info.gender = request.POST.get("gender")
        info.dob = request.POST.get("dob")
        info.father_name = request.POST.get("father_name")
        info.mother_name = request.POST.get("mother_name")
        info.father_number = request.POST.get("father_number")
        info.mother_number = request.POST.get("mother_number")
        info.phone_number = request.POST.get("phone_number")
        info.address = request.POST.get("address")
        info.city = request.POST.get("city")
        info.pincode = request.POST.get("pincode")
        info.state = request.POST.get("state")
        info.alternate_gmail = request.POST.get("alternate_gmail")
        user.save()
        info.save()
        return HttpResponseRedirect(reverse("user:profile", kwargs={"username":username}))
    else:
        var_dict = {"user":user, "info":info}
        return render(request, "TPO_App/edit_info.html", context = var_dict)

def HomeView(request):
    return render(request,'TPO_App/home.html')


