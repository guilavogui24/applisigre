import django_filters
from .models import Operation

class OperationFiltre(django_filters.FilterSet):
    class Meta:
        model = Operation
        fields = ['Ref_Operation', 'TypeOperation']
