# Python-Django-join_with

## Overview

The `Python-Django-join_with` project provides a custom Django queryset class, `JoinWithQuerySet`, that simplifies complex join operations between Django models. This project includes custom query functions and API views to demonstrate how to use these operations effectively.

## Features

- Custom Django queryset class for easy join operations.
- Examples of joining user profiles, orders, and countries.
- REST API views for fetching joined data.
- Comprehensive test coverage.

## Requirements

- Python 3.x
- Django 3.x or later
- Django REST Framework

## Installation

To run the `Python-Django-join_with` project locally, follow these steps:

1. *Clone the repository*:

  ```
  git clone https://github.com/AbdullahBakir97/Python-Django-join_with.git
  cd Python-Django-join_with
  ```
2. *Create and activate a virtual environment*:

  ```
  python -m venv venv
  source venv/bin/activate # On Windows use venv\Scripts\activate
  ```

3. *Install dependencies*:

  ```
  pip install -r requirements.txt
  ```

4. *Run migrations*:
   
  ```
  python manage.py migrate
  ```

5. *Run the development server*:
   
  ```
  python manage.py runserver
  ```


## Usage

### Queryset Operations

This project demonstrates various queryset operations using the `JoinWithQuerySet` class. Here are a few examples:

1. *Get users with profile and order status*:
   
```python
from django.contrib.auth.models import User
from .queries import get_user_with_profile
from .querysets import JoinWithQuerySet

users = JoinWithQuerySet(User.objects.all()).join_with_profile().join_with('order_set', status='completed')

# Example usage:
user_id = 1
user = get_user_with_profile(user_id)
print(user.username)
print(user.profile.avatar.url if user.profile else None)
print(user.profile.country.name if user.profile else None)

# Users With Profile Count

from .queries import get_users_with_profile_count

# Example usage:
users = get_users_with_profile_count()
for user in users:
    print(f"User: {user.username}, Profile Count: {user.profile_count}")

# Users From Country

from .queries import get_users_with_country

# Example usage:
country_name = "USA"
users = get_users_with_country(country_name)
for user in users:
    print(f"User: {user.username}")

# Users With Order Status

from .queries import get_users_with_order_status

# Example usage:
order_status = "completed"
users = get_users_with_order_status(order_status)
for user in users:
    print(f"User: {user.username}")

# Users With Profile and Order Status

from .queries import get_users_with_profile_and_order_status

# Example usage:
order_status = "completed"
users = get_users_with_profile_and_order_status(order_status)
for user in users:
    print(f"User: {user.username}")


```

## API Endpoints

The project provides several API endpoints to fetch joined data:

- *Get user details*:

  ```sql
  GET /api/user-detail/<int:user_id>/
  ```
- *Get list of countries*:

  ```sql
  GET /api/country-list/
  ```
- *Get profile details by user ID*:
  
  ```sql
  GET /api/profile-detail/<int:user_id>/
  ```
- *Get list of orders*:

  ```sql
  GET /api/order-list/
  ```
- *Get users with profiles*:

  ```sql
  GET /api/user-with-profile/
  ```
- *Get users with profile count*:

  ```sql
  GET /api/users-with-profile-count/
  ```
- *Get users from a specific country*:

  ```sql
  GET /api/users-from-country/<str:country_name>/
  ```
- *Get users with a specific order status*:

  ```sql
  GET /api/users-with-order-status/<str:order_status>/
  ```
- *Get users with profile and order status*:

  ```sql
  GET /api/users-with-profile-and-order-status/<str:order_status>/
  ```
- *Get user with orders by user ID*:

  ```sql
  GET /api/user-with-orders/<int:user_id>/
  ```
- *Get user with profile and country by user ID*:

  ```sql
  GET /api/user-with-profile-and-country/<int:user_id>/
  ```
- *Get user with profile and order status by user ID*:

  ```sql
  GET /api/user-with-profile-and-order-status/<int:user_id>/<str:order_status>/
  ```
## Credits

- Custom queryset functionality inspired by various Django community resources.
- Project structure and examples based on best practices in Django development.


## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on GitHub or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
