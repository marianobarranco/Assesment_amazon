from behave import *
from selenium import webdriver
from Amazon.pages.homePage import HomePage
from Amazon.pages.signInPage import SignInPage
from Amazon.pages.todaysDealsPage import TodaysDeals
from Amazon.pages.productPage import ProductPage
from Amazon.pages.basketPage import BasketPage
import time


@given('I am on the Arab Emirates Amazon homepage')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="C:\\Users\\Juli\\PycharmProjects\\pythonProject\\Amazon\\resources\\webdrivers\\chromedriver_105.exe")
    driver = context.driver
    driver.maximize_window()
    home = HomePage(driver)

    home.go_to_amazon_ae_page()
    driver.refresh()


'''First scenario Methods'''

@when('I navigate to the sign in page')
def step_impl(context):
    driver = context.driver
    home = HomePage(driver)

    home.click_hamburger_navigation_menu()
    home.click_avatar_icon()


@when('I attempt to sign in with a valid but unregistered email')
def step_impl(context):
    driver = context.driver
    signin = SignInPage(driver)

    signin.enter_valid_email()
    signin.click_submit()

@then('I should remain in the sig in page')
def step_impl(context):
    driver = context.driver
    signin = SignInPage(driver)

    signin.verify_current_url()

@then('an error message should be displayed')
def step_impl(context):
    driver = context.driver
    signin = SignInPage(driver)

    signin.verify_alert_message()


'''Second scenario methods'''


@when('i select the first item in the second category in todays deals')
def step_impl(context):
    driver = context.driver
    home = HomePage(driver)
    today = TodaysDeals(driver)

    home.click_todays_deals()
    today.select_second_category()
    today.select_first_item()


@when('i attempt to add three units of the first item displayed to my cart')
def step_impl(context):
    driver = context.driver
    product = ProductPage(driver)

    product.store_product_information()
    product.add_three_items_to_cart()
    product.go_to_cart()
    time.sleep(5)

@then('i should see that the three items are added to my cart')
def step_impl(context):
    driver = context.driver
    basket = BasketPage(driver)

    basket.validate_product_title_and_quantity()

@then('the price and subtotal values are as expected')
def step_impl(context):
    driver = context.driver
    basket = BasketPage(driver)

    basket.validate_price_and_subtotal()


'''Third scenario methods'''

@when('i go to the Accounts and Lists option')
def step_impl(context):
    driver = context.driver
    home = HomePage(driver)

    home.hover_over_account_menu()
    time.sleep(3)


@when('i select the "{option}" option')
def step_impl(context,option):
    driver = context.driver
    home = HomePage(driver)

    home.select_option(option)


@then('i should be sent to the "{pages}" page')
def step_impl(context,pages):
    driver = context.driver
    signin = SignInPage(driver)

    signin.validate_page(pages)



