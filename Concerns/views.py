from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, Http404
from .models import Country, Profile, Order
from django.contrib.auth.models import User
from .querysets import JoinWithQuerySet
from .queries import (
    get_user_with_profile, 
    get_user_with_orders, 
    get_users_with_profile_count,
    get_users_with_country,
    get_users_with_order_status,
    get_users_with_profile_and_order_status,
)


app_name = 'Concerns'

def user_detail(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
        
    profile_avatar = user.profile.avatar.url if user.profile and user.profile.avatar else None
    country_name = user.profile.country.name if user.profile else None
    
    data = {
        'name': user.username,
        'profile_avatar': profile_avatar,
        'country': country_name
    }
    return JsonResponse(data)

def country_list(request):
    countries = Country.objects.all()
    data = [{'id': country.id, 'name': country.name} for country in countries]
    return JsonResponse(data, safe=False)

def profile_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    profile = user.profile
    if profile:
        avatar_url = profile.avatar.url if profile.avatar else None
        data = {
            'avatar_url': avatar_url,
            'country': profile.country.name
        }
    else:
        data = {}
    return JsonResponse(data)

def order_list(request):
    orders = Order.objects.all()
    data = [{'id': order.id, 'user': order.user.username, 'status': order.status} for order in orders]
    return JsonResponse(data, safe=False)

# New views utilizing custom query functions

def user_with_profile(request, user_id):
    user = get_user_with_profile(user_id)
    data = {
        'name': user.username,
        'profile_avatar': user.profile.avatar if user.profile else None,
        'country': user.profile.country.name if user.profile else None
    }
    return JsonResponse(data)

def users_with_profile_count(request):
    users = get_users_with_profile_count()
    data = [{'name': user.username, 'profile_count': user.profile_count} for user in users]
    return JsonResponse(data, safe=False)

def users_from_country(request, country_name):
    users = get_users_with_country(country_name)
    data = [{'name': user.username} for user in users]
    return JsonResponse(data, safe=False)

def users_with_order_status(request, order_status):
    users = get_users_with_order_status(order_status)
    data = [{'name': user.username} for user in users]
    return JsonResponse(data, safe=False)

# Additional views using custom queryset methods

def users_with_profile_and_country(request):
    users = JoinWithQuerySet(User.objects.all()).join_with_profile().join_with('profile__country')
    data = [{'name': user.username, 'country': user.profile.country.name} for user in users]
    return JsonResponse(data, safe=False)

def users_with_profile_and_order_status(request, order_status):
    users = JoinWithQuerySet(User.objects.all()).join_with_profile().join_with('order_set', status=order_status)
    data = [{'name': user.username} for user in users]
    return JsonResponse(data, safe=False)

def users_with_profile_count_and_country(request, country_name):
    users = JoinWithQuerySet(User.objects.all()).annotate_profile_count().filter_by_country(country_name)
    data = [{'name': user.username, 'profile_count': user.profile_count} for user in users]
    return JsonResponse(data, safe=False)


def users_with_profile_and_order_status(request, order_status):
    users = get_users_with_profile_and_order_status(order_status)
    data = [{'name': user.username} for user in users]
    return JsonResponse(data, safe=False)


def user_with_orders(request, user_id):
    user = get_user_with_orders(user_id)
    orders = user.order_set.all()
    data = [{'id': order.id, 'status': order.status} for order in orders]
    return JsonResponse(data, safe=False)
