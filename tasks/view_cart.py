from locust import task, SequentialTaskSet
from common.utils import UtilHelper


class ViewCart(SequentialTaskSet):

    @task
    def get_all_cart_tem(self):
        header = UtilHelper.get_base_header_with_cookie(self.user.get_cookie())
        with self.client.get("/index.php?controller=order", headers=header,
                             catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get all cart items, StatusCode: "
                                 + str(response.status_code))
            else:
                if "Shopping-cart summary" in response.text:
                    response.success()
                else:
                    response.failure("Failed to get all cart items, Text: "
                                     + response.text)

    @task
    def exit_navigation(self):
        self.interrupt()
