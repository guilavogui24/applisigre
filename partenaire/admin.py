from django.contrib import admin

from .models import Partenaire
from .models import TypePartenaire
from .models import FormeJuridique
from .models import Categories
from .models import SousCategorie


class SousCategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'Categories')
    search_fields = ['nom']




# Register your models here.

admin.site.register(Partenaire)
admin.site.register(TypePartenaire)
admin.site.register(FormeJuridique)
admin.site.register(Categories)
admin.site.register(SousCategorie, SousCategorieAdmin)
