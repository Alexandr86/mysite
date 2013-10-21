from models import Post, Person, Portfolio, Contacts
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
from form import ContactForm


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PersonListView(ListView):
    model = Person


class PortfolioListView(ListView):
    model = Portfolio


class ContactsCreateView(CreateView):
    model = Contacts
    template_name = 'blog/templates/blog/contacts_form.html'
    form_class = ContactForm
    success_url = '/contacts/'
    # def get_success_url(self):
    #     c = {}
    #     c['msg'] = "Message has been sended. Thank you"
    #     return reverse('contacts', kwargs={'pk':self.kwargs['pk']})
    #     #
        # def get_context_data(self, **kwargs):
        #     context = super(ContactsCreateView, self).get_context_data(**kwargs)
        #     context['person'] = Person.objects.get(pk=1)
        #     return context