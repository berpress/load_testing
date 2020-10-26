from locust import events

from tasks.category import CategoryNavigate
from tasks.view_cart import ViewCart
from users.guest_user import GuestHttpUser
from users.register_user import RegisteredHttpUser
from tasks.account import MyAccountNavigate
from common.user_loader import UserLoader
from common.log_module import Logger
from common.event_flux_handler import EventInfluxHandlers


@events.test_start.add_listener
def on_test_start(**kwargs):
    if kwargs['environment'].parsed_options.logfile:
        Logger.init_logger(__name__, kwargs['environment'].parsed_options.logfile)
    UserLoader.load_users()
    EventInfluxHandlers.init_influx_client()
    Logger.log_message("......... Initiating Load Test .......")


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    Logger.log_message("........ Load Test Completed ........")


class UserGroupA(RegisteredHttpUser):
    weight = 1
    RegisteredHttpUser.tasks = [MyAccountNavigate, CategoryNavigate, ViewCart]


class UserGroupB(GuestHttpUser):
    weight = 4
    GuestHttpUser.tasks = [CategoryNavigate, ViewCart]






