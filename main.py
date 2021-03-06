from getpass import getpass
from edulink import provisioning, school_details, login

school_code = input("Enter school code:\t")
server = provisioning.server(school_code)

school = school_details.school(school_code)

if __name__ == "__main__":
    usr = input("usr:\t")
    pwd = getpass("pwd:\t")
    try:
        user = login.login(server, usr, pwd)
        print(user.Pupil.avatar.width)
        print(user.Pupil.avatar.height)
    except Exception as e:
        print(e)
