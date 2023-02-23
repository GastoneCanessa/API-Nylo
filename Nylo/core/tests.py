from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {
            "username": "testcase", "email": "test@localhost.app",
            "password1": "change_me_123", "password2": "change_me_123" 
            }
        response = self.client.post("/api/rest-auth/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class SellerViewsetTestCase(APITestCase):
    list_url = reverse("seller-list")

    def setUp(self):
        self.user = User.objects.create_user(
            username="davinci",
            password="una_password_non_decifrabile",
            )
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        "capire come gestire i permessi ora funziona solo con IsAuthenticated"

    def test_sellers_list_un_authenticate(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_sellers_list_authenticate(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_sellers_create(self):
        data = {"name": "leonardo", "email": "davinci@gmail.com"}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["user"], "davinci")
        self.assertEqual(response.data["name"], "leonardo")

        "capire come far funzionare il test retrive"
    # def test_sellers_detail_retrive(self):
    #     response = self.client.get(reverse("seller-detail", kwargs={"pk":1}))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data["user"], "davinci")
