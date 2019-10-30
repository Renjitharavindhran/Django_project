from django.shortcuts import render, get_object_or_404, HttpResponse, redirect, reverse
from django.contrib.auth import authenticate, login, get_user
from django.contrib.auth import logout
from django.contrib.auth.models import User
from datetime import datetime
from .models import Textile
from .models import Cart, Buynow, Coupon
from .forms import TextileForm
# from .forms import CartForm
from django.contrib import messages


def index(request):
    obj1 = Textile.objects.all()
    return render(request, 'index.html', {'ob': obj1})


def get_user(user):
    a = User.objects.filter(username=user)
    return a[4]


def oneitem(request, id):
    ob = get_object_or_404(Textile, id=id)

    if request.method == 'POST':
        user = request.user
        quantity = request.POST['quantity']
        # totalprice = (ob.price + Cart.quantity)
        # print(totalprice)
        totalprice = request.POST['totalprice']
        size = request.POST['size']
        cart = Cart.objects.create(title_id=ob.id, user_id=user.id, quantity=quantity, totalprice=totalprice,
                                   date=datetime.now(), size=size)
        cart.save()
        obj = Cart.objects.filter(user_id=user.id)
        return render(request, 'carts.html', {'ob': obj})
    return render(request, 'oneob.html', {'ob': ob})


def delete(request, id):
    d = Textile.objects.get(id=id)
    d.delete()
    return redirect('index')


def add(request):
    form = TextileForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TextileForm()
    contex = {'form': form}
    return render(request, 'form.html', contex)


def log(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['passwd']
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return HttpResponse('invalid login')


def logout_view(request):
    logout(request)
    return render(request, 'index.html')


def registration(request):
    if request.method == 'POST':
        uname = request.POST['create_username']
        psw = request.POST['create_password']
        cnfrmpsw = request.POST['cnfrm_pswd']
        eid = request.POST['email_create']
        # print(uname)
        if psw == cnfrmpsw:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'Username already exist..!')
            elif User.objects.filter(email=eid).exists():
                messages.info(request, 'Email already exist..!')
            else:
                user = User.objects.create_user(username=uname, password=psw, email=eid)
                user.save()
                return redirect('index')
        else:
            messages.info(request, 'Incorrect Password')
            return redirect('registration')
    return render(request, 'registration.html')


def reg(request):
    if request.method == 'POST':
        uname = request.POST['create_username']
        psw = request.POST['create_password']
        cnfrmpsw = request.POST['cnfrm_pswd']
        eid = request.POST['email_create']
        # print(uname)
        if psw == cnfrmpsw:
            if User.objects.filter(username=uname).exists():
                return HttpResponse('Username already exist..!')
            elif User.objects.filter(email=eid).exists():
                return HttpResponse('Email already exist..!')
            else:
                user = User.objects.create_user(username=uname, password=psw, email=eid)
                user.save()
                return redirect('index')
        else:
            return HttpResponse('Incorrect Password')
    return render(request, 'registration.html')


def search(request):
    if request.method == 'GET':
        prdname = request.GET['search']
        print(prdname)
        # if Textile.objects.filter(title=prdname):
        #     ob = Textile.objects.filter(title=prdname)
        #     return render(request, 'search.html', {'ob': ob})
        status = Textile.objects.filter(title__icontains=prdname)
        if status:
            return render(request, 'search.html', {'ob': status})
        else:
            messages.info(request, 'not available')
            return redirect('index')
    return redirect('index')


def searchitem(request, id):
    ob = get_object_or_404(Textile, id=id)
    return render(request, 'searchitem.html', {'ob': ob})


def blog(request):
    return render(request, 'blog.html')


def shop(request):
    return render(request, 'shop.html')


# def addtocart(request,id):
#     item = get_object_or_404(Textile, id=id)
#     form = CartForm(request.POST or None,request.FILES or None)
#     if form.is_valid():
#          # instance = form.save(commit=False)
#          # instance.user = request.user
#          # instance.save()
#          # form.instance.Author = Author.objects.get(author=request.user.username)
#          form.instance.author = get_user(request.user)
#          form.instance.item = item
#          # quantity=request.POST.get('quantity', '')
#          # obj=Cart(quantity=quantity)
#          # print(obj)
#          # obj.save()
#          form.save()
#     form = CartForm()
#     contex = {'form': form}
#     return render(request, 'oneob.html',contex)


def carts(request):
    ob = request.user
    obj = Cart.objects.filter(user_id=ob.id)
    return render(request, 'carts.html', {'ob': obj})


def buynow(request, id):
    ob = request.user
    obj = Cart.objects.filter(title_id=id,user_id=ob.id)
    print(obj)

    obj1 = Cart.objects.filter(user_id=ob.id)
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        state = request.POST['state']
        street = request.POST['street']
        apartment = request.POST['apartment']
        town = request.POST['town']
        postcode = request.POST['postcode']
        phone = request.POST['phone']
        buynow = Buynow.objects.create(firstname=firstname, lastname=lastname, state=state, town=town,
                                       streetaddress=street,
                                       appartment=apartment, phone=phone, postcode=postcode, email=email, user_id=ob.id,
                                       title_id=id)
        buynow.save()
        c = request.POST['couponcode']
        co = Coupon.objects.get(code=c)
        if c:
            if Coupon.objects.filter(code=c).exists():

                return render(request, 'buynow.html', {'ob': obj,'co':co})

                # return HttpResponse('valid coupon')
            else:
                return HttpResponse('invalid coupon')
        else:
            return HttpResponse('no coupon code')
        # d = get_object_or_404(Cart, id=id)
        # d.delete()
        # ob = request.user
        # obj = Cart.objects.filter(user_id=ob.id)
        return render(request, 'buynow.html', {'ob': obj1})

    return render(request, 'buynow.html', {'ob': obj})


def removecart(request, id):
    d = get_object_or_404(Cart, id=id)
    d.delete()
    ob = request.user
    obj = Cart.objects.filter(user_id=ob.id)
    return render(request, 'carts.html', {'ob': obj})
#
#
# def coupon(request):
#     obc = get_object_or_404(Cart, id=id)
#     ob = get_object_or_404(Coupon, id=id)
#     if request.method == 'POST':
#         c = request.POST['coupon']
#         if Coupon.objects.filter(code=c).exists():
#             # return HttpResponse('valid coupon')
#             return render(request, 'coupon.html', {'ob': ob, 'obc': obc})
#         else:
#             return HttpResponse('Invalid coupon')
