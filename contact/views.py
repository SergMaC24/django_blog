from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.views import View

from .forms import ContactForm
from .models import ContactLinc, About


class ContactView(View):
    def get(self, request):
        contacts = ContactLinc.objects.all()
        form = ContactForm()
        return render(request, 'contact/contact.html', {'contacts': contacts, 'form': form})


class CreteContact(CreateView):
    form_class = ContactForm
    success_url = '/'


class AboutView(View):
    def get(self, request):
        about = About.objects.last()
        return render(request, 'contact/about.html', {'about': about})

