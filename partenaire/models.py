from django.db import models

# Create your models here.
from django.db import models



# Create your models here.

# ---------- TYPE PARTENAIRE ---------------
class TypePartenaire(models.Model):
    nom = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nom

# ---------- TYPE FORME JURIDIQUE ---------------
class FormeJuridique(models.Model):
    nom = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nom

# ---------- CATEGORIE ---------------
class Categories(models.Model):
    nom = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nom

# ---------- SOUS CATEGORIE ---------------
class SousCategorie(models.Model):
    nom = models.CharField(max_length=100, null=True)
    Categories = models.ForeignKey(Categories, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nom



# ---------- PARTENAIRE ---------------
class Partenaire(models.Model):
    Denomination_Partenaire = models.CharField(max_length=200)
    Sous_Categorie = models.ForeignKey(SousCategorie, null=True, on_delete=models.SET_NULL)             # Key
    Forme_Juridique = models.ForeignKey(FormeJuridique, null=True, on_delete=models.SET_NULL)           # Key
    Type_Partenaire = models.ForeignKey(TypePartenaire, null=True, on_delete=models.SET_NULL)           # Key
    IFU = models.IntegerField(max_length=50)
    Num_Compte = models.IntegerField(max_length=15)
    Nom_Prenom_Rprst_legal = models.CharField(max_length=100)
    Adresse = models.CharField(max_length=50)
    Ville = models.CharField(max_length=50)
    Telephone_fixe = models.IntegerField(max_length=15)
    Telephone_Mobile = models.IntegerField(max_length=15)
    Email = models.EmailField()
    No_Cpte_Bancaire = models.IntegerField(max_length=15)
    IBAN = models.IntegerField(max_length=15)
    BIC = models.IntegerField(max_length=15)
    Observations = models.CharField(max_length=200)

    def __str__(self):
        return self.Denomination_Partenaire