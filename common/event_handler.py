from locust import events
import socket
import csv


class EventHandlers:

    hostname = socket.gethostname()
    req_success_data_list = []
    req_failure_data_list = []
    req_success_data_list.append(["HostName", "RequestType", "Name", "ResponseTime",
                                  "ResponseLength", "Status"])
    req_failure_data_list.append(["HostName", "RequestType", "Name", "ResponseTime",
                                  "ResponseLength", "Exception", "Status"])

    @staticmethod
    @events.request_success.add_listener
    def request_success_handlers(request_type, name, response_time, response_length,
                                 **kwagrs):
        EventHandlers.req_success_data_list.append([EventHandlers.hostname, 
                                                    request_type, name, response_time,
                                                   response_length, "PASS"])

    @staticmethod
    @events.request_failure.add_listener
    def request_failure_handlers(request_type, name, response_time, response_length,
                                 exception, **kwagrs):
        EventHandlers.req_failure_data_list.append([EventHandlers.hostname,
                                                    request_type, name, response_time,
                                                    response_length, exception, "FAIL"])

    @staticmethod
    def save_success_stats():
        with open("success_req_stats.csv", "wt") as csv_file:
            writer = csv.writer(csv_file)
            for value in EventHandlers.req_success_data_list:
                writer.writerow(value)

    @staticmethod
    def save_failure_stats():
        with open("failure_req_stats.csv", "wt") as csv_file:
            writer = csv.writer(csv_file)
            for value in EventHandlers.req_failure_data_list:
                writer.writerow(value)

    @staticmethod
    @events.quitting.add_listener
    def exit_handlers(**kwargs):
        EventHandlers.save_success_stats()
        EventHandlers.save_failure_stats()
