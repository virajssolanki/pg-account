from django import forms

from account.models import ChatFile


class UploadFileForm(forms.ModelForm):
    '''
    upload text file
    '''
    class Meta:
        model = ChatFile
        fields = ['chat_file']