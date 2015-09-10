from user import User
import student


class Teacher(User):
    def __init__(self, number, password, is_exit=False):
        User.__init__(self, number, password, is_exit)

    @staticmethod
    def change_score(stu, score):
        try:
            stu.score = score
            print "Add score success!"
        except ValueError:
            print "Negative value not allowed"

    def query_all_stu(self, user_list):
        for each in user_list.itervalues():
            if isinstance(each, student.Student):
                self.show_stu_score(each)

    @staticmethod
    def show_menu():
        print "1.add/change student's score\n2.query all student's score\n3.change password\n0.quit"

    @staticmethod
    def choose_menu():
        choice = raw_input("choose:")
        return choice

    def choose_action(self, choice, user_list):
        if choice == "1":
            stu_num = raw_input("The number of the student you want to change: ")
            try:
                stu = user_list[stu_num]
                score = raw_input("Please input your new score: ")
                self.change_score(stu, score)
            except KeyError:
                print"The student is not in the list!"
                self.choose_action("1", user_list)
        elif choice == "2":
            self.query_all_stu(user_list)
        elif choice == "3":
            self.change_password()
        elif choice == "0":
            self.is_exit = True
        else:
            print "input error"

    @staticmethod
    def show_stu_score(stu):
        print 'Number: %s Score: %s' % (stu.get_number(), stu.get_score())
