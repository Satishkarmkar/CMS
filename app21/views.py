from django.shortcuts import render
from django.shortcuts import redirect
from app21.models import StudentModel
from app21.models import LoginModel
from django.contrib import messages
# Create your views here.
def showcommon(request):
    return render(request, "index.html")

def studentLogin(request):
    return render(request,"stu_login.html")

def logincheck(request):
    un = request.POST.get("uname")
    pwd = request.POST.get("passwd")
    ty = 'student'
    try:
        LoginModel.objects.get(uname=un, passwd= pwd, type = ty)
        return render(request, "stu_home.html",{"name":un})
    except LoginModel.DoesNotExist:
        messages.error(request,"Invalid User")
        return redirect('studentLogin')

def studentHome(request):
    # reading the data from hyper-link
    uname = request.GET.get("una")
    return render(request, "stu_home.html",{"name":uname})

def studentRegistration(request):
    return render(request, "stu_registration.html")

def registrationStudent(request):
    name = request.POST.get("name")
    age = request.POST.get("age")
    gender = request.POST.get("gender")
    contact = request.POST.get("contact")
    email = request.POST.get("email")
    un = request.POST.get("uname")
    passwd = request.POST.get("passwd")
    # print(name,age,gender,contact,email,uname,passwd)
    type = 'student'
    stinfo = StudentModel(name=name,age=age,gender=gender,contact=contact,email=email,uname=un,passwd=passwd)
    stinfo.save()

    stlogin = LoginModel(uname= un, passwd= passwd, type= type)
    stlogin.save()

    messages.success(request,"Thanks for registration")
    return redirect('stu_registration')
    
def studentProfile(request):
    # reading the data from hyper-link
    uname = request.GET.get("una")
    studata=StudentModel.objects.get(uname=uname)

    return render(request,"stu_profile.html",{"name":uname,"data":studata})

def updateStudent(request):
    uname = request.GET.get("una")
    studata= StudentModel.objects.get(uname=uname)
    return render(request, "stu_update.html",{"name":uname, "data":studata})

def updated_student(request):
    name = request.POST.get("name")
    age = request.POST.get("age")
    gender = request.POST.get("gender")
    contact = request.POST.get("contact")
    email = request.POST.get("email")
    un = request.POST.get("uname")

    studata=StudentModel.objects.filter(uname=un).update(name=name,age=age,gender=gender,contact=contact,email=email,uname=un)
    # return render(request,"stu_update.html",{"name":un,"data":studata})

    messages.success(request,"Your Data is updated")
    return render(request,"stu_update.html",{"name":un,"data":studata})

def stu_logout(request):
    return render(request, "index.html")
