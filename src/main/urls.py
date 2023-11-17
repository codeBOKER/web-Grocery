from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),    
    path('Home/', views.home,
          name='Home'),
    path("About/", views.about,
         name='About Us'),
    
    path("category/<str:category_name>/", views.func_category,
         name='category-page'),

    path("BestDeals/", views.best_deals,
         name='Best Deals'),
 
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