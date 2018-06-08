# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from oscar.core.loading import get_model

from ecommerce.core.constants import COURSE_ENTITLEMENT_PRODUCT_CLASS_NAME

ProductAttribute = get_model("catalogue", "ProductAttribute")
ProductClass = get_model("catalogue", "ProductClass")


def create_idverifyreq_attribute(apps, schema_editor):
    """Create entitlement code 'id_verification_required' attribute."""
    entitlement_code_class = ProductClass.objects.get(name=COURSE_ENTITLEMENT_PRODUCT_CLASS_NAME)
    ProductAttribute.objects.create(
        product_class=entitlement_code_class,
        name='id_verification_required',
        code='id_verification_required',
        type='boolean',
        required=False
    )

class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
        ('catalogue', '0025_course_entitlement'),
        ('catalogue', '0030_auto_20180124_1131')
    ]
    operations = [
        migrations.RunPython(create_idverifyreq_attribute)
    ]
