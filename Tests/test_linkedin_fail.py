import allure
from Data.credentials import user


@allure.feature('Login page')
@allure.story('The first step')
def test_login(app, screenshot_on_failure):
    app.linked.type_login(user['email'])
    print("Locating and fill in username")

    app.linked.type_pass(user['password'])
    print("Locating and fill in password form...")

    app.linked.press_button_signin()

    # get title of the page
    expected_title = 'Intentionally down the test' # for testing purpose
    actual_title = app.linked.title
    print(f'It is expected the page title starts with "{expected_title}".'
          f'The actual title is "{actual_title}"')

    assert expected_title in actual_title
    print("Assertion completed")

# py.test --alluredir=/home/stable/Documents/Automation_SS/Python/CH_096_TAQC/Reports_Allure
# allure serve /home/stable/Documents/Automation_SS/Python/CI_j/Reports_Allure
# (venv_demo2) stable@Castle:~/Documents/Automation_SS/Python/CI_jenkins$ py.test -v --setup-show --alluredir=/home/stable/Documents/Automation_SS/Python/CI_jenkins/Reports_Allure /home/stable/Documents/Automation_SS/Python/CI_jenkins/Tests/test_linkedin.py
