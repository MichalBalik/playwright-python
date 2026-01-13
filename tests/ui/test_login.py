import re
import pytest
from playwright.sync_api import Page, expect

URL = "https://www.saucedemo.com/"



class TestSwagLabsLogin:

    @pytest.fixture(autouse=True)
    def open_login_page(self, page: Page):
        page.goto(URL)

    """
    Verify login with correct credentials.
    Essential because the website requires user authentication
    in order to access protected website functions.
    """
    def test_login_successfully_with_valid_credentials(self, page: Page):
        page.fill('input[data-test="username"]', 'standard_user')
        page.fill('input[data-test="password"]', 'secret_sauce')
        page.click('input[data-test="login-button"]')

        expect(page).to_have_url(re.compile(".*inventory.html"))

    """
    Verify invalid user data.
    Essential to prevent unauthorized access for invalid users
    and to display error information.
    """
    def test_show_error_on_invalid_login(self, page: Page):
        page.fill('input[data-test="username"]', 'invalid_user')
        page.fill('input[data-test="password"]', 'wrong_password')
        page.click('input[data-test="login-button"]')

        error = page.locator('h3[data-test="error"]')
        expect(error).to_be_visible()
        expect(error).to_contain_text("Epic sadface")

    """
    Verify that login is not possible when the username or password is missing.
    Essential to reduce unnecessary backend requests.
    """
    def test_prevent_login_with_empty_username_or_password(self, page: Page):
        # empty username
        page.fill('input[data-test="password"]', 'secret_sauce')
        page.click('input[data-test="login-button"]')

        error = page.locator('h3[data-test="error"]')
        expect(error).to_be_visible()
        expect(error).to_contain_text("Username is required")

        # reload page for next test
        page.reload()

        # empty password
        page.fill('input[data-test="username"]', 'standard_user')
        page.click('input[data-test="login-button"]')

        error = page.locator('h3[data-test="error"]')
        expect(error).to_be_visible()
        expect(error).to_contain_text("Password is required")

    """
    Verify that the site does not allow a locked-out user to log in.
    It is essential to ensure that a locked-out user cannot access the website.
    """
    def test_not_allow_login_for_locked_out_user(self, page: Page):
        page.fill('input[data-test="username"]', 'locked_out_user')
        page.fill('input[data-test="password"]', 'secret_sauce')
        page.click('input[data-test="login-button"]')

        error = page.locator('h3[data-test="error"]')
        expect(error).to_be_visible()
        expect(error).to_contain_text("Sorry, this user has been locked out")

    """
    Verify password security.
    Essential to ensure the password is protected from unauthorized access.
    """
    def test_mask_password_input(self, page: Page):
        password_input = page.locator('input[data-test="password"]')
        expect(password_input).to_have_attribute("type", "password")

    """
    Verify the logout function.
    It is essential to ensure that the user can log out of the page after logging in.
    """
    def test_logout_successfully(self, page: Page):
        # login
        page.fill('input[data-test="username"]', 'standard_user')
        page.fill('input[data-test="password"]', 'secret_sauce')
        page.click('input[data-test="login-button"]')

        expect(page).to_have_url(re.compile("inventory.html"))

        # open menu and logout
        page.click('#react-burger-menu-btn')
        page.click('#logout_sidebar_link')

        expect(page).to_have_url(URL)
