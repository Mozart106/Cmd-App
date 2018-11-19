
import datetime


'''
    comments = [
        {"comment_id": 1, "user_id": 1, "message": "Hi there", "timestamp": "9.00"}

    ]

    def __init__(self, user_id, username, role, login=False, lastLoggedInAt=False)
    self.user_id = user_id
    self.username = username
    self.lastLoggedInAt = lastLoggedInAt

    def comment(self):
        pass

    def moderator(self):
        pass

    def admin(self):
        pass


class Comment(object):
	coments=[]

    def __init__(self, comment_id, user_id, message, timestamp):
        self.comment_id = comment_id
        self.user_id = user_id
        self.message = message
        self.timetamp = timestamp


class Reply(Comment):

    def __init__(self, reply):
        self.reply = reply

'''


class User(object):
    users = [
        {"user_id": 1, "username": "Rachel", "password": "rachel", "login": False,
            "role": "normal", "lastLoggedInAt": True},
        {"user_id": 2, "username": "Mark", "password": "mark", "login": False,
            "role": "moderator", "lastLoggedInAt": True},
        {"user_id": 3, "username": "Sam", "password": "sam", "login": False,
            "role": "admin", "lastLoggedInAt": True},
    ]
    comments=[]


class Login(User):

    def login(self):
        # Login
        data = []
        username = input("Username: ")
        password = input("Password: ")
     
        user = next((luser for luser in self.users if
         luser["username"] == username and luser["password"] == password), None)



        if user["role"] == "normal":
            print("You are logged in as " + user["role"])
            message = input("Comment: ")

            comment = {
                "username": user["username"],
                #"login": login,
                "role": user["role"],
                "timestamp": datetime.datetime.now().timestamp(),
                "message": message
            }
            data.append(comment)

            
            message = input("Enter comment to edit: ")
            
            for s in self.comments:
                if s["message"] == message:
                    edit = input("Enter edited comment: ")
                    s["message"] == edit

                print("Edited comment: " + edit)

        elif user["role"] == "moderator":
            print("You are logged in as " + user["role"])
            message = input("Message: ")

            payload = {
                "username": user["username"],
                #"login": login,
                "role": user["role"],
                "timestamp": datetime.datetime.now().timestamp(),
                "message": message
            }
            data.append(payload)

            action = input("Delete comment? y/n")
            if action == "y":
                for d in data:
                    #data.pop()
                    print("Message deleted")


            for d in data:
                message = input("Edit comment ")
                d["message"] == message
                        
                print("Edited message: " + message)
        elif user["role"] == "admin":
            print("You are logged in as " + user["role"])
            message = input("Message: ")

            payload = {
                "username": user["username"],
                #"login": login,
                "role": user["role"],
                "timestamp": datetime.datetime.now().timestamp(),
                "message": message
            }
            data.append(payload)

            action = input("Delete comment? y/n")
            if action == "y":
                for d in data:
                    #data.pop()
                    print("Message deleted")
                    

            for d in data:
                message = input("Edit comment ")
                d["message"] == message
                        
                print("Edited message: " + message)

            return "Username or password incorrect"
        return data
        #com = Comment()
        # com.create_comment()



cl = Login()
cl.login()