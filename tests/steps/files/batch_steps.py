
from assertpy import assert_that
from behave import given, when, then
import subprocess


@given(u'I have a batch file')
def given_i_have_a_batch_file(context):
    context.file_path = "test.bat"


@when(u'I run it')
def when_i_run_it(context):
    context.p = subprocess.Popen(f'{context.file_path}', creationflags=subprocess.CREATE_NEW_CONSOLE)
    stdout, stderr = context.p.communicate()
    context.return_code = context.p.returncode


@then(u'it executes')
def then_it_executes(context):
    assert_that(context.return_code).is_equal_to(0)
