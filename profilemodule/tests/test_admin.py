# your_app/tests/test_admin.py

import pytest
from django.contrib.admin.sites import AdminSite
from django.test import RequestFactory
from profilemodule.admin import *
from profilemodule.models import *

@pytest.mark.django_db
def test_admin_model():
    # Create a sample object for testing
    obj = About.objects.create(full_name='Test Object',designation = 'ge', mobile='01888')

    # Create an instance of the admin site
    admin_site = AdminSite()

    # Create an instance of the admin model and register it with the admin site
    model_admin = AboutAdmin(About, admin_site)
    admin_site.register(About, AboutAdmin)

    # Create a request for the admin page
    request = RequestFactory().get(f'admin/profilemodule/About/{obj.id}/change/')

    # Create an admin form based on the request
    form = model_admin.get_form(request)(instance=obj)

    # Your test assertions go here
    assert form

