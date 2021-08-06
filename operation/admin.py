from django.contrib import admin

from .models import Operation
from .models import ModePaiement
from .models import Devise
from .models import TypeOperation
from .models import TypeRessource
from .models import TypeJuridiction
from .models import Ville
from .models import Banque


# Register your models here.

admin.site.register(Operation)
admin.site.register(ModePaiement)
admin.site.register(Devise)
admin.site.register(TypeOperation)
admin.site.register(TypeRessource)
admin.site.register(TypeJuridiction)
admin.site.register(Ville)
admin.site.register(Banque)
