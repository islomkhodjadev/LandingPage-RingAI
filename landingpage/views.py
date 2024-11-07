from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

from django_ratelimit.decorators import ratelimit


@ratelimit(key="ip", rate="5/m", method="POST", block=True)
def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect("home")
        else:
            messages.error(
                request, "There was an error sending your message. Please try again."
            )
    else:
        form = ContactForm()

    return render(request, "index.html", {"form": form})
