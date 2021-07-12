import os
from locust import HttpUser, task, constant


class QuickstartUser(HttpUser):
    wait_time = constant(0)
    url = os.environ.get('BOT_URL', '')
    auth_token = os.environ.get('AUTH_TOKEN', '')

    @task
    def test_nlp_short_input(self):
        headers = {
            'Authorization': self.auth_token,
            'Referer': self.host,
            'Content-Type': 'application/json'
        }
        self.client.post(self.url, json={"language": "en", "text": "Lorem ipsum sex dolor"}, headers=headers)

    @task
    def test_nlp_long_input(self):
        headers = {
            'Authorization': self.auth_token,
            'Referer': self.host,
            'Content-Type': 'application/json'
        }
        self.client.post(self.url, json={"language": "en", "text": "Lorem ipsum sex dolor amet, consectetur adipiscing elit. Donec vitae pellentesque arcu. Mauris vel arcu erat. Praesent in nulla et nulla condimentum rutrum. Sed dictum est orci, quis maximus nisl commodo ac. Ut cursus velit quis metus rhoncus consequat. Cras eu pharetra nulla, ac maximus eros. Cras malesuada, turpis vel rhoncus ullamcorper, mi purus malesuada ante, molestie cursus nunc risus non ante. Sed non est enim. Donec quis sagittis risus, ac scelerisque augue."
            "Sed rutrum quam nec sapien tristique venenatis. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Duis non vehicula leo, vitae suscipit orci. Integer ac mattis lacus, eu fermentum justo. Donec sit amet mauris fringilla quam cursus porta eget id ante. Proin fringilla dapibus pulvinar. Fusce mattis odio enim, in dignissim elit consectetur vitae. Sed tincidunt dictum sapien, sed auctor dui tristique vel."
            "Vestibulum laoreet diam eros, nec tristique justo lacinia et. Cras eu eros sem. Aenean malesuada consectetur dapibus. In quis feugiat lacus, et bibendum neque. Fusce massa ligula, pulvinar ut libero id, viverra semper felis. Pellentesque vulputate pharetra leo nec tincidunt. Nunc volutpat, turpis nec bibendum bibendum, felis lectus varius purus, eu tempor elit eros id felis. Morbi gravida tortor in metus."
        }, headers=headers)

    def on_start(self):
        pass

    def on_stop(self):
        pass
