class google():
    def __init__(self):
        print("welcome to google chrome")
    def google_account(self,username,password):
        print("enter the username",username,"enter the password",password)
    def search_bar(self,title):
        print("enter the title",title)
    def software(self,software):
        print("enter the software name")   
class email(google):
    
    def login(self):
        print("you can login gmail")
    def compose(self):
        print("you can compose and sent mail")
    def inbox(self):
        print("you can reciving the mail")
class browser(email):
    def __init__(self):
        super().__init__()
        super().google_account()
        super().search_bar()
        super().software()
        super().login()
        super().compose()
        super().inbox()

b=browser()