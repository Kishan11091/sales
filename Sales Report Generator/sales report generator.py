from tkinter import *
import time
import datetime
import mysql.connector
from tkinter import ttk
import tkinter as tk
import csv
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from tkinter import messagebox

###
root = Tk()
root.geometry("1600x8000")
root.title("Sales Report Generator")
#database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Kishan@09",
    database="sales_report_generator"
)
my_cursor = mydb.cursor()

Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

# =================================================================================
#                  TIME
# ================================================================================
localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font=('castellar', 50, 'bold', 'underline'), text="SALES REPORT GENERATOR", fg="black", bd=10,
                anchor='w')
lblInfo.grid(row=0, column=0)

lblInfo = Label(Tops, font=('times new roman', 20, 'bold', 'underline'), text=localtime, fg="green", bd=10, anchor='w')
lblInfo.grid(row=1, column=0)

def Ref():

    if (apple.get() == ""):
        Coapple = 0
    else:
        Coapple = float(apple.get())

    if (mango.get() == ""):
        Comango = 0
    else:
        Comango = float(mango.get())

    if (orange.get() == ""):
        Coorange = 0
    else:
        Coorange = float(orange.get())

    if (toothbrush.get() == ""):
        Cotoothbrush = 0
    else:
        Cotoothbrush = float(toothbrush.get())

    if (toothpaste.get() == ""):
        Cotoothpaste = 0
    else:
        Cotoothpaste = float(toothpaste.get())

    if (Drinks.get() == ""):
        CoD = 0
    else:
        CoD = float(Drinks.get())

    if (chocolate.get() == ""):
        Coc = 0
    else:
        Coc = float(chocolate.get())

    if (soap.get() == ""):
        Cos = 0
    else:
        Cos = float(soap.get())
#COST PR
    ca = Coapple * 15
    cd = CoD * 10
    cm = Comango * 25
    co = Coorange * 20
    ctb = Cotoothbrush * 30
    ctp = Cotoothpaste * 10
    cc = Coc * 5
    cs = Cos * 10
#SELL PR
    Costofapple = Coapple * 25
    CostofDrinks = CoD * 20
    Costofmango = Comango * 35
    Costoforange = Coorange * 25
    Costtoothbrush = Cotoothbrush * 35
    Costtoothpaste = Cotoothpaste * 20
    Costofchocolate = Coc * 10
    Costofsoap = Cos * 20
    '(total cost)'
    Costofall = "Rs", str('%.2f' % (
                Costofchocolate + Costofapple + CostofDrinks + Costofmango + Costoforange + Costtoothbrush + Costtoothpaste + Costofsoap))
#chocolate, cold drinks are taxed at 28%
#household items like toothbrush, soap, toothpaste are taxed at 18%
#fruits are exempt from taxation
    PayTax = ((
        (Costofchocolate*0.28)+(CostofDrinks*0.28)+(Costtoothbrush*0.18)+(Costtoothpaste*0.18)+(Costofsoap*0.18)))

    TotalCost = (
                Costofapple + CostofDrinks + Costofmango + Costoforange + Costtoothbrush + Costtoothpaste + Costofchocolate + Costofsoap)
    profits = ((Costofapple - ca) + (CostofDrinks - cd) + (Costofmango - cm) + (Costoforange - co) + (
                Costtoothbrush - ctb) + (Costtoothpaste - ctp) + (Costofchocolate - cc) + (Costofsoap - cs))

    Ser_Charge = ((
                              Costofapple + CostofDrinks + Costofmango + Costoforange + Costtoothbrush + Costtoothpaste + Costofchocolate + Costofsoap) / 99)

    Service = "Rs", str('%.2f' % Ser_Charge)

    OverAllCost = "Rs", str('%.2f' % (PayTax + TotalCost + Ser_Charge))

    PaidTax = "Rs", str('%.2f' % PayTax)

    Profit = "Rs", str('%.2f' % (profits))

    Service_Charge.set(Service)
    Cost.set(Costofall)
    Tax.set(PaidTax)
    SubTotal.set(Costofall)
    Total.set(OverAllCost)
    profit.set(Profit)

    sql_command = "INSERT IGNORE INTO srgtable1(billno,apple,mango,orange,toothbrush,toothpaste,colddrinks,chocolate,soap) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (txtReference.get(), txtapple.get(), txtmango.get(), txtorange.get(), txttoothbrush.get(), txttoothpaste.get(),txtDrinks.get(), txtchoclate.get(), txtsoap.get())
    my_cursor.execute(sql_command, values)
    mydb.commit()
def qExit():
    root.destroy()

def Reset():
    rand.set("")
    apple.set("")
    mango.set("")
    orange.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    toothbrush.set("")
    toothpaste.set("")
    chocolate.set("")
    soap.set("")
    profit.set("")


rand = StringVar()
apple = StringVar()
mango = StringVar()
orange = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
toothbrush = StringVar()
toothpaste = StringVar()
chocolate = StringVar()
soap = StringVar()
profit = StringVar()

lblReference = Label(f1, font=('arial', 16, 'bold'), text="BILL NO", bd=16, anchor="w")
lblReference.grid(row=0, column=0)
txtReference = Entry(f1, font=('arial', 16, 'bold'), textvariable=rand, bd=10, insertwidth=4, bg="light pink",
                     justify='right')
txtReference.grid(row=0, column=1)

lblapple = Label(f1, font=('arial', 16, 'bold'), text="APPLE", bd=16, anchor="w")
lblapple.grid(row=1, column=0)
txtapple = Entry(f1, font=('arial', 16, 'bold'), textvariable=apple, bd=10, insertwidth=4, bg="light pink",
                 justify='right')
txtapple.grid(row=1, column=1)

lblmango = Label(f1, font=('arial', 16, 'bold'), text="MANGO", bd=16, anchor="w")
lblmango.grid(row=2, column=0)
txtmango = Entry(f1, font=('arial', 16, 'bold'), textvariable=mango, bd=10, insertwidth=4, bg="light pink",
                 justify='right')
txtmango.grid(row=2, column=1)

lblorange = Label(f1, font=('arial', 16, 'bold'), text="ORANGE", bd=16, anchor="w")
lblorange.grid(row=3, column=0)
txtorange = Entry(f1, font=('arial', 16, 'bold'), textvariable=orange, bd=10, insertwidth=4, bg="light pink",
                  justify='right')
txtorange.grid(row=3, column=1)

lbltoothbrush = Label(f1, font=('arial', 16, 'bold'), text="TOOTHBRUSH", bd=16, anchor="w")
lbltoothbrush.grid(row=4, column=0)
txttoothbrush = Entry(f1, font=('arial', 16, 'bold'), textvariable=toothbrush, bd=10, insertwidth=4, bg="light pink",
                      justify='right')
txttoothbrush.grid(row=4, column=1)

lbltoothpaste = Label(f1, font=('arial', 16, 'bold'), text="TOOTHPASTE", bd=16, anchor="w")
lbltoothpaste.grid(row=5, column=0)
txttoothpaste = Entry(f1, font=('arial', 16, 'bold'), textvariable=toothpaste, bd=10, insertwidth=4, bg="light pink",
                      justify='right')
txttoothpaste.grid(row=5, column=1)


lblDrinks = Label(f1, font=('arial', 16, 'bold'), text="COLD DRINKS", bd=16, anchor="w")
lblDrinks.grid(row=0, column=2)
txtDrinks = Entry(f1, font=('arial', 16, 'bold'), textvariable=Drinks, bd=10, insertwidth=4, bg="light pink",
                  justify='right')
txtDrinks.grid(row=0, column=3)

lblchoclate = Label(f1, font=('arial', 16, 'bold'), text="CHOCOLATE", bd=16, anchor="w")
lblchoclate.grid(row=1, column=2)
txtchoclate = Entry(f1, font=('arial', 16, 'bold'), textvariable=chocolate, bd=10, insertwidth=4, bg="light pink",
                    justify='right')
txtchoclate.grid(row=1, column=3)

lblsoap = Label(f1, font=('arial', 16, 'bold'), text="SOAP", bd=16, anchor="w")
lblsoap.grid(row=2, column=2)
txtsoap = Entry(f1, font=('arial', 16, 'bold'), textvariable=soap, bd=10, insertwidth=4, bg="light pink",
                justify='right')
txtsoap.grid(row=2, column=3)

lblprofit = Label(f1, font=('arial', 16, 'bold'), text="PROFIT", bd=16, anchor="w")
lblprofit.grid(row=3, column=2)
txtprofit = Entry(f1, font=('arial', 16, 'bold'), textvariable=profit, bd=10, insertwidth=4, bg="light pink",
                  justify='right')
txtprofit.grid(row=3, column=3)

lblCost = Label(f1, font=('arial', 16, 'bold'), text="COST", bd=16, anchor="w")
lblCost.grid(row=4, column=2)
txtCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cost, bd=10, insertwidth=4, bg="light pink",
                justify='right')
txtCost.grid(row=4, column=3)

lblService = Label(f1, font=('arial', 16, 'bold'), text="Service Charge", bd=16, anchor="w")
lblService.grid(row=5, column=2)
txtService = Entry(f1, font=('arial', 16, 'bold'), textvariable=Service_Charge, bd=10, insertwidth=4, bg="light pink",
                   justify='right')
txtService.grid(row=5, column=3)


lblStateTax = Label(f1, font=('arial', 16, 'bold'), text="State Tax", bd=16, anchor="w")
lblStateTax.grid(row=0, column=4)
txtStateTax = Entry(f1, font=('arial', 16, 'bold'), textvariable=Tax, bd=10, insertwidth=4, bg="light pink",
                    justify='right')
txtStateTax.grid(row=0, column=5)

lblSubTotal = Label(f1, font=('arial', 16, 'bold'), text="Sub Total", bd=16, anchor="w")
lblSubTotal.grid(row=1, column=4)
txtSubTotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=SubTotal, bd=10, insertwidth=4, bg="light pink",
                    justify='right')
txtSubTotal.grid(row=1, column=5)

lblTotalCost = Label(f1, font=('arial', 16, 'bold'), text="Total Cost", bd=16, anchor="w")
lblTotalCost.grid(row=2, column=4)
txtTotalCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4, bg="light pink",
                     justify='right')
txtTotalCost.grid(row=2, column=5)


def allsalesbutton():
    allsales= tk.Tk()
    allsales.title("All Sales")
    allsales.geometry("600x300")
    my_cursor.execute("SELECT * FROM srgtable1")
    tree= ttk.Treeview(allsales)
    tree['show']='headings'
    s= ttk.Style(allsales)
    s.theme_use("clam")
    s.configure(".", font=('Helvetica',11))
    s.configure("Treeview.Heading", foreground='Red')

    tree["columns"]=("billno", "apple", "orange","mango","toothbrush","toothpaste","colddrinks","chocolate","soap","subtotal")
    tree.column("billno", width=150, minwidth=150, anchor=tk.CENTER)
    tree.column("apple", width=150, minwidth=150, anchor=tk.CENTER)
    tree.column("orange", width=150, minwidth=150, anchor=tk.CENTER)
    tree.column("mango", width=150, minwidth=150, anchor=tk.CENTER)
    tree.column("toothbrush", width=150, minwidth=150, anchor=tk.CENTER)
    tree.column("toothpaste", width=150, minwidth=150, anchor=tk.CENTER)
    tree.column("colddrinks", width=150, minwidth=150, anchor=tk.CENTER)
    tree.column("chocolate", width=150, minwidth=150, anchor=tk.CENTER)
    tree.column("soap", width=150, minwidth=150, anchor=tk.CENTER)
    tree.column("subtotal", width=150, minwidth=150, anchor=tk.CENTER)

    tree.heading("billno",text="Bill No", anchor=tk.CENTER)
    tree.heading("apple",text="Apple", anchor=tk.CENTER)
    tree.heading("orange",text="Orange", anchor=tk.CENTER)
    tree.heading("mango",text="Mango", anchor=tk.CENTER)
    tree.heading("toothbrush",text="Toothbrush", anchor=tk.CENTER)
    tree.heading("toothpaste",text="Toothpaste", anchor=tk.CENTER)
    tree.heading("colddrinks", text="Cold Drinks", anchor=tk.CENTER)
    tree.heading("chocolate", text="Chocolate", anchor=tk.CENTER)
    tree.heading("soap",text="Soap", anchor=tk.CENTER)
    tree.heading("subtotal", text="Subtotal", anchor=tk.CENTER)

    i=0
    for x in my_cursor:
        tree.insert('',i,text="", values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9]))
        i= i+1
    tree.pack()

    hsb= ttk.Scrollbar(allsales, orient="horizontal")
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X,side=BOTTOM)
    tree.pack()

def pdf():
    pdf=SimpleDocTemplate("Sales Report.pdf")
    flow_obj=[]
    with open("Sales_Record.csv")as f1:
        csvdata=csv.reader(f1,delimiter=",")
        tdata=[]
        for row in csvdata:
            data=[]
            #print(row)
            billno=row[0]
            apple= row[1]
            mango = row[2]
            orange = row[3]
            toothbrush = row[4]
            toothpaste = row[5]
            colddrinks = row[6]
            chocolate = row[7]
            soap = row[8]
            subtotal = row[9]
            data.append( billno)
            data.append(apple)
            data.append(mango)
            data.append(orange)
            data.append( toothbrush)
            data.append(toothpaste)
            data.append(colddrinks)
            data.append(chocolate)
            data.append(soap)
            data.append(subtotal)
            tdata.append(data)
    t=Table(tdata)
    tstyle=TableStyle([("GRID", (0,0), (-1,-1),1,colors.black)])
    t.setStyle(tstyle)
    flow_obj.append(t)
    pdf.build(flow_obj)
    messagebox.showinfo(title='PDF Creator', message="Your PDF has been created successfully!")

#Function to export MySQL data into excel file
def export():
    my_cursor.execute("SELECT * FROM srgtable1")
    result=my_cursor.fetchall()
    column_names = [i[0] for i in my_cursor.description]
    fp = open('Sales_Record.csv','w')
    myFile = csv.writer(fp, lineterminator='\n')  # use lineterminator for windows
    myFile.writerow(column_names)
    myFile.writerows(result)
    fp.close()
    messagebox.showinfo(title='Export to excel', message="Your data has been exported to excel!")


# Buttons==========================================================================================
btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Total",
                  bg="green", command=Ref).grid(row=7, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Reset",
                  bg="orange", command=Reset).grid(row=7, column=2)

btnExit = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Exit", bg="red",
                 command=qExit).grid(row=7, column=3)

btnpdf = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Create PDF",
                  bg="springgreen",command=pdf).grid(row=7, column=5)
btnlist = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="List of all sales",
                  bg="cyan", command= allsalesbutton).grid(row=4, column=7)

btnexport = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Export to Excel",
                  bg="coral",command=export).grid(row=4, column=5)

root.mainloop()
