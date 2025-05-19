# Import the Page class from Playwright's synchronous API
# This is used to interact with web pages in a browser automation context
from playwright.sync_api import Page


# Define the SignupPage class to handle interactions with the signup page
class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_field = page.get_by_placeholder("Email address")
        self.password_field = page.get_by_placeholder("Password")
        self.signup_button = page.get_by_role("button", name="Create your account")

    def complete_signup_form(self, email, password):
        # Method to fill out and submit the signup form
        # Fill the email field with the provided email
        self.email_field.fill(email)
        self.password_field.fill(password)
        self.signup_button.click()

# Define the LoginPage class to handle interactions with the login page
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_field = page.get_by_placeholder("Email address")
        self.password_field = page.get_by_placeholder("Password")
        # Locate the sign-in button by its role ("button") and name ("Sign in")
        # Note: The variable name 'signup_button' is misleading; it should be 'signin_button'
        self.signup_button = page.get_by_role("button", name="Sign in")



# Define the ConfirmationPage class to handle interactions with a confirmation page
class ConfirmationPage:
    def __init__(self, page: Page):
        self.page = page
        # Locate a button by its role ("button")
        # Note: This is a generic locator; it may need a more specific identifier (e.g., name or text)
        self.confirm_button = page.get_by_role("button")