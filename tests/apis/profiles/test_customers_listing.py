# @pytest.mark.django_db
# def test_customers_listing(api_client, user):
#     api_client.force_authenticate(user)
#     url = reverse("customers:profiles-list")
#     assert url == "/api/profiles/"
#     response = api_client.get(url)
#     assert response.status_code == status.HTTP_200_OK, response.content
#     assert "customers" in response.json()
