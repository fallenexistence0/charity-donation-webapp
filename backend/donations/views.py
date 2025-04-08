from django.shortcuts import render, redirect
from .forms import DonationForm
from .models import Donation



def donate_view(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # go to a thank-you page
    else:
        form = DonationForm()
    
    return render(request, 'donations/donate.html', {'form': form})

def thank_you_view(request):
    return render(request, 'donations/thank_you.html')



def leaderboard_view(request):
    donations = Donation.objects.order_by('-timestamp')  # newest first
    return render(request, 'donations/leaderboard.html', {'donations': donations})
