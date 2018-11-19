
import datetime


class User(object):
    users = [
        {"user_id": 1, "username": "Rachel", "password": "rachel", "login": False,
            "role": "normal", "lastLoggedInAt": True},
        {"user_id": 2, "username": "Mark", "password": "mark", "login": False,
            "role": "moderator", "lastLoggedInAt": True},
        {"user_id": 3, "username": "Sam", "password": "sam", "login": False,
            "role": "admin", "lastLoggedInAt": True},
    ]



class Login(User):

    def login(self):
        # Login
        data = []
        username = input("Username: ")
        password = input("Password: ")
     
        user = next((luser for luser in self.users if
         luser["username"] == username and luser["password"] == password), None)
        



        if user["role"] == "normal":
            print("You are logged in as a " + user["role"] + " user")
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

            
            for s in data:
                if s["message"] == message:
                    edit = input("Enter New comment: ")
                    s["message"] == edit
                

                    print("Edited comment: " + edit)
                    print ("User logged out\n")
                    cl = Login()
                    cl.login()

                else: print ("Comment not found")
                print ("User logged out \n")
                cl = Login()
                cl.login()


        elif user["role"] == "moderator":
            print("You are logged in as " + user["role"])
            message = input("Comment: ")

            payload = {
                "username": user["username"],
                #"login": login,
                "role": user["role"],
                "timestamp": datetime.datetime.now().timestamp(),
                "message": message
            }
            data.append(payload)

            action = input("Delete comment? y/n: \n")
            if action == "y":
                for d in data:
                  
                    print("Message deleted")


            else: 
                for d in data:
                    message = input("Edit comment ")
                    d["message"] == message
                            
                    print("Edited message: " + message)
                    print ("User logged out\n")
                    cl = Login()
                    cl.login()
               

        elif user["role"] == "admin":
            print("You are logged in as " + user["role"])
            print ("All comments: ")
            print (data)
            


            action = input("Delete comment? y/n: \n")
            message = input("Comment to delete: ")
            if action == "y":
                for d in data:
                    if d["message"] == message:
                        print("Comment  deleted")

                print ("Comment not found")
                print ("User logged out \n")
                cl = Login()
                cl.login()
  
cl = Login()
cl.login()