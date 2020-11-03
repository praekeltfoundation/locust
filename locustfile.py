import os
from bs4 import BeautifulSoup
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)
    domain = os.environ.get('TEST_DOMAIN', '')

    user = {
        "creds": {
            "username": os.environ.get("TEST_USERNAME", ''),
            "password": os.environ.get("TEST_PASSWORD", '')
        }
    }
    urls = os.environ.get('TEST_PATHS', '').split(',')

    login_url = os.environ.get('TEST_LOGIN_PATH', '/users/login')
    csrftoken_append = os.environ.get('TEST_CSRFTOKEN_APPEND', True)
    csrftoken_name = os.environ.get('TEST_CSRFTOKEN_NAME', 'csrfmiddlewaretoken')

    @task
    def test_page(self):
        for url in self.urls:
            self.client.get(self.domain + url)

    def on_start(self):
        url = self.login_url
        creds = self.user.get('creds')
        if all([creds.get('username'), creds.get('password'), url]):
            if self.csrftoken_append:
                res = self.client.get(self.domain + url)
                soup = BeautifulSoup(res.content, 'html.parser')
                csrftoken = soup.find('input', attrs=dict(name=self.csrftoken_name))
                creds.update({self.csrftoken_name: csrftoken.get('value')})
            self.client.post(self.domain + url, json=creds)
