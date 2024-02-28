from django.shortcuts import render,redirect
from .models import users
from django.http import HttpResponse

# Create your views here.



def index(request):
    return render(request,"index.html")

def userhome(request):
    return render(request,'userhome.html')

def adminhome(request):
    return render(request,'adminhome.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if users.objects.filter(name=name).exists():
            return render(request,'registration.html',{'message':'username already exists'})
        date = request.POST.get('date')
        gender = request.POST.get('gender')
        place = request.POST.get('place')
        email = request.POST.get('email')
        if users.objects.filter(email=email).exists():
            return render(request,'registartion.html',{'message':'email already exists'})
        phone = request.POST.get('phone')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            return render(request,'registration.html',{'message':'Password doesnot match'})
        else:
            data = users.objects.create(name=name,dob=date,gender=gender,place=place,email=email,phone=phone,password=password2,user_type="user")
            data.save()
            return redirect(login)
    else:
        return render(request,"registration.html")
    


def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        context = {'message': 'Invalid User Credentials'}

        if users.objects.filter(name=name, password=password).exists():
            user_detail = users.objects.get(name=name, password=password)
            if user_detail.user_type == 'user':
                if user_detail.status == 'accepted':
                    request.session['uid'] = user_detail.id
                    return redirect(userhome)
                else:
                    context = {'message': 'Your account is pending approval by the admin'}
                    return render(request, 'login.html', context)
            elif user_detail.user_type == 'admin':
                request.session['aid'] = user_detail.id
                return redirect(adminhome)
        else:
            context = {'message': 'Invalid User Credentials'}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')




def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
      del request.session[key]
    return redirect(index)




# admin.............................


def viewuser(request):
    data = users.objects.filter(user_type='user')
    return render(request,'adminviewuser.html',{'data':data})


def adminuseraccept(request,id):
    data = users.objects.get(id=id)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status == 'accepted':
            data.status = 'accepted'
        elif status == 'rejected':
            data.status = 'rejected'
        data.save()
        return redirect(viewuser)
    else:
        return redirect(viewuser)
    




# user....................................................
    

def userprofile(request):
    tem = request.session['uid']
    User = users.objects.get(id=tem)
    return render(request,'userprofile.html',{'data':User})



def updat(request,id):
    if 'uid' in request.session:
        data=users.objects.get(id=id)
        return render(request,'userprofileedit.html',{'data':data})
    


def updates(request,id):
    user =users.objects.get(id=id)
    if request.method=="POST":
        user.name=request.POST.get('name')
        user.dob=request.POST.get('date') 
        user.gender=request.POST.get('gender') 
        user.place=request.POST.get('place') 
        user.email = request.POST.get('email')
        user.phone=request.POST.get('phone')
        user.save()
        return redirect(userprofile)

def userchangepassword(request):
    tem = request.session['uid']
    user = users.objects.get(id=tem)
    if request.method=='POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        password3 = request.POST.get('password3')
        if user.password==password1:
            if password2==password3:
                user.password=password2
                user.save()
                return redirect(userhome)
            else:
                return render(request,'userchangepassword.html',{'message':'new password and confirm password not matching'})
        else:
            return render(request,'userchangepassword.html',{'message':'current password not matching'})
    else:
        return render(request,'userchangepassword.html')



def uservision(request):
    return render(request,'uservision.html')