from user import User
from teacher import Teacher
from student import Student


class Admin(User):
    def __init__(self, number, password, is_exit=False, user_list={}):
        User.__init__(self, number, password, is_exit)
        self.list = user_list

    def set_user_list(self, user_list):
        self.list = user_list

    def add_stu(self, stu_num, stu_psw):
        user_list = self.list

        new_stu = Student(stu_num, stu_psw)
        new_stu.set_number(stu_num)
        new_stu.set_password(stu_psw)
        user_list[stu_num] = new_stu

        self.set_user_list(user_list)

        print "Success!"

    def add_tea(self, tec_num, tec_psw):
        user_list = self.list

        new_tec = Teacher(tec_num, tec_psw)
        new_tec.set_number(tec_num)
        new_tec.set_password(tec_psw)
        user_list[tec_num] = new_tec
        self.set_user_list(user_list)

        print "Success!"

    def del_user(self, user_num):
        try:
            del self.list[user_num]
        except KeyError:
            print "The account does not exist!"
        print "deleted successfully!"

    @staticmethod
    def show_menu():
        print "1.query all students\n2.query all teachers\n3.add user\n4.delete user\n5.change password\n0.quit"

    @staticmethod
    def choose_menu():
        choice = raw_input("choose:")
        return choice

    def choose_action(self, choice, user_list):
        self.set_user_list(user_list)
        if choice == "1":
            self.query_all_student()
        elif choice == "2":
            self.query_all_teacher()
        elif choice == "3":
            self.add_user(user_list)
        elif choice == "4":
            self.query_all_user()
            user_num = raw_input("The number you want to delete: ")
            self.del_user(user_num)
        elif choice == "5":
            self.change_password()
        elif choice == "0":
            self.is_exit = True

        else:
            print "input error"

    def add_user(self, user_list):
        number = raw_input("Please enter your number: ")
        self.set_user_list(user_list)
        print self.list

        if number not in self.list:

            password = raw_input("Please enter your  password: ")
            choice = raw_input("Please choose your id (S-student/T-teacher/A-admin): ")

            if choice not in 'stST':
                print "Input error, please try again!"
            elif choice == 's' or choice == 'S':
                self.add_stu(number, password)
            elif choice == 't' or choice == 'T':
                self.add_tea(number, password)
        else:
            print "The number is already exists, please try another one!"
            self.add_user(user_list)

    def query_all_student(self):
        for each in self.list.itervalues():
            if isinstance(each, Student):
                self.show_student(each)

    def query_all_teacher(self):
        for each in self.list.itervalues():
            if isinstance(each, Teacher):
                self.show_teacher(each)

    def query_all_user(self):
        for each in self.list.itervalues():
            if (isinstance(each, Teacher)) or (isinstance(each, Student)):
                self.show_teacher(each)

    @staticmethod
    def show_student(stu):
        print 'Number: %s Score: %s' % (stu.get_number(), stu.get_score())

    @staticmethod
    def show_teacher(tec):
        print 'Number: %s' % tec.get_number()
