from pyscript import display

display("Specify the data types below", target= "div1")

a = "Doomsday" #str
b = 2026 #int
c = 3.14 #float
student_type = True #bool
e = ["Japan, South Korea, Switzerland"] #list
f = (1, 2, 3) #tuple
g = {"manggo", "grape", "banana"} #set
h = {"name" : "Full name: Zara Giele C. Llaguno",
     "age" : "Age: 16",
     "height" : "My height: 171 cm",
     "color" : "My favorite colors: black and white",
     "shoe" : "My shoe size: 9",
     "friend" : "My ",

     } #dict
week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

#display in div1
display(type(a), target="div1")
display(type(b), target="div1")
display(type(c), target="div1")
display(type(student_type), target="div1")
display(type(e), target="div1")
display(type(f), target="div1")
display(type(g), target="div1")
display(type(h), target="div1")

display("I wanna go to:", e[0])
display (g)
display(h["name"], h["height"], h["age"])
display(week)
