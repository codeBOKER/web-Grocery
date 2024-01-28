from django.shortcuts import render, redirect
from .models import Rating
from django.contrib.auth.decorators import login_required

@login_required(login_url='login_registr')
def rate_website(request):
    if request.method == 'POST':
        rating = request.POST.get('rating1')
        user = request.user

        # Check if the user has already submitted a rating
        if Rating.objects.filter(user=user).exists():
            # Delete the last rating for the user
            last_rating = Rating.objects.filter(user=user).latest('id')
            last_rating.delete()

        # Create the new rating
        Rating.objects.create(user=user, rating=rating)
        return redirect('feedback_confirmation')  # Redirect to a confirmation page
    return render(request, 'feedback_website.html')

def feedback_confirmation(request):
    return render(request, 'feedback_confirmation.html')
