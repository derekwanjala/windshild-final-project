from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.core.mail import send_mail

from .models import About, Contact, Portfolio, Service

def home(request):
    services = Service.objects.all()
    portfolio = Portfolio.objects.order_by('created')[:9]
    about = About.objects.all()
    return render(request, 'index.html', {'services': services, 'portfolio': portfolio, 'about': about})


def about(request):
    about = About.objects.all()
    services = Service.objects.all()
    return render(request, 'about.html', {'about': about, 'services': services})


def service(request):
    services = Service.objects.all()
    about = About.objects.all()
    return render(request, 'service.html', {'services': services, 'about': about})


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    about = About.objects.all()
    return render(request, 'service_detail.html', {'service': service, 'about': about})


def portfolio(request):
    portfolio = Portfolio.objects.all()
    services = Service.objects.all()
    about = About.objects.all()
    return render(request, 'portfolio.html', {'portfolio': portfolio, 'services': services, 'about': about})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(name=name, email=email, phone=phone,
                          subject=subject, message=message)

        contact.save()

        send_mail(
            subject,  # title
            message,  # message
            email,
            ['codeworldcreatives@gmail.com'],
            fail_silently=False)

        messages.success(
            request, 'Your Message has been received, we will get back soon!')
    services = Service.objects.all
    about = About.objects.all()
    return render(request, 'contact.html', {'services': services, 'about': about})

