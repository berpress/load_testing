from locust import HttpUser


class AbstractUser(HttpUser):
    abstract = True

    def __init__(self, parent):
        super(AbstractUser, self).__init__(parent)
        self.user_attr = {}

    def set_email(self, email):
        self.user_attr['email'] = email

    def get_email(self):
        if 'email' in self.user_attr.keys():
            return self.user_attr['email']
        else:
            return None

    def set_cookie(self, cookie):
        self.user_attr['cookie'] = cookie

    def get_cookie(self):
        return self.user_attr['cookie']