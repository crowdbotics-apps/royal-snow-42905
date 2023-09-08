# Generated by Django 2.2.28 on 2023-09-08 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_consumeroffer_importedfile_loanaccount_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessOwnerData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.TextField()),
                ('lastName', models.TextField()),
                ('phone', models.TextField()),
                ('percentOwned', models.IntegerField()),
                ('jobTitle', models.TextField()),
                ('address', models.TextField()),
                ('zipCode', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MembershipPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('monthlyPrice', models.FloatField()),
                ('anualPrice', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='loanaccount',
            name='payments',
            field=models.ManyToManyField(blank=True, null=True, related_name='loanaccount_payments', to='home.Payment'),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('lastPaymentDate', models.DateField()),
                ('nextPaymentDate', models.DateField()),
                ('plan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='subscription_plan', to='home.MembershipPlan')),
            ],
        ),
        migrations.CreateModel(
            name='CreditorBusinessData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('businessType', models.IntegerField()),
                ('businessName', models.TextField()),
                ('legalBusinessName', models.TextField()),
                ('companyEmail', models.EmailField(max_length=254)),
                ('taxIdNumber', models.TextField()),
                ('phone', models.TextField()),
                ('companyWebsite', models.URLField()),
                ('address1', models.TextField()),
                ('address2', models.TextField()),
                ('zipCode', models.TextField(blank=True, null=True)),
                ('country', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creditorbusinessdata_country', to='home.Country')),
                ('ownerData', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creditorbusinessdata_ownerData', to='home.BusinessOwnerData')),
                ('state', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creditorbusinessdata_state', to='home.State')),
            ],
        ),
        migrations.AddField(
            model_name='businessownerdata',
            name='city',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='businessownerdata_city', to='home.City'),
        ),
        migrations.AddField(
            model_name='businessownerdata',
            name='country',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='businessownerdata_country', to='home.Country'),
        ),
        migrations.AddField(
            model_name='businessownerdata',
            name='state',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='businessownerdata_state', to='home.State'),
        ),
        migrations.CreateModel(
            name='BillingDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOnCheck', models.TextField()),
                ('routingNumber', models.TextField()),
                ('accountNumer', models.TextField()),
                ('achFormat', models.TextField()),
                ('accountType', models.IntegerField()),
                ('zip', models.TextField()),
                ('cardNumber', models.TextField()),
                ('cardHoldername', models.TextField()),
                ('billAddrFirstname', models.TextField()),
                ('billAddrLastname', models.TextField()),
                ('billAddr', models.TextField()),
                ('billAddrZipCode', models.TextField()),
                ('billAddrCity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='billingdetails_billAddrCity', to='home.City')),
                ('billAddrCountry', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='billingdetails_billAddrCountry', to='home.Country')),
                ('billAddrState', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='billingdetails_billAddrState', to='home.State')),
                ('state', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='billingdetails_state', to='home.State')),
            ],
        ),
    ]
