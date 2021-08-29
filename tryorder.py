from tkinter import *
from functools import partial

root = Tk()

root.geometry('500x500')
root.title("Invoice Generator")


   

def gen_win(item_list):
    

    l3=Label(f2,text="Your Items")
    l3.pack()
    for i in range(len(item_list)):
        l=Label(f2,text=item_list[i])
        l.pack()
        global v
        global v1
        v=StringVar()
        v1=StringVar()
        
        quality=Entry(f2,textvariable=v)
        amount=Entry(f2,textvariable=v1)
        quality.pack()
        amount.pack() 


def gen_invoice(bill,total):
    bill.append(int(v.get())*int(v1.get()))
    for i in bill:
        total =total+ i
    l1=Label(f3,text=str(total))
    l1.pack()
    for widgets in f2.winfo_children():
      widgets.destroy()
    
    
def add_items():
    item_list=[]
    flag=False
    res=lb.curselection()
    if res[0]==5:
        res_all=lb.get(0,4)
        l1=list(res_all)
        flag=True
        
    elif res[0]==0:
        item_list.append("bread")
    elif res[0]==1:
        item_list.append("Milk")
        
    elif res[0]==2:
        item_list.append("Meat")
        
    elif res[0]==3:
        item_list.append("Cheese")
        
    elif res[0]==4:
        item_list.append("Vegetables")

    if flag==False:   
        gen_win(item_list)
    else:
        gen_win(l1)
    
f1=Frame(root,padx=10)
f1.grid(row=0)

l1=Label(f1,text="Select Items",font="Arial 17 bold",padx=20)
l1.pack()
lb=Listbox(f1,width=14,height=6,font="Arial 12")
lb.insert(0,"Bread")  
lb.insert(1, "Milk")  
lb.insert(2, "Meat")  
lb.insert(3, "Cheese")
lb.insert(4, "Vegetables") 
lb.insert(5, "All of the above")
lb.pack()

bt=Button(f1,text="Add Items",command=add_items)
bt.pack(side=BOTTOM,pady=10)

f3=Frame(root)
f3.grid(row=1,column=4)
bill = []
total = 0
f2=Frame(root)
f2.grid(row=1)
bt=Button(f3,text="Generate Bill",command=partial(gen_invoice,bill,total))
bt.pack(side=BOTTOM)
root.mainloop()
 
