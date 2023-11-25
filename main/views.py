import datetime
import json
from django.http import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)
    context = {
        'products': products,
        'name': request.user.username,
        'last_login': request.COOKIES.get('last_login', 'No last login information available'),

        }

    return render(request, "main.html", context)

def preview_product(request):
    products = Product.objects.filter(user=request.user)
    context = {
        'products': products,
        'name': request.user.username,
        'last_login': request.COOKIES.get('last_login', 'No last login information available'),

        }

    return render(request, "preview_product.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)
    products = Product.objects.filter(user=request.user)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.current_stock = product.amount
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {
        'products': products,
        'form': form,
        'name': request.user.username,
        'last_login': request.COOKIES.get('last_login', 'No last login information available'),
}
    return render(request, "create_product.html", context)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('main:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')

        else:
            messages.info(request, 'Password not matching..')
            return redirect('main:register')
    else:
        return render(request, 'register.html')
        
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:login')


def dropdown_user(request):
    products = Product.objects.filter(user=request.user)
    context = {
        'products': products,
        'name': request.user.username,
        'last_login': request.COOKIES.get('last_login', 'No last login information available'),

        }

    return render(request, "dropdown_user.html", context)


from django.shortcuts import get_object_or_404

def delete_product(request, product_id):
    # Get the product by its ID or return a 404 if not found
    product = get_object_or_404(Product, pk=product_id)

    # Check if the user has permission to delete the product
    if request.user == product.user:
        # Delete the product
        product.delete()
        # Redirect to the main page or any other appropriate page
        return HttpResponseRedirect(reverse('main:show_main'))
    else:
        # Return a response indicating the user doesn't have permission
        return HttpResponse("You do not have permission to delete this product.")


from django.shortcuts import get_object_or_404, redirect
from main.models import Product

def increment_amount(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    # Check if the user has permission to update the product
    if request.user == product.user:
        product.amount += 1
        product.date = (datetime.datetime.now())
        product.save()
    
    return redirect('main:show_main')

def decrement_amount(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    # Check if the user has permission to update the product
    if request.user == product.user and product.amount > 1:
        product.amount -= 1
        product.date = (datetime.datetime.now())
        product.save()
    
    elif product.amount<=1:
        product.delete()

    return redirect('main:show_main')

def edit_product(request, id):
    # Get product berdasarkan ID
    product = Product.objects.get(pk = id)
    products = Product.objects.filter(user=request.user)

    # Set product sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {
        'products': products,
        'form': form,
        'name': request.user.username,
        'last_login': request.COOKIES.get('last_login', 'No last login information available'),

        }
    return render(request, "edit_product.html", context)

def get_product_json(request):
    product_item = Product.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_product = Product(name=name, price=price, amount=amount, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Product.objects.create(
            user = request.user,
            name = data["name"],
            price =int(data["price"]),
            amount = int(data["amount"]),
            description = data["description"],
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)