from django.shortcuts import render, redirect
from .forms import DonationForm
from .models import Donation

# This view handles the donation form.
def donate_view(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Redirect to confirmation page
    else:
        form = DonationForm()
    
    return render(request, 'donations/donate.html', {'form': form})

# This view displays the Thank you message.
def thank_you_view(request):
    return render(request, 'donations/thank_you.html')

# This view displays the leaderboard
def leaderboard_view(request):
    donations = Donation.objects.order_by('-timestamp')  # Newest first
    return render(request, 'donations/leaderboard.html', {'donations': donations})
