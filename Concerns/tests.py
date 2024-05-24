from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Country, Profile, Order, CustomUser

class UserDetailAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')

    def test_get_user_detail(self):
        url = reverse('api_user_detail', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class CountryListAPITest(TestCase):
    def test_get_country_list(self):
        url = reverse('api_country_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class ProfileDetailAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='password')
        self.country = Country.objects.create(name='TestCountry')
        self.profile = Profile.objects.create(user=self.user, avatar='avatar.png', country=self.country)

    def test_get_profile_detail(self):
        url = reverse('api_profile_detail', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class OrderListAPITest(TestCase):
    def test_get_order_list(self):
        url = reverse('api_order_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class UserWithProfileAPITest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='password')
        self.country = Country.objects.create(name='TestCountry')
        self.profile = Profile.objects.create(user=self.user, avatar='avatar.png', country=self.country)

    def test_get_user_with_profile(self):
        url = reverse('api_user_with_profile', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class UsersWithProfileCountAPITest(TestCase):
    def test_get_users_with_profile_count(self):
        url = reverse('api_users_with_profile_count')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class UsersFromCountryAPITest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name='Testland')

    def test_get_users_from_country(self):
        url = reverse('api_users_from_country', args=[self.country.name])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class UsersWithOrderStatusAPITest(TestCase):
    def test_get_users_with_order_status(self):
        url = reverse('api_users_with_order_status', args=['Pending'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class UsersWithProfileAndOrderStatusAPITest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='password')
        self.country = Country.objects.create(name='TestCountry')
        self.profile = Profile.objects.create(user=self.user, avatar='avatar.png', country=self.country)
        self.order = Order.objects.create(user=self.user, status='delivered')

    def test_get_users_with_profile_and_order_status(self):
        url = reverse('api_users_with_profile_and_order_status', args=['delivered'])  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('name', data[0])  



class UserWithOrdersAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')

    def test_get_user_with_orders(self):
        url = reverse('api_user_with_orders', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class ViewsTestCase(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name="USA")
        self.user = User.objects.create(username="testuser")
        self.profile = Profile.objects.create(user=self.user, country=self.country)
        self.order = Order.objects.create(user=self.user, status="completed")

    def test_user_detail_view(self):
        response = self.client.get(reverse('user_detail', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], self.user.username)
        self.assertEqual(response.json()['country'], self.country.name)

    def test_country_list_view(self):
        response = self.client.get(reverse('country_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['name'], self.country.name)

    def test_profile_detail_view(self):
        response = self.client.get(reverse('profile_detail', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['country'], self.country.name)

    def test_order_list_view(self):
        response = self.client.get(reverse('order_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['status'], self.order.status)

    def test_user_with_profile_view(self):
        response = self.client.get(reverse('user_with_profile', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], self.user.username)
        self.assertEqual(response.json()['country'], self.country.name)

    def test_users_with_profile_count_view(self):
        response = self.client.get(reverse('users_with_profile_count'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['profile_count'], 1)

    def test_users_from_country_view(self):
        response = self.client.get(reverse('users_from_country', args=[self.country.name]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['name'], self.user.username)

    def test_users_with_order_status_view(self):
        response = self.client.get(reverse('users_with_order_status', args=[self.order.status]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['name'], self.user.username)

    def test_users_with_profile_and_country_view(self):
        response = self.client.get(reverse('users_with_profile_and_country'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['country'], self.country.name)

    def test_users_with_profile_and_order_status_view(self):
        response = self.client.get(reverse('users_with_profile_and_order_status', args=['completed']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['name'], self.user.username)

    def test_users_with_profile_count_and_country_view(self):
        response = self.client.get(reverse('users_with_profile_count_and_country', args=[self.country.name]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['profile_count'], 1)

    def test_user_with_orders_view(self):
        response = self.client.get(reverse('user_with_orders', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['status'], self.order.status)