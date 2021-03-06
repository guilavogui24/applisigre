# Generated by Django 3.2.5 on 2021-07-21 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormeJuridique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypePartenaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SousCategorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, null=True)),
                ('Categories', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='partenaire.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Partenaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Denomination_Partenaire', models.CharField(max_length=200)),
                ('IFU', models.IntegerField(max_length=50)),
                ('Num_Compte', models.IntegerField(max_length=15)),
                ('Nom_Prenom_Rprst_legal', models.CharField(max_length=100)),
                ('Adresse', models.CharField(max_length=50)),
                ('Ville', models.CharField(max_length=50)),
                ('Telephone_fixe', models.IntegerField(max_length=15)),
                ('Telephone_Mobile', models.IntegerField(max_length=15)),
                ('Email', models.EmailField(max_length=254)),
                ('No_Cpte_Bancaire', models.IntegerField(max_length=15)),
                ('IBAN', models.IntegerField(max_length=15)),
                ('BIC', models.IntegerField(max_length=15)),
                ('Observations', models.CharField(max_length=200)),
                ('Forme_Juridique', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='partenaire.formejuridique')),
                ('Sous_Categorie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='partenaire.souscategorie')),
                ('Type_Partenaire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='partenaire.typepartenaire')),
            ],
        ),
    ]
