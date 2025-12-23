from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactSubmission
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            submission = form.save(commit=False)
            if request.user.is_authenticated:
                submission.user = request.user
            submission.ip_address = request.META.get('REMOTE_ADDR')
            submission.user_agent = request.META.get('HTTP_USER_AGENT', '')
            submission.save()
            
            # Send email notification
            try:
                send_mail(
                    f'New Contact: {submission.subject}',
                    f'From: {submission.name} ({submission.email})\n\n{submission.message}',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
            except:
                pass  # Email might fail in development
            
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('contact:contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})
