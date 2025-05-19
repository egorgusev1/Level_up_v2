import re # Regular expression module for extracting URLs from text

from django.core import mail
from playwright.sync_api import Page
from allauth.account.models import EmailAddress

from tests.pages.auth import SignupPage, ConfirmationPage
from app.models import UserProfile

def test_signup(page: Page, user_data: dict):
    # 
    # Test to verify the signup process, including email confirmation and user verification.
    # Args:
    #     page: Playwright Page object for browser interaction.
    #     user_data: Fixture providing test user email and password.
    # 
    page.goto("/")
    signup_page = SignupPage(page)
    signup_page.complete_signup_form(user_data["email"], user_data["password"])
    
    confirmation_link = re.search(
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
        mail.outbox[0].body,
    ).group()

    page.goto(confirmation_link)

    confirmation_page = ConfirmationPage(page)
    confirmation_page.confirm_button.click()

    user = UserProfile.objects.get(email=user_data["email"])
    email_address = EmailAddress.objects.get(user=user, email=user_data["email"])
    assert email_address.verified


