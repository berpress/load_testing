import logging
import enum


class LogType(enum.Enum):
   INFO = 1
   DEBUG = 2
   ERROR = 3
   CRITICAL = 4


# Class definition #
class Logger:

    log_obj = None

    @staticmethod
    def init_logger(name, log_file):
        Logger.log_obj = logging.getLogger(name)
        open(log_file, 'w').close()

    @staticmethod
    def log_message(message, log_type=LogType.INFO):
        if not Logger.log_obj:
            print(message)
            return

        if log_type == LogType.INFO:
            Logger.log_obj.info(message)
        elif log_type == LogType.DEBUG:
            Logger.log_obj.debug(message)
        elif log_type == LogType.ERROR:
            Logger.log_obj.error(message)
        else:
            Logger.log_obj.critical(message)
