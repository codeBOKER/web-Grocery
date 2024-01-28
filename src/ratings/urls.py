from django.urls import path
from ratings.views import rate_website, feedback_confirmation

urlpatterns = [
    path('feedback/', rate_website, name='feedback_website'),
    path('feedback_confirmation/',feedback_confirmation, name='feedback_confirmation'),
]