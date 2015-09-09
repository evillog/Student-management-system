class User(object):
    def __init__(self, number, password):
        self.number = number
        self.password = password
        self.user_list = {}

    def set_number(self, number):
        self.number = number

    def set_password(self, password):
        self.password = password

    def get_number(self):
        return self.number

    def check_password(self, psw):
        if self.password == psw:
            return True
        else:
            print "Wrong password or account!"

    def change_password(self):
        new_pass = raw_input("Please input your new password: ")
        repeat_pass = raw_input("Please repeat your new password: ")
        if new_pass == repeat_pass:
            self.password = new_pass
        else:
            print "Input error!"





