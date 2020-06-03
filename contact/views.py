from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            mail = request.POST.get('mail','')
            content = request.POST.get('content','')
    

    return render(request, "contact.html", {'form':contact_form})    

    email = EmailMessage('name', 'content', to=['luislopez121963@gmail.com'])
    email.send()
