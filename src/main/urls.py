from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),    
    path('home/', views.home,
          name='home'),
    path("about/", views.about,
         name='about_us'),
    
    path("category/<str:category_name>/", views.func_category,
         name='category-page'),
 
]

    # path("ContactForm/", views.contact_form,
    #      name='Contact Form'),
    # path("DetailsForCheckout/", views.DetailsForCheckout,
    #      name='Details For Checkout'),
    
    # path("LoginRegistr/", views.LoginRegistr,
    #      name='Login And Registr'),
    # path("Payment/", views.Payment,
    #      name='Payment'),
    # path("Profile/", views.Profile,
    #      name='Profile'),
    # path("ShoppingCart/", views.ShoppingCart,
    #      name='ShoppingCart'),
    # path("Wishlist/", views.Wishlist,
    #      name='Wishlist'),
    # path("ContactFormConfirm/", views.ContactFormConfirm,
    #      name='ContactFormConfirm'),
    # path("FeedbackFormConfirm/", views.FeedbackFormConfirm,
    #      name='FeedbackFormConfirm'),
    # path("FeedbackForm/", views.FeedbackForm,
    #      name='FeedbackForm'),
    # path("PaymentConfirmation/", views.PaymentConfirmation,
    #      name='PaymentConfirmation'),