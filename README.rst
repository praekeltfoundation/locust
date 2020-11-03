Locust Load testing service
===========================

Env Vars that can be added:
---------------------------

TEST_DOMAIN
    required: String in the format `https://somedomain.com` without a trailing slash

TEST_PATHS
    required: A comma separated list of paths to test eg `/,/contact/,/about/`
    if omitted only the domain root will be hit/tested by the locust script


*In an instance where a user is required to be logged in*

TEST_USERNAME
    This is the var to set to provide the script with a username

TEST_PASSWORD
    This is the var to set to provide the script with a username

TEST_LOGIN_PATH
    This is a path of the auth url, defaults to `/users/login`

TEST_LOGOUT_PATH
    This is a path of the auth url, defaults to `/users/logout`

TEST_CSRFTOKEN_APPEND
    Variable to determine whether the script should retrieve and inject a csrf token in the login request
    defaults to `True`

TEST_CSRFTOKEN_NAME
    Different systems name their csrf token inputs differently,
    you can change the name of the csrf token to extract and inject into the request with this variable.
    defaults to `csrfmiddlewaretoken`
