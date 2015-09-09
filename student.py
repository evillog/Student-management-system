import user


class Student(user.User):
    def __init__(self, number, password):
        user.User.__init__(self, number, password)
        self.score = 0

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def show_menu(self):
        print "1.query score"
        print "0.quit"

    def choose_menu(self):
        choice = raw_input("choose:")
        return choice

    def choose_action(self, choice, user_list):
        if choice == "1":
            print self.get_score()
        elif choice == "0":
            pass
        else:
            print "input error"
