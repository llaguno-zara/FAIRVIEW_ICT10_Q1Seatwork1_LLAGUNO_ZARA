from pyscript import display

display("Specify the data types below", target= "div1")

a = "Doomsday" #str
b = 2026 #int
c = 3.14 #float
d = True #bool
e = ["Spiderman: Brand New Day", "Avengers: Eng Game", "X-Men"] #list
f = (1, 2, 3) #tuple
g = {"keyboard", "monitor", "mouse"} #set
h = {"name" : "Zara",
     "age" : 15,
     "desc" : "sir ramos' favorite"} #dict

#display in div1
display(type(a), target="div1")
display(type(b), target="div1")
display(type(c), target="div1")
display(type(d), target="div1")
display(type(e), target="div1")
display(type(f), target="div1")
display(type(g), target="div1")
display(type(h), target="div1")

display("My favorite movie is", e[0])
display("keyboard", in g)
display(h["name"], h["desc"])