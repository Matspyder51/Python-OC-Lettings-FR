import pytest
from django.urls import reverse


# Create your tests here.
@pytest.mark.django_db
def test_status_code(client):
    res = client.get(reverse("profiles:index"))
    assert res.status_code == 200


@pytest.mark.django_db
def test_title(client):
    res = client.get(reverse("profiles:index"))
    assert str(res.content).find("<title>Profiles</title>")
