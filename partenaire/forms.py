from django.forms import ModelForm
from .models import Partenaire


class PartenaireForm(ModelForm):
    class Meta:
        model = Partenaire
        fields='__all__'