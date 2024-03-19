#class-class attributes, constructor, instance attributes,properties, class methods

#emptuy class

 class Customer:
  #class attributes
  name="Paul"
  gender= "Male"
  phone_number= "0114318200"
  email= "nkiprotich439@gmail.com"

  #class functions/methods
  def make_order():
   print("We have received your order! ")

  def make_payment():
   print("Thankyou, payment received. ")

  def rate_us():
   comment=input("Leave a comment: ")
   print(comment)

   #creating an instance of a class(object)
   #syntax
   #objectname=classname()
   customer_1= Customer()
   customer_1.name= "Benedict Kiprotich Ngetich"
   customer_1.gender="male"
   customer_1.email="nkiprotich439@gmail.com"
   
   #accessing the variable name using an object
   #print(objectname.variable name)i