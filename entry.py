import re
import datetime


def ask_for_name(name_type):       # for name
    while True:
        name = input(f"{name_type} name: ")
        if name.isalpha():
            break
        else:
            print("_______what you entered can't be accepted, enter alphabetical name_______")
            continue
    return name


def ask_for_email():       # for email
    while True:
        email = input("please enter your email: ")
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        # if "@" in email and "." in email:
        if re.fullmatch(pattern, email):
            break
        else:
            print("--------this email isn't valid--------")
            continue
    return email


def ask_for_password():        # for password
    while True:
        password = input("password: ")
        if len(password) >= 8:
            while True:
                password_again = input("enter same password again to confirm it: ")
                if password_again == password:
                    break
                else:
                    print("______what you entered can't be accepted (not same password)_______")
                    continue
            break
        else:
            print("________please enter password for at least a length of 8______ ")
            continue
    return password


def ask_for_phone():         # for phone number
    while True:
        phone = input("phone number: ")
        if phone.isdigit():
            # if (phone[:6] == "002010" or phone[:6] == "002011" or phone[:6] == "002012") and len(phone) == 14:
            pattern = r"^01[0125][0-9]{8}$"
            if re.match(pattern, phone):
                break
            else:
                print("____the phone number should be in format 01(0/1/2/3/5)******** with total length of 14 ")
                continue
        else:
            print("_____what you entered isn't a valid phone number______")
            continue
    return phone


def ask_for_title():        # for title of project
    while True:
        title = input("please enter the title of the project: ")
        if title.isalpha():
            break
        else:
            print("______what you entered can't be accepted, enter alphabetical name_______")
            continue
    return title


def ask_for_details():       # for details of project
    while True:
        details = input("please enter the details of the project: ")
        if details.isalpha():
            break
        else:
            print("______what you entered can't be accepted, enter alphabetical name_______")
            continue
    return details


def ask_for_target():          # for total target of project
    while True:
        total_target = input("please enter the total target of the project: ")
        if total_target.isdigit() and int(total_target) > 0:
            break
        else:
            print("_______the total target should be a number_______")
            continue
    return total_target


def ask_for_date(date_type):      # for {type} date of project
    while True:
        try:
            date = input(f"please enter the {date_type} time of the project: ")
            if date == datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%d'):
                break
            break
        except Exception:
            print("______please enter the date in the format YY-mm-dd _____")
            continue
    return date
