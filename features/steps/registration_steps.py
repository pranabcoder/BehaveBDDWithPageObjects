import time
from behave import given, when, then

from Utilities import configReader
from features.pageobjects.RegistrationPage import RegistrationPage


@given(u'I navigate to qa.way2automation.com')
def step_impl(context):
    context.reg = RegistrationPage(context.driver)
    context.reg.open(configReader.readConfig("basic info", "testsiteurl"))
    time.sleep(3)


@when(u'I enter the name as "{name}"')
def step_impl(context, name):
    context.reg.setName(name)


@then(u'I enter the phone number as "{phone_number}"')
def step_impl(context, phone_number):
    context.reg.setPhoneNumber(phone_number)


@then(u'I enter the email as "{email}"')
def step_impl(context, email):
    context.reg.setEmail(email)


@then(u'I enter the country as "{country}"')
def step_impl(context, country):
    context.reg.setCountry(country)


@then(u'I enter the city as "{city}"')
def step_impl(context, city):
    context.reg.setCity(city)


@then(u'I enter the username as "{email}"')
def step_impl(context, email):
    context.reg.setUsername(email)


@then(u'I enter the password as "{password}"')
def step_impl(context, password):
    context.reg.setPassword(password)


@then(u'I click on the submit button')
def step_impl(context):
    context.reg.submitForm()
    assert False
    time.sleep(3)
