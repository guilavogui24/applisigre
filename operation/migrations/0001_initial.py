# Generated by Django 3.2.5 on 2021-07-21 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partenaire', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, null=True)),
                ('Code_Banque', models.CharField(max_length=50, null=True)),
                ('Code_Guichet', models.CharField(max_length=50, null=True)),
                ('No_Compte_CDCB', models.CharField(max_length=50, null=True)),
                ('RIB_CDCB', models.CharField(max_length=50, null=True)),
                ('IBAN_CDCB', models.CharField(max_length=50, null=True)),
                ('SWIFT', models.CharField(max_length=50, null=True)),
                ('No_Compte_GSM', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Devise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModePaiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeJuridiction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeRessource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, null=True)),
                ('duree', models.CharField(choices=[('3 mois', '3 mois'), ('6 mois', '6 mois'), ('1 ans', '1 ans')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ref_Operation', models.CharField(max_length=50)),
                ('Objet_Cons_depot', models.CharField(max_length=200, null=True)),
                ('Affaire_Concernee', models.CharField(max_length=400, null=True)),
                ('Ref_Decision', models.CharField(max_length=50, null=True)),
                ('Montant_Lettre', models.CharField(max_length=400, null=True)),
                ('Montant_Chiffre', models.FloatField(default=0, null=True)),
                ('Reference_Reglement', models.CharField(max_length=50, null=True)),
                ('Nom_Deposant', models.CharField(max_length=100, null=True)),
                ('Date_Operation', models.DateTimeField(auto_now_add=True, null=True)),
                ('Info_Reglement', models.CharField(max_length=400, null=True)),
                ('Statut', models.BooleanField(default=False, null=True)),
                ('Date_Reception_Fonds', models.DateTimeField(auto_now_add=True, null=True)),
                ('Nom_Consignataire', models.CharField(max_length=100, null=True)),
                ('Banque', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='operation.banque')),
                ('Devise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='operation.devise')),
                ('Mode_Paiement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='operation.modepaiement')),
                ('Partenaire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='partenaire.partenaire')),
                ('TypeOperation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='operation.typeoperation')),
                ('Type_Juridiction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='operation.typejuridiction')),
                ('Type_Ressource', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='operation.typeressource')),
                ('Ville', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='operation.ville')),
            ],
        ),
    ]
