from tkinter import *
import datetime

# List:
entreeList = ["Burger($3.25)", "Chicken(4.75)", "Fish($4.50)"]
sideList = ["Fries($1.75)", "Salad(2.00)", "No side"]
drinkList = ["Coke($1.75)", "Sweet tea(2.00)", "Water(no charge)"]

# Function:


def compute():
    name = myNameString.get()

    entree = myEntreeList.curselection()
    side = mySideList.curselection()
    drink = myDrinkList.curselection()

    if entree[0] == 0:
        entreeCost = 3.25
    elif entree[0] == 1:
        entreeCost = 4.75
    elif entree[0] == 2:
        entreeCost = 4.5

    if side[0] == 0:
        sideCost = 1.75
    elif side[0] == 1:
        sideCost = 2
    elif side[0] == 2:
        sideCost = 0

    if drink[0] == 0:
        drinkCost = 1.75
    elif drink[0] == 1:
        drinkCost = 2
    elif drink[0] == 2:
        drinkCost = 0

    totalCost = entreeCost + sideCost + drinkCost
    myTotalString.set("%.2f" % totalCost)

    # Receipt:
    d = datetime.datetime.today()

    print("==============================")
    print("---KHOI'S FAMILY RESTAURANT---")
    print()
    print("Date:", d.strftime("%d-%B-%Y"))
    print("Time:", d.strftime("%H:%M:%S"))
    print()

    print("RECEIPT FOR PURCHASE")
    print()
    print("Customer:", name.upper())
    print()

    print("ITEMS:")
    print(entreeList[entree[0]])
    print(sideList[side[0]])
    print(drinkList[drink[0]])
    print()

    print("Total: $", "%.2f" % totalCost, sep="")
    print("==============================")
    print()

    # Append to a file:
    outfile = open("restaurantData.csv", "a")

    outfile.write(d.strftime("%d-%B-%Y") + ",")
    outfile.write(d.strftime("%H:%M:%S") + ",")
    outfile.write(name.upper() + ",")
    outfile.write(entreeList[entree[0]] + ",")
    outfile.write(sideList[side[0]] + ",")
    outfile.write(drinkList[drink[0]] + ",")
    outfile.write("%.2f" % totalCost + "\n")

    outfile.close()


# Window:
window = Tk()
window.title("Online Food Ordering")
window.minsize(300, 200)
# window.geometry("550x270")
window.configure(bg="light blue")

# Label:
myLabel1 = Label(window, text="Khoi's Family Restaurant",
                 fg="black", font="Arial 20 bold", justify="center")
myLabel1.grid(row=0, column=0, columnspan=3, padx=0, pady=10)

myLabel2 = Label(window, text="ENTREE:", fg="black")
myLabel2.grid(row=1, column=0, padx=0, pady=10)

myLabel3 = Label(window, text="SIDE:", fg="black")
myLabel3.grid(row=1, column=1, padx=0, pady=10)

myLabel4 = Label(window, text="DRINK:", fg="black")
myLabel4.grid(row=1, column=2, padx=0, pady=10)

myLabel5 = Label(window, text="TOTAL:", fg="black")
myLabel5.grid(row=4, column=0, padx=10, pady=15)

myLabel6 = Label(window, text="NAME:", fg="black")
myLabel6.grid(row=5, column=0, padx=10, pady=15)

# List:
entreeString = StringVar()
myEntreeList = Listbox(window, listvariable=entreeString,
                       exportselection=0, width=17, height=3)
myEntreeList.grid(row=2, column=0, padx=10, pady=10)
entreeString.set(entreeList)

sideString = StringVar()
mySideList = Listbox(window, listvariable=sideString,
                     exportselection=0, width=17, height=3)
mySideList.grid(row=2, column=1, padx=10, pady=10)
sideString.set(sideList)

drinkString = StringVar()
myDrinkList = Listbox(window, listvariable=drinkString,
                      exportselection=0, width=17, height=3)
myDrinkList.grid(row=2, column=2, padx=10, pady=10)
drinkString.set(drinkList)

# Button:
myButton = Button(window, text="Add to the order",
                  bg="yellow", command=compute)
myButton.grid(row=3, column=1, padx=10, pady=15)

# Entry:
myTotalString = StringVar()
myTotal = Entry(window, state="readonly", textvariable=myTotalString)
myTotal.grid(row=4, column=1)

myNameString = StringVar()
myName = Entry(window, textvariable=myNameString)
myName.grid(row=5, column=1)

# Mainloop:
window.mainloop()
