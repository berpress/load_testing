from locust import task, SequentialTaskSet
from common.log_module import *
from common.utils import UtilHelper


class MyAccountNavigate(SequentialTaskSet):

    @task
    def fetch_personal_information(self):
        header = UtilHelper.get_base_header_with_cookie(self.user.get_cookie())
        with self.client.get("/index.php?controller=addresses", headers=header,
                             catch_response=True) as response:
            if response.status_code == 200:
                Logger.log_message("fetch my-account user address "
                                   + self.user.get_email())
            else:
                response.failure("Failed to fetch my-account user address"
                                 + self.user.get_email())
                Logger.log_message("Failed to fetch my-account user address "
                                   + self.user.get_email(), LogType.ERROR)

    @task
    def exit_task_execution(self):
        self.interrupt()
