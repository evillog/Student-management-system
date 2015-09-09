import user
import student


class Teacher(user.User):
    def __init__(self, number, password):
        user.User.__init__(self, number, password)

    def change_score(self, stu_num, score, user_list):
        print user_list
        stu = user_list[stu_num]
        if stu_num not in user_list:
            print"The student is not in the list!"

        stu.set_score(score)

    def query_all_stu(self, user_list):
        for each in user_list.itervalues():
            if isinstance(each, student.Student):
                show_stu_score(each)

    def show_menu(self):
        print "1.add/change student's score"
        print "2.query all student's score"
        print "0.quit"

    def choose_menu(self):
        choice = raw_input("choose:")
        return choice

    def choose_action(self, choice, user_list):
        if choice == "1":
            stu_num = raw_input("The number of the student you want to change: ")
            score = raw_input("Please input your new score: ")
            self.change_score(stu_num, score, user_list)
            print "Add score success!"
        elif choice == "2":
            self.query_all_stu(user_list)
        elif choice == "0":
            pass
        else:
            print "input error"


def show_stu_score(stu):
    print 'Number: %s Score: %s' % (stu.get_number(), stu.get_score())
