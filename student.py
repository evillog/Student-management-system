from user import User


class Student(User):
    def __init__(self, number, password, is_exit=False, score=0):
        User.__init__(self, number, password, is_exit)
        self._score = 0

        self.score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if int(value) < 0:
            raise ValueError("Negative value not allowed: %s" % value)
        self._score = value

    def get_score(self):
        return self.score

    @staticmethod
    def show_menu():
        print "1.query score"
        print "2.change password"
        print "0.quit"

    @staticmethod
    def choose_menu():
        choice = raw_input("choose:")
        return choice

    def choose_action(self, choice, user_list):
        if choice == "1":
            print self.get_score()
        elif choice == "2":
            self.change_password()
        elif choice == "0":
            self.is_exit = True
        else:
            print "input error"
