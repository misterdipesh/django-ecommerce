from django.shortcuts import render,redirect
from django.http import  HttpResponseNotFound
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Product,Purchase
from .form import AccountRegistrationForm
from datetime import date

def login_page(request):
    error_message=''
    if request.method=="GET":
        return render(request,"login.html",{})
    else:
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            error_message="Invalid Email or password !!!"
            return render(request,"login.html",{'error_message':error_message})
@login_required(login_url='/login/')
def home(request):
    search_value = request.GET.get('search')
    print(search_value)
    if request.method=='GET' and search_value==None:
        Items=Product.objects.all()
    else:
        Items=Product.objects.all().filter(product_name=search_value)
    context={'Items':Items,'user':request.user}
    return render(request,'index.html',context)
def register(request):
    user=request.user
    if not user.is_authenticated:
        form=AccountRegistrationForm()
        context={'form': form}
        if request.method=='POST':
            form=AccountRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        return render(request,"register.html",context)
    else:
        return redirect('home')
@login_required(login_url='/login/')
def buy(request,P_id):
    if request.method=="POST":
        product_id=request.POST.get('product_id')
        product_obj=Product.objects.get(id=product_id)
        user_obj=request.user
        Product_purchased=Purchase.objects.create(product_purchased=product_obj,purchased_by=user_obj,purchased_quantity=1,
                                                  purchased_on=date.today())
        Product_purchased.save()
        quantity=product_obj.product_quantiy
        if quantity >0:
            product_obj.product_quantiy=quantity-1
        else:
            product_obj.product_is_avaliable=False
        product_obj.save()
        return redirect('home')
    else:
        try:
            product=Product.objects.get(id=P_id)
            context = {
                "user": request.user,
                "product": product

            }
            return render(request, "addtocart.html", context)
        except:
            return HttpResponseNotFound("Oops something went wrong!!")
@login_required(login_url='/login/')
def buy_not_found(request):
    return HttpResponseNotFound("Oops something went wrong!!")
@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return redirect('login')
@login_required(login_url='/login/')
def about(request):
    return render(request,'about.html',{})
# @login_required(login_url='/login/')
# def search(request):
#     if request.method=='GET':
#         print('hello')
#         search_value=request.GET.get('search')
#         print(search_value)
#         Items=Product.objects.all().filter(product_name=search_value)
#         context:{
#             'Items':Items
#         }
#         return render(request,'index.html',context)




