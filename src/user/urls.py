from django.urls import path
from . import views

urlpatterns = [
    path("DetailsForCheckout/", views.details_for_checkout,
         name='Details For Checkout'),
    
    path("LoginRegistr/", views.login_registr,
         name='Login And Registr'),

    path("Payment/", views.payment,
         name='Payment'),

    path("Profile/", views.payment,
         name='Profile'),

    path("ShoppingCart/", views.shopping_cart,
         name='Shopping Cart'),

    path("Wishlist/", views.wishlist,
         name='Wishlist'),

    path("ContactFormConfirm/", views.contact_form_confirm,
         name='Contact Form Confirm'),

    path("FeedbackFormConfirm/", views.feedback_form_confirm,
         name='Feedback Form Confirm'),

    path("FeedbackForm/", views.feedback_form,
         name='Feedback Form'),

    path("PaymentConfirmation/", views.payment_confirmation,
         name='Payment Confirmation'),
]