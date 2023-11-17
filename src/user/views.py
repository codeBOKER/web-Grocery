from django.shortcuts import render

# login and registr app
def login_registr(request):
    # email = request.POST.get('email')
    # password = request.POST.get('password')
    # data = NewUser(email= email, password= password)
    # data.save()
    return render(request, 'Login And Registration.html')

def profile(request):
    return render(request, 'profile.html')

def shopping_cart(request):
    return render(request, 'Shopping Cart.html')

def wishlist(request):
    return render(request, 'Wishlist.html')

def contact_form_confirm(request):
    return render(request, 'Contact Form Confirm.html')

def contact_form(request):
   return render(request, 'Contact Form.html')

def details_for_checkout(request):
    return render(request, 'Details For Checkout.html')

# pyment app
def payment(request):
    return render(request, 'Payment.html')

def payment_confirmation(request):
    return render(request, 'Payment Confirmation.html')


# feedback app
def feedback_form_confirm(request):
    return render(request, 'Feedback Form Confirm.html')

def feedback_form(request):
    return render(request, 'Feedback Form.html')

# Create your views here.
