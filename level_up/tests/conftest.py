import os

import pytest
from allauth.account.models import EmailAddress
from allauth.account.utils import user_email
from django.contrib.auth import get_user_model
from playwright.sync_api import Page
from django.test import Client
from playwright.sync_api import sync_playwright
from pytest_django.live_server_helper import LiveServer


# Set an environment variable to allow async operations in Django's synchronous context
# This is necessary for Playwright to work with Django's ORM in some cases
os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE","true")

@pytest.fixture
def browser_context_args(live_server: LiveServer):
    # 
    # Fixture to configure Playwright browser context with the live server URL.
    # Args:
    #     live_server: Django's LiveServer instance providing the test server URL.
    # Returns:
    #     Dictionary with the base URL for the browser context.
    # 
    return {"base_url" : live_server.url}

@pytest.fixture
def user_data():
    # 
    # Fixture to provide test user data (email and password).
    # Returns:
    #     Dictionary containing a test email and password.
    # 
    return {"email": "test@example.com", "password":"test_password123"}


@pytest.fixture
def verified_user(user_data):
    # 
    # Fixture to create a verified user in the database.
    # Args:
    #     user_data: Fixture providing test user email and password.
    # Returns:
    #     A User instance with a verified email address.
    #
    User = get_user_model()

    user = User.objects.create_user(
        email=user_data["email"],password=user_data["password"]
    )

    email,created = EmailAddress.objects.get_or_create(
        user=user, email=user_email(user)
    )

    email.verified = True
    email.save()

    return user
@pytest.fixture
def auth_page(page: Page, verified_user, user_data):
    #
    # Fixture to authenticate a Playwright page with a verified user session.
    # Args:
    #     page: Playwright Page object for browser interaction.
    #     verified_user: Fixture providing a verified user.
    #     user_data: Fixture providing test user email and password.
    # Returns:
    #     A Playwright Page object with an authenticated session cookie.
    #
    client = Client()
    resp = client.post("/accounts/login/", {"login":user_data["email"],"password":user_data["password"]})

    session_id = resp.cookies["sessionid"].value
    page.context.add_cookies(
        [
            {
                "name":"sessionid",
                "value": session_id,
                "domain": "localhost",
                "path": "/"
            }
        ]
    )
    return page





    
