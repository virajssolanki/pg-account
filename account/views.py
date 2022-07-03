from django.contrib.auth import views    
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from account.forms import UploadFileForm


class ParseChatView(SuccessMessageMixin, generic.CreateView):
    '''
    create new user
    '''
    template_name = 'home.html'
    success_url = reverse_lazy('login')
    form_class = UploadFileForm
    success_message = "File parsed successfully"