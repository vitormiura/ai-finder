from django.shortcuts import render, redirect
from django.views.generic import View
from contacts.forms import ContactForm

def index(request):
    return render(request, 'contacts/index.html')

def about(request):
    return render(request, 'contacts/about.html')

class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, 'contacts/contact.html')

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('contact')
        return render(request, 'contacts/contact.html', {'form': form})
