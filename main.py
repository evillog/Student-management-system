import pickle
import sys
from admin import Admin


def main():

    user_list = load_data()

    print user_list

    current_user = None
    count = 3
    while current_user is None and count > 0:
        number, password = welcome_login()
        current_user = login(number, password, user_list)
        count -= 1

        while current_user is not None:
            current_user.show_menu()
            choice = current_user.choose_menu()
            current_user.choose_action(choice, user_list)

            save_data(user_list)
            exit_program()
    else:
        exit_program()


def load_data():
    fb = open('data.pkl', 'r')
    data = pickle.load(fb)
    user_list = data
    fb.close()
    return user_list


def save_data(user_list):
    fc = open('data.pkl', 'w')
    pickle.dump(user_list, fc)
    fc.close()


def welcome_login():
    print "Welcome to use the GMS"
    number = raw_input("Please enter your number: ")
    password = raw_input("Please enter your password: ")
    return number, password


def login(number, password, user_list):
    try:
        user_list[number].check_password(password)
    except KeyError:
        print "The account does not exist!"
        return None

    return user_list[number]


def choose_menu(user, user_list):
    user.show_menu(user_list)


def exit_program():
    print "Thank you for using it!"
    sys.exit(0)


if __name__ == '__main__':
    f = open('data.pkl', 'r').read()
    if len(f) == 0:
        admin_user = Admin('0', '0', {})
        user_dic = {'0': admin_user}
        info_file = open('data.pkl', 'w')
        pickle.dump(user_dic, info_file)
        info_file.close()
    main()





