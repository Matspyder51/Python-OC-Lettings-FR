from django.urls import resolve, reverse


def test_status_code(client):
    res = client.get(reverse("index"))
    assert res.status_code == 200


def test_title(client):
    res = client.get(reverse("index"))
    assert str(res.content).find("<title>Holiday Homes</title>")
