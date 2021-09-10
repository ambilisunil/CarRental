from django.shortcuts import render
from django.http import HttpResponse
import datetime
from datetime import date
from.models import adminLogin,user,feed,car,carRent
def adminlogin(request):
    return render(request,"adminlogin.html")
def l1(request):
    global userobj,loginobj
    if request.method=='POST':
        uname=request.POST.get('username')
        pwd=request.POST.get('password')
        if uname == "admin":
            if adminLogin.objects.filter(username=uname, password=pwd).exists():
                loginobj = adminLogin.objects.get(username=uname, password=pwd)
                return render(request, "index.html")
            else:
                return HttpResponse("LOgin errror")
        else:
            if adminLogin.objects.filter(username=uname,password=pwd).exists():
                loginobj = adminLogin.objects.get(username=uname, password=pwd)
                userobj = user.objects.get(loginid=loginobj)
                request.session['loginid'] = loginobj.id
                return render(request, "index2.html")
            else:
                return HttpResponse("LOgin errror")

def nv(request):
    return render(request,"h.html")
def register(request):
    if request.method=='POST':
        name=request.POST.get('Name')
        address=request.POST.get('address')

        uname=request.POST.get('username')
        pwd= request.POST.get('pwd')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        if adminLogin.objects.filter(username=uname).exists():

            return HttpResponse(" user name already exist")
        else:

            loginobj=adminLogin()
            loginobj.username=uname
            loginobj.password=pwd
            loginobj.save()

            userobj=user()
            userobj.loginid=loginobj
            userobj.name=name
            userobj.address=address

            userobj.email=email
            userobj.contact=contact
            if len(request.FILES)!=0:
              userobj.u_image=request.FILES['img']
              userobj.v_image = request.FILES['vimg']

            userobj.save()
            del userobj
            del loginobj

            return render(request,"adminlogin.html")

    return render(request,"userRegister.html")
def up(request):

    return render(request,"userdetails.html",{'user':userobj})
def update(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        address = request.POST.get('address')


        email = request.POST.get('email')
        contact = request.POST.get('contact')



        userobj.name = name
        userobj.address = address

        userobj.email = email
        userobj.contact = contact

        if len(request.FILES) != 0:
            userobj.u_image = request.FILES['img']
        userobj.save()

        return HttpResponse("updated sucessfully")
def logout(request):

    return render(request, "home.html")
    del loginobj
    del userobj
def changepswd(request):
    if request.method == 'POST':
        pwd = request.POST.get('pswd')
        pwd1 = request.POST.get('pswd1')

        pwd2 = request.POST.get('pswd2')
        if loginobj.password==pwd :
            if pwd1==pwd2:
                loginobj.password=pwd1
                loginobj.save()
                return HttpResponse(" Password updated sucessfully")
            else:
                return HttpResponse("Enter PASSWORD CORRECTLY")
        else:
            return HttpResponse("ENTER OLD PASSWORD CORRECTLY")

def ch(request):
    return render(request,"changepswd.html",{'user':loginobj})

def people(request):
    istekler = user.objects.all()
    return render(request, "list.html", {'m': istekler})
def serch(request):
    if request.method == 'POST':
        k = request.POST.get('serch1')
        istekler = user.objects.get(name=k)
        return render(request, "list2.html", {'m': istekler})
def feedbacks(request):
    if request.method=='POST':
        txt=request.POST.get('feed')


        feedobj=feed()
        feedobj.fid_id=userobj.id
        feedobj.feedback=txt
        feedobj.name=userobj.name


        feedobj.save()
        del feedobj


        return HttpResponse(" feedback sucessfully")

    return render(request,"feed.html")

def feeduser(request):

    h = feed.objects.filter(fid_id=userobj.id)
    return render(request, "usefeed.html", {'f': h})


def carRegister(request):
    if request.method=='POST':
        name=request.POST.get('Name')
        cmp=request.POST.get('company')

        price=request.POST.get('price')
        rent=request.POST.get('rent')
        fuel=request.POST.get('fuel')
        model=request.POST.get('model')


        carobj=car()
        carobj.name=name
        carobj.model=model
        carobj.company=cmp
        carobj.fuel=fuel
        carobj.rentPerDay=rent
        carobj.price=price
        if len(request.FILES)!=0:
            carobj.c_image=request.FILES['img']

        carobj.save()




        del carobj


        return render(request,"index.html")

    return render(request,"car\carRegister.html")
def discar(request):
    istekler = car.objects.all()
    return render(request, "car\discar.html", {'dc': istekler})
def adminfeed(request):
    ist = feed.objects.all()
    return render(request,"feedadmin.html", {'fa': ist})
def discarTo(request):
    istekler = car.objects.all()
    return render(request, "carRent\Rent.html", {'ca': istekler})
def rentcal(request):
    if request.method=='POST':
        global t
        id=request.POST.get('id')
        start=request.POST.get('start')

        end=request.POST.get('end')
        start_date = datetime.datetime.strptime(request.POST.get('start'), "%Y-%m-%d")
        end_date = datetime.datetime.strptime(request.POST.get('end'), "%Y-%m-%d")
        diff = abs((end_date - start_date).days)
        days= diff

        cr = car.objects.get(id=id)
        rentPerday=cr.rentPerDay
        amnt=rentPerday*days
        finalAmount=amnt


        rentobj=carRent()
        rentobj.uid=userobj
        rentobj.cid=cr
        rentobj.dateStart=start
        rentobj.dateEnd = end
        rentobj.dur = days
        rentobj.rentPerday=rentPerday
        rentobj.amnt=amnt
        rentobj.finalAmount=finalAmount


        rentobj.save()
        t=rentobj.id

    return render(request, "carRent\Rentdis.html", {'rnt': rentobj})
def returnin(request):

    return render(request, "index.html")
def returninu(request):

    return render(request, "index2.html")
def distrans(request):
    istekler = carRent.objects.all()
    return render(request, "carRent\disrentadmin.html", {'dct': istekler})
def returnind(request):

    return render(request, "index.html")
def distransuser(request):
    istekler = carRent.objects.filter(uid_id=userobj.id)
    return render(request, "carRent\disrentuser.html", {'dcu': istekler})
def returnuser(request):

    return render(request, "index2.html")

def adminapprove(request):
    istekler = carRent.objects.all()
    return render(request, "carRent\Adminaprove.html", {'acu': istekler})
def adminupdate(request):
    id = request.POST.get('id')
    dis = request.POST.get('dis')

    status = request.POST.get('status')





    rentobj = carRent.objects.get(id=id)
    s=rentobj.finalAmount
    rentobj.discount=dis
    rentobj.finalAmount = s-float(dis)

    rentobj.status= status

    rentobj.save()


    return render(request, "carRent\Adminaprovedis.html", {'rnt': rentobj})
    del rentobj

def rentdisa(request):

    return render(request, "index2.html")

def returnd(request):
    k = carRent.objects.filter(returened="NO")
    return render(request, "carRent\Return.html", {'rcu': k})
def returncar(request):
    id = request.POST.get('id')


    status = request.POST.get('rtstatus')


    rentobj = carRent.objects.get(id=id)


    rentobj.returened= status

    rentobj.save()


    return render(request, "index.html")
    del rentobj

def updatecar(request):
    upc= car.objects.all()
    return render(request, "car\carUpdate.html", {'uc': upc})


def updatecar1(request):
    ids = request.POST.get('id')

    upck = car.objects.get(id=ids)
    return render(request, "car\carupdated.html", {'upcr': upck})


def carUpdaTe(request):
    if request.method=='POST':
        ids = request.POST.get('idk')
        name=request.POST.get('Name')
        cmp=request.POST.get('company')

        price=request.POST.get('price')
        rent=request.POST.get('rent')
        fuel=request.POST.get('fuel')
        model=request.POST.get('model')


        carobj=car.objects.get(id=ids)
        carobj.name=name
        carobj.model=model
        carobj.company=cmp
        carobj.fuel=fuel
        carobj.rentPerDay=rent
        carobj.price=price
        if len(request.FILES)!=0:
            carobj.c_image=request.FILES['img']

        carobj.save()




        del carobj


        return render(request,"index.html")
def dltcar(request):
    upc= car.objects.all()
    return render(request, "car\dltcar.html", {'uc': upc})
def dltcar1(request):
    ids = request.POST.get('ids')
    if ids=="none":
        return HttpResponse(" enter correct")
    else:
        upck = car.objects.get(id=ids)
        upck.delete()
        return render(request, "index.html")


def adm(request):
    return render(request,"home.html")
def returnadm(request):

    return render(request, "index.html")

def abt(request):
    return render(request,"about.html")
def cnt(request):
    return render(request,"contact.html")
def hm(request):
    return render(request,"home.html")
# Create your views here.
