from django.db import models
from partenaire.models import Partenaire


# ---------- MODE DE PAIEMENT ---------------
class ModePaiement(models.Model):
    nom = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nom

# ---------- DEVISE ---------------
class Devise(models.Model):
    nom = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.nom

# ---------- TYPE OPERATION ---------------
class TypeOperation(models.Model):
    nom = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.nom

# ---------- TYPE RESSOURCES ---------------
class TypeRessource(models.Model):
    DUREE=(('3 mois', '3 mois'),
           ('6 mois','6 mois'),
           ('1 ans', '1 ans'))

    nom = models.CharField(max_length=50, null=True)
    duree = models.CharField(max_length=200, null=True, choices=DUREE)

    def __str__(self):
        return self.nom

# ---------- TYPE JURIDICTION ---------------
class TypeJuridiction(models.Model):
    nom = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nom

# ---------- VILLE ---------------
class Ville(models.Model):
    nom = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nom

# ---------- BANQUE ---------------
class Banque(models.Model):
    nom = models.CharField(max_length=50, null=True)
    Code_Banque = models.CharField(max_length=50, null=True)
    Code_Guichet = models.CharField(max_length=50, null=True)
    No_Compte_CDCB = models.CharField(max_length=50, null=True)
    RIB_CDCB = models.CharField(max_length=50, null=True)
    IBAN_CDCB = models.CharField(max_length=50, null=True)
    SWIFT = models.CharField(max_length=50, null=True)
    No_Compte_GSM = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nom




# ---------- OPERATION ---------------
class Operation(models.Model):
    STATUS = (('en instance', 'en instance'),
              ('non valide', 'non valide'),
              ('valide', 'valide'))
    Partenaire = models.ForeignKey(Partenaire, null=True, on_delete=models.SET_NULL)
    Ref_Operation = models.CharField(max_length=50)
    TypeOperation = models.ForeignKey(TypeOperation, null=True, on_delete=models.SET_NULL)             # Key
    Objet_Cons_depot = models.CharField(max_length=200, null=True)
    Affaire_Concernee = models.CharField(max_length=400, null=True)
    Ref_Decision = models.CharField(max_length=50, null=True)
    Devise = models.ForeignKey(Devise, null=True, on_delete=models.SET_NULL)                            # Key
    Mode_Paiement = models.ForeignKey(ModePaiement, null=True, on_delete=models.SET_NULL)               # Key
    Montant_Lettre = models.CharField(max_length=400, null=True)
    Montant_Chiffre = models.FloatField(default=0, null=True)
    Type_Ressource = models.ForeignKey(TypeRessource, null=True, on_delete=models.SET_NULL)             # Key
    Type_Juridiction = models.ForeignKey(TypeJuridiction, null=True, on_delete=models.SET_NULL)         # Key
    Reference_Reglement = models.CharField(max_length=50, null=True)
    Nom_Deposant = models.CharField(max_length=100, null=True)
    Date_Operation = models.DateTimeField(auto_now_add=True, null=True)
    Info_Reglement = models.CharField(max_length=400, null=True)
    Statut = models.CharField(max_length=50, null=True, choices=STATUS, default=STATUS[0])
    Date_Reception_Fonds = models.DateTimeField(auto_now_add=True, null=True)
    Banque = models.ForeignKey(Banque, null=True, on_delete=models.SET_NULL)                            # Key
    Ville = models.ForeignKey(Ville, null=True, on_delete=models.SET_NULL)                              # Key
    Nom_Consignataire = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.Ref_Operation

# Create your models here.


