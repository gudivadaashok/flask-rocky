from behave import *

@when(u'I navigate to Home Page')
def step_impl(ctx):
    ctx.resp = ctx.client.get('/')

@then(u'Home Page should be displayed')
def step_impl(ctx):
    assert 'This is the home page' in ctx.resp
