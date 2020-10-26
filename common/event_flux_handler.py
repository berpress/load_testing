import json
import pytz
from influxdb import InfluxDBClient
from locust import events
import socket
import datetime


class EventInfluxHandlers:

    hostname = socket.gethostname()
    data_base_name = "locustdb"
    table_name = "REST_Table"

    influxDbClient = InfluxDBClient(host='localhost',
                                    port=8086,
                                    database=data_base_name)

    @staticmethod
    def init_influx_client():
        EventInfluxHandlers.influxDbClient.\
            drop_database(EventInfluxHandlers.data_base_name)
        EventInfluxHandlers.influxDbClient.\
            create_database(EventInfluxHandlers.data_base_name)
        EventInfluxHandlers.influxDbClient.switch_database(
            EventInfluxHandlers.data_base_name
        )

    @staticmethod
    @events.request_success.add_listener
    def request_success_handlers(request_type, name, response_time, response_length,
                                 **kwagrs):
        success_temp = \
            '[{"measurement": "%s",\
            "tags": {\
                "hostname": "%s",\
                "requestName": "%s",\
                "requestType": "%s",\
                "status": "%s"\
            },\
            "time": "%s",\
            "fields": {\
                "responseTime": "%s",\
                "responseLength": "%s"\
            }\
         }]'

        json_string = success_temp % (EventInfluxHandlers.table_name,
                                      EventInfluxHandlers.hostname, name, request_type,
                                      "PASS", datetime.datetime.now(tz=pytz.UTC),
                                      response_time, response_length)
        EventInfluxHandlers.influxDbClient.write_points(json.loads(json_string))

    @staticmethod
    @events.request_failure.add_listener
    def request_failure_handlers(request_type, name, response_time, response_length,
                                 exception, **kwagrs):
        failure_temp = \
            '[{"measurement": "%s",\
            "tags": {\
                "hostname": "%s",\
                "requestName": "%s",\
                "requestType": "%s",\
                "status": "%s",\
                "exception": "%s"\
            },\
            "time": "%s",\
            "fields": {\
                "responseTime": "%s",\
                "responseLength": "%s"\
            }\
         }]'

        json_string = failure_temp % (EventInfluxHandlers.table_name,
                                      EventInfluxHandlers.hostname, name, request_type,
                                      "FAIL", exception,
                                      datetime.datetime.now(tz=pytz.UTC),
                                      response_time, response_length)
        EventInfluxHandlers.influxDbClient.write_points(json.loads(json_string))
