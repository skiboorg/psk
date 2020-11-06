from django.forms import ModelForm
from .models import *



class CallbackForm(ModelForm):
    class Meta:
        model = Callback
        fields = (
            'name',
            'phone',
            'email',
            # 'service',
            'message',
            # 'file'
        )
