from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
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
from .serializers import UserSerializer, CountrySerializer, ProfileSerializer, OrderSerializer

class UserDetailAPIView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class CountryListAPIView(APIView):
    def get(self, request):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)

class ProfileDetailAPIView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        profile = user.profile
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

class OrderListAPIView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

class UserWithProfileAPIView(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    
class UsersWithProfileCountAPIView(APIView):
    def get(self, request):
        users = get_users_with_profile_count()
        data = [{'name': user.username, 'profile_count': user.profile_count} for user in users]
        return Response(data)

class UsersFromCountryAPIView(APIView):
    def get(self, request, country_name):
        users = get_users_with_country(country_name)
        data = [{'name': user.username} for user in users]
        return Response(data)

class UsersWithOrderStatusAPIView(APIView):
    def get(self, request, order_status):
        users = get_users_with_order_status(order_status)
        data = [{'name': user.username} for user in users]
        return Response(data)


class UsersWithProfileAndOrderStatusAPIView(APIView):
    def get(self, request, order_status):
        users = get_users_with_profile_and_order_status(order_status)
        data = [{'name': user.username} for user in users]
        return Response(data)


class UserWithOrdersAPIView(APIView):
    def get(self, request, user_id):
        user = get_user_with_orders(user_id)
        orders = user.order_set.all()
        data = [{'id': order.id, 'status': order.status} for order in orders]
        return Response(data)

class UserWithProfileAndCountryAPIView(APIView):
    def get(self, request, user_id):
        user = get_user_with_profile(user_id)
        data = {
            'name': user.username,
            'profile_avatar': user.profile.avatar if user.profile else None,
            'country': user.profile.country.name if user.profile else None
        }
        return Response(data)

class UserWithProfileAndOrderStatusAPIView(APIView):
    def get(self, request, user_id, order_status):
        user = get_object_or_404(User, id=user_id)
        orders = user.order_set.filter(status=order_status)
        data = [{'id': order.id, 'status': order.status} for order in orders]
        return Response(data)


    


class UsersWithProfileAndOrderStatusAPIView(APIView):
    def get(self, request, order_status):
        users = JoinWithQuerySet(User.objects.all()).join_with_profile().join_with('order_set', status=order_status)
        data = [{'name': user.username} for user in users]
        return Response(data)

