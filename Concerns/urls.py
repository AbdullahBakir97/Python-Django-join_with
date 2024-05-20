from django.urls import path
from . import views
from . import api

urlpatterns = [
    
    # URLs for traditional Django views
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
    path('countries/', views.country_list, name='country_list'),
    path('profile/<int:user_id>/', views.profile_detail, name='profile_detail'),
    path('orders/', views.order_list, name='order_list'),
    path('user-with-profile/<int:user_id>/', views.user_with_profile, name='user_with_profile'),
    path('users-with-profile-count/', views.users_with_profile_count, name='users_with_profile_count'),
    path('users-from-country/<str:country_name>/', views.users_from_country, name='users_from_country'),
    path('users-with-order-status/<str:order_status>/', views.users_with_order_status, name='users_with_order_status'),
    path('users-with-profile-and-country/', views.users_with_profile_and_country, name='users_with_profile_and_country'),
    path('users-with-profile-and-order-status/<str:order_status>/', views.users_with_profile_and_order_status, name='users_with_profile_and_order_status'),
    path('users-with-profile-count-and-country/<str:country_name>/', views.users_with_profile_count_and_country, name='users_with_profile_count_and_country'),
    path('user-with-orders/<int:user_id>/', views.user_with_orders, name='user_with_orders'),
    
    # URLs for REST API views
    path('api/user-detail/<int:user_id>/', api.UserDetailAPIView.as_view(), name='api_user_detail'),
    path('api/country-list/', api.CountryListAPIView.as_view(), name='api_country_list'),
    path('api/profile-detail/<int:user_id>/', api.ProfileDetailAPIView.as_view(), name='api_profile_detail'),
    path('api/order-list/', api.OrderListAPIView.as_view(), name='api_order_list'),
    path('api/user-with-profile/', api.UserWithProfileAPIView.as_view(), name='api_user_with_profile'),
    path('api/users-with-profile-count/', api.UsersWithProfileCountAPIView.as_view(), name='api_users_with_profile_count'),
    path('api/users-from-country/<str:country_name>/', api.UsersFromCountryAPIView.as_view(), name='api_users_from_country'),
    path('api/users-with-order-status/<str:order_status>/', api.UsersWithOrderStatusAPIView.as_view(), name='api_users_with_order_status'),
    path('api/users-with-profile-and-order-status/<str:order_status>/', api.UsersWithProfileAndOrderStatusAPIView.as_view(), name='api_users_with_profile_and_order_status'),
    path('api/user-with-orders/<int:user_id>/', api.UserWithOrdersAPIView.as_view(), name='api_user_with_orders'),
    path('api/user-with-profile-and-country/<int:user_id>/', api.UserWithProfileAndCountryAPIView.as_view(), name='api_user_with_profile_and_country'),
    path('api/user-with-profile-and-order-status/<int:user_id>/<str:order_status>/', api.UserWithProfileAndOrderStatusAPIView.as_view(), name='api_user_with_profile_and_order_status'),
    path('api/users-with-profile-and-order-status/<str:order_status>/', api.UsersWithProfileAndOrderStatusAPIView.as_view(), name='api_users_with_profile_and_order_status'),
]
