class grandparents(object):
    def __init__(self,grandpaname,grandmaname,familyname):
        self.grandfathername=grandpaname
        self.grandmothername=grandmaname
        self.familyname=familyname

    def welcome(self):
          return "welcome to",self.familyname,"wishes from",self.grandfathername,"and",self.grandmothername



class mkazhagiri(grandparents):
     def __init__(self,grandpaname,grandmaname,familyname,fathername,mothername):
          self.fathername=fathername
          self.mothername=mothername
          super().__init__(grandpaname,grandmaname,familyname)
     def thanks(self):
          print("hi....!grandpa",self.grandfathername,"and",self.grandmothername,"we",self.fathername,"and",self.mothername,"thankyou for warm welcome to our",self.fathername,"family")

class dhayanithi(mkazhagiri):
     def welcome(self):
          return super().welcome()

x=dhayanithi(input("enter the grandpa name    :"),input("enter the grandma name   :"),input("enter the family name    :"),input("enterthe father name    :"),input("enter the mother name    :"))
print(x.welcome())
x.thanks()