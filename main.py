from pyscript import display, document

student_type = False #bool
coun = ["Japan, South Korea, Switzerland"] #list
fru = {"manggo", "grape", "banana", "apple", "strawberry"} #set
me = {"name" : "Full name: Zara Giele C. Llaguno",
     "age" : "Age: 16",
     "height" : "My height: 171 cm",
     "color" : "My favorite colors: black and white",
     "shoe" : "My shoe size: 9",
     "friend" : "My bestfriend is Kailey",
     "car" : "My car brands: Toyota and Ford",
     } #dict
week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday") #tuple



display("I wanna go to:", coun[0], target="div1") #displays in div1
display (fru, target="div1")
display(me["name"], me["height"], me["age"], me["color"], me["shoe"], me["friend"], me["car"], target="div1")
display(week, target="div1")
display("New student:", student_type, target="div1")

def get_numbers(): #to insert the numbers
    n1 = float(document.getElementById("n1").value)
    n2 = float(document.getElementById("n2").value)
    return n1, n2

def add(event): #adds numbers
    n1, n2 = get_numbers()
    document.getElementById("Result").innerHTML = ""  # clear it first
    display(f"Result: {n1 + n2}", target="Result")

def subtract(event): #subtracts numbers
    n1, n2 = get_numbers()
    document.getElementById("Result").innerHTML = ""  
    display(f"Result: {n1 - n2}", target="Result")

def multiply(event): #subtracts numbers
    n1, n2 = get_numbers()
    document.getElementById("Result").innerHTML = ""
    display(f"Result: {n1 * n2}", target="Result")

def divide(event): #divides numbers
    n1, n2 = get_numbers()
    document.getElementById("Result").innerHTML = ""
    display(f"Result: {n1 / n2}", target="Result")
