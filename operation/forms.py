from django.forms import ModelForm
from .models import Operation


class OperationForm(ModelForm):
    class Meta:
        model = Operation
        fields='__all__'