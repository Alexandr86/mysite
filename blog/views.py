from models import Post, Person, Portfolio, Contacts
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer, ContactSerializer
from form import ContactForm


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Contacts.objects.all()
    serializer_class = ContactSerializer

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