import os
from locust import HttpUser, task, constant


class QuickstartUser(HttpUser):
    wait_time = constant(0)

    # Topic lookup flow and Result in Lookup_unhandled_v2
    topic_url = os.environ.get('TOPIC_URL', '')
    primary_url = os.environ.get('PRIMARY_LOOKUP_URL', '')
    secondary_url = os.environ.get('SECONDARY_LOOKUP_URL', '')

    # Each task below was run individually

    # @task
    # def test_topic_url(self):
    #     self.client.get(self.topic_url + "AboMSSA2")

    @task
    def test_primary_url(self):
        self.client.get(self.primary_url + "Lorem ipsum sed dolor amet, consectetur adipiscing elit. Donec vitae pellentesque arcu. Mauris vel arcu erat. Praesent in nulla et nulla condimentum rutrum. Sed dictum est orci, quis maximus nisl commodo ac. Ut cursus velit quis metus rhoncus consequat. Cras eu pharetra nulla, ac maximus eros. Cras malesuada, turpis vel rhoncus ullamcorper, mi purus malesuada ante, molestie cursus nunc risus non ante. Sed non est enim. Donec quis sagittis risus, ac scelerisque augue."
"Sed rutrum quam nec sapien tristique venenatis. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Duis non vehicula leo, vitae suscipit orci. Integer ac mattis lacus, eu fermentum justo. Donec sit amet mauris fringilla quam cursus porta eget id ante. Proin fringilla dapibus pulvinar. Fusce mattis odio enim, in dignissim elit consectetur vitae. Sed tincidunt dictum sapien, sed auctor dui tristique vel."
"Vestibulum laoreet diam eros, nec tristique justo lacinia et. Cras eu eros sem. Aenean malesuada consectetur dapibus. In quis feugiat lacus, et bibendum neque. Fusce massa ligula, pulvinar ut libero id, viverra semper felis. Pellentesque vulputate pharetra leo nec tincidunt. Nunc volutpat, turpis nec bibendum bibendum, felis lectus varius purus, eu tempor elit eros id felis. Morbi gravida tortor in metus."
)

#     @task
#     def test_secondary_url(self):
#         self.client.get(self.secondary_url + "Lorem ipsum sed dolor amet, consectetur adipiscing elit. Donec vitae pellentesque arcu. Mauris vel arcu erat. Praesent in nulla et nulla condimentum rutrum. Sed dictum est orci, quis maximus nisl commodo ac. Ut cursus velit quis metus rhoncus consequat. Cras eu pharetra nulla, ac maximus eros. Cras malesuada, turpis vel rhoncus ullamcorper, mi purus malesuada ante, molestie cursus nunc risus non ante. Sed non est enim. Donec quis sagittis risus, ac scelerisque augue."
# "Sed rutrum quam nec sapien tristique venenatis. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Duis non vehicula leo, vitae suscipit orci. Integer ac mattis lacus, eu fermentum justo. Donec sit amet mauris fringilla quam cursus porta eget id ante. Proin fringilla dapibus pulvinar. Fusce mattis odio enim, in dignissim elit consectetur vitae. Sed tincidunt dictum sapien, sed auctor dui tristique vel."
# "Vestibulum laoreet diam eros, nec tristique justo lacinia et. Cras eu eros sem. Aenean malesuada consectetur dapibus. In quis feugiat lacus, et bibendum neque. Fusce massa ligula, pulvinar ut libero id, viverra semper felis. Pellentesque vulputate pharetra leo nec tincidunt. Nunc volutpat, turpis nec bibendum bibendum, felis lectus varius purus, eu tempor elit eros id felis. Morbi gravida tortor in metus.")

    def on_start(self):
        pass

    def on_stop(self):
        pass
