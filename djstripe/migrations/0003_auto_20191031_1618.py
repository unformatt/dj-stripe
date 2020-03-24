# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-10-31 20:18
from __future__ import unicode_literals

from django.db import migrations
import djstripe.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0002_auto_20180627_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=djstripe.fields.StripeCharField(help_text='The primary user\u2019s email address.', max_length=255),
        ),
        migrations.AlterField(
            model_name='account',
            name='product_description',
            field=djstripe.fields.StripeCharField(help_text='Internal-only description of the product sold or service provided by the business. It\u2019s used by Stripe for risk and underwriting purposes.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='number',
            field=djstripe.fields.StripeCharField(help_text='A unique, identifying string that appears on emails sent to the customer for this invoice. This starts with the customer\u2019s unique invoice_prefix if it is specified.', max_length=64, null=True),
        ),
    ]