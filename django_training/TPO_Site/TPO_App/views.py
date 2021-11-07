from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from TPO_App.forms import UserLoginModelForm, UserRegistrationModelForm, UserInfoModelForm
from TPO_App.models import UserInfoModel, UserMarksModel, DocumentsModel, TrainingInfoModel
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
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
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
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request,"TPO_App/edit_info.html")

@login_required()
def UserMarksView(request,username):
    temp_user = User.objects.get(username=username)
    user = UserInfoModel.objects.get(user = temp_user)
    if request.method=="POST":
        name = str(request.POST.get("name"))
        if " " in name:
            user.first_name, user.last_name = name.split(" ")
        else:
            user.first_name = name
            user.last_name = ""
        tenth_obt_marks = request.POST.get("tenth_obt_marks")
        tenth_total_marks = request.POST.get("tenth_total_marks")
        tenth_percentage = request.POST.get("tenth_percentage")
        twelve_obt_marks = request.POST.get("twelve_obt_marks")
        twelve_total_marks = request.POST.get("twelve_total_marks")
        twelve_percentage = request.POST.get("twelve_percentage")
        jee_rank = request.POST.get("jee_rank")
        first_sem_marks = request.POST.get("first_sem_marks")
        second_sem_marks = request.POST.get("second_sem_marks")
        third_sem_marks = request.POST.get("third_sem_marks")
        fourth_sem_marks = request.POST.get("fourth_sem_marks")
        fifth_sem_marks = request.POST.get("fifth_sem_marks")
        sixth_sem_marks = request.POST.get("sixth_sem_marks")
        seventh_sem_marks = request.POST.get("seventh_sem_marks")
        supplees = request.POST.get("supplees")
        aggregates = request.POST.get("aggregates")
        agg = UserMarksModel.objects.create(user = user, tenth_obt_marks=tenth_obt_marks, tenth_total_marks=tenth_total_marks, tenth_percentage=tenth_percentage, twelve_obt_marks = twelve_obt_marks, twelve_total_marks=twelve_total_marks, twelve_percentage=twelve_percentage, jee_rank=jee_rank, first_sem_marks=first_sem_marks, second_sem_marks=second_sem_marks, third_sem_marks=third_sem_marks, fourth_sem_marks=fourth_sem_marks, fifth_sem_marks=fifth_sem_marks, sixth_sem_marks=sixth_sem_marks, seventh_sem_marks=seventh_sem_marks, aggregates=aggregates,supplees=supplees)
        agg.save()
        user.save()
        return HttpResponseRedirect(reverse('home'))
    else:
        return render(request,"TPO_App/marks_details.html")


@login_required()
def TrainingDetailsView(request,username):
    user = User.objects.get(username=username)
    info = UserInfoModel.objects.get(user = user)
    if request.method == "POST":
        technology = request.POST.get("technology")
        project = request.POST.get("project")
        training_mode = request.POST.get("training_mode")
        institute_name = request.POST.get("institute_name")
        institute_address = request.POST.get("institute_address")
        institute_number = request.POST.get("institute_number")
        training_duration = request.POST.get("training_duration")
        train_detail = TrainingInfoModel.objects.create(user = info, technology=technology, project =project , training_mode=training_mode, institute_name=institute_name,institute_address=institute_address, institute_number=institute_number,training_duration=training_duration)
        train_detail.save()
        user.save()
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request,"TPO_App/training_details.html")


@login_required()
def DocumentsView(request,username):
    user = User.objects.get(username=username)
    info = UserInfoModel.objects.get(user = user)
    if request.method=="POST":
        if "tenth_dmc" in request.FILES:
            tenth_dmc = request.FILES.get("tenth_dmc")
        if "twelvth_dmc" in request.FILES:
            twelvth_dmc = request.FILES.get("twelvth_dmc")
        if "first_sem_dmc" in request.FILES:
            first_sem_dmc = request.FILES.get("first_sem_dmc")
        if "second_sem_dmc" in request.FILES:
            second_sem_dmc = request.FILES.get("second_sem_dmc")
        if "third_sem_dmc" in request.FILES:
            third_sem_dmc = request.FILES.get("third_sem_dmc")
        if "fourth_sem_dmc" in request.FILES:
            fourth_sem_dmc = request.FILES.get("fourth_sem_dmc")
        if "fifth_sem_dmc" in request.FILES:
            fifth_sem_dmc = request.FILES.get("fifth_sem_dmc")
        if "sixth_sem_dmc" in request.FILES:
            sixth_sem_dmc = request.FILES.get("sixth_sem_dmc")
        if "seventh_sem_dmc" in request.FILES:
            seventh_sem_dmc = request.FILES.get("seventh_sem_dmc")
        docs = DocumentsModel.objects.create(user = info, tenth_dmc=tenth_dmc, twelvth_dmc = twelvth_dmc, first_sem_dmc=first_sem_dmc, second_sem_dmc=second_sem_dmc, third_sem_dmc =third_sem_dmc,fourth_sem_dmc=fourth_sem_dmc, fifth_sem_dmc=fifth_sem_dmc, sixth_sem_dmc=sixth_sem_dmc ,seventh_sem_dmc=seventh_sem_dmc)
        docs.save()
        user.save()
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request,"TPO_App/documents_detail.html")

def PlacementView(request):
    return render(request,"TPO_App/placement.html")


def HomeView(request):
    return render(request,'TPO_App/home.html')


