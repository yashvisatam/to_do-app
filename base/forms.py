from django.forms import ModelForm
from .models import Tasks

class AddForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['tasks']
class EditForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['tasks']        