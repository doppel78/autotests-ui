import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.authorization
@pytest.mark.regression
def test_authorization_error():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')


        email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
        password_input = page.get_by_test_id('login-form-password-input').locator('//div//input')

        login_button = page.get_by_test_id('login-page-login-button')
        alert = page.locator('//div[@data-testid = "login-page-wrong-email-or-password-alert"]')

        email_input.fill('hooehu')
        password_input.fill('qwerty123')

        login_button.click()

        expect(alert).to_be_visible()

        expect(alert).to_have_text('Wrong email or password')
