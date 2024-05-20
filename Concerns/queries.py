from django.db.models import Count
from .models import Profile, Country, Order
from django.contrib.auth.models import User

def get_user_with_profile(user_id):
    """
    Fetch a user along with their profile.
    """
    return User.objects.select_related('profile').get(id=user_id)

def get_user_with_orders(user_id):
    """
    Fetch a user along with their orders.
    """
    return User.objects.prefetch_related('order_set').get(id=user_id)

def get_users_with_profile_count():
    """
    Fetch all users with a count of their profiles.
    """
    return User.objects.annotate(profile_count=Count('profile'))

def get_users_with_country(country_name):
    """
    Fetch all users belonging to a specific country.
    """
    return User.objects.filter(profile__country__name=country_name)

def get_users_with_order_status(order_status):
    """
    Fetch all users who have orders with a specific status.
    """
    return User.objects.filter(order__status=order_status).distinct()


def get_users_with_profile_and_order_status(order_status):
    """
    Fetch all users along with their profiles and orders with a specific status.
    """
    return User.objects.select_related('profile').prefetch_related('order_set').filter(order__status=order_status).distinct()

