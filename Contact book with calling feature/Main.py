#!/usr/bin/env python
# coding: utf-8

# In[372]:

#CONTACT BOOK WITH CALLING FEATURE, SQL AND GUI
#SUBMITTED BY- KANIKA JOSHI


import sqlite3
con=sqlite3.connect("contacts.db")
con.execute('''CREATE TABLE IF NOT EXISTS contacts (NAME TEXT PRIMARY KEY NOT NULL, PHNO INT NOT NULL); ''')


# In[373]:


import tkinter as tk
from tkinter.font import BOLD
from tkinter import messagebox
import os
from time import sleep
from tkinter.constants import RIGHT, Y


# In[374]:


#.........................to check db for entries................................

def check(name):

    a= con.execute("SELECT NAME FROM contacts")
    for row in a:
        if row[0]==name:
            return True
    return False


# In[375]:


# ..................................add contact...............................................

def add(name, phno):
    
        data=(name, phno)
        sql = 'insert into contacts (NAME, PHNO) values(?,?)'
           
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        proceed()

        
def Add() :
    
    global awindow
    awindow = tk.Tk()
    awindow.configure(bg="#FFE4B5")
    awindow.geometry("400x350")
    awindow.title("Contacts")

    head = tk.Label(awindow, text="\nAdd New Contacts\n", font=("Arial", 20),bg="#FFE4B5").pack()
        
    
    def to_add() :
        name=nametk.get()
        
        if name=="" or name.isspace()==True:
            tk.messagebox.showwarning("Warning", "Name cannot be empty!!")
        
        elif check(name)==True:
            tk.messagebox.showwarning("Warning", "Contact with same name already exists!!")
                    
        else:       
            try:

                tphno=phnotk.get()
                l=len(tphno)
                phno=int(tphno)

                if l==10:
                    tk.messagebox.showinfo("Information", "Contact added successfully!!")
                    awindow.destroy()
                    add(name,phno)
                else:
                    tk.messagebox.showwarning("Warning", "Phone No must be of 10 digits!!")

            except:
                tk.messagebox.showwarning("Warning", "Phone No must be a 10 digit Integer!!")

                
    def back3() :
        awindow.destroy()
        proceed()
        

    l_2 = tk.Label(awindow, text="Name ",bg="#FFE4B5").place(x=70, y=150)
   
    nametk = tk.Entry(awindow, fg='blue', bg="white", width=30)
    nametk.place(x=140, y=150)
    
    
    l_4 = tk.Label(awindow, text="Phone no ",bg="#FFE4B5").place(x=70, y=200)
    
    phnotk = tk.Entry(awindow, fg='blue', bg="white", width=30)
    phnotk.place(x=140, y=200)

    Submit = tk.Button(awindow, text="Submit", bg="green", fg="white", command=to_add).place(x=190, y=300)
    
    back3_button = tk.Button(text="Back", bg="blue", fg="white", height=1, width=10, command=back3)
    back3_button.place(x=280,y=300)

    awindow.mainloop()


# In[376]:


# ..................................remove contact...............................................

def remove(nname):
        a="DELETE FROM contacts WHERE NAME=?"
        data=(nname,)
        c=con.cursor()
        c.execute(a,data)
        con.commit()
        proceed()
        
def Remove():
    
    global rwindow
    rwindow = tk.Tk()
    rwindow.geometry("400x350")
    rwindow.configure(bg="#FFE4B5")
    rwindow.title("Contacts")

    head = tk.Label(rwindow, text="\nDelete Contact\n", font=("Arial", 20),bg="#FFE4B5").pack()

        
    def to_rem() :
    
        name=nametk.get()     
            
        if check(name)==False:
            tk.messagebox.showwarning("Warning", "Contact does not exist!!")
        
        else:
            x=tk.messagebox.askyesno("Delete Contact", "Are you sure you want to delete {}'s details permanently?".format(name))
            if x==True:
                tk.messagebox.showinfo("Information", "Contact removed successfully!!")
                rwindow.destroy()
                remove(name)
            else:
                pass
            
                
    def back3() :
        rwindow.destroy()
        proceed()
        
    l_1 = tk.Label(rwindow, text=" Name ",bg="#FFE4B5").place(x=70, y=100)
    
    nametk = tk.Entry(rwindow, fg='blue', bg='white', width=30)
    nametk.place(x=140, y=100)

    Delete = tk.Button(rwindow, text="Delete", bg="green", fg="white", command=to_rem).place(x=190, y=300)
    
    back3_button = tk.Button(text="Back", bg="blue", fg="white", height=1, width=10, command=back3)
    back3_button.place(x=280,y=300)

    rwindow.mainloop()


# In[377]:


# ..................................update contact...............................................

def promote(tname,nname,nphno):
    
        a="UPDATE contacts set NAME=?, PHNO=? WHERE NAME=?"
        data=(nname, nphno, tname)
        c=con.cursor()
        c.execute(a,data)
        con.commit()
        print("Phone no changed successfully")
        
        proceed()
        


def Promote():
    
    global pwindow
    pwindow = tk.Tk()
    pwindow.geometry("550x450")
    pwindow.configure(bg="#FFE4B5")
    pwindow.title("Contacts")

    head = tk.Label(pwindow, text="\nUpdate Contact\n", font=("Arial", 20),bg="#FFE4B5").pack()
                
    def to_proceed() :
        pwindow.destroy()
        proceed()
        
    def back3() :
        pwindow.destroy()
        proceed()
    
    def display(name):
        a="SELECT * FROM contacts WHERE NAME=?"
        data=(name,)
        c=con.cursor()
        x=c.execute(a,data)
       
        for i in x:            
            name=i[0]
            phno=i[1]
            return name,phno
        
    def to_dispns() :
        
        name=tnametk.get()     
                   
        if check(name)==False:
            
            tk.messagebox.showwarning("Warning", "Contact does not exist!!")
            
        else:
            nametk,phnotk=display(name)

            l_2 = tk.Label(text="Current Name: " + nametk,bg="#FFE4B5").place(x=70, y=150)

            l_3 = tk.Label(text="Current Phone no: " + str(phnotk),bg="#FFE4B5").place(x=70, y=200)            

            l_4 = tk.Label(pwindow, text="Enter New Name ",bg="#FFE4B5").place(x=70, y=260)

            nnametk = tk.Entry(pwindow, fg='blue', bg='white', width=30)
            nnametk.place(x=200, y=260)

            l_5 = tk.Label(pwindow, text="Enter New Phone No ",bg="#FFE4B5").place(x=70, y=310)

            nphnotk = tk.Entry(pwindow, fg='blue', bg='white', width=30)
            nphnotk.place(x=200, y=310)
    
        
            def to_change():
                tname=tnametk.get()
                name=nnametk.get()
                
                if name=="" or name.isspace()==True:
                    
                    tk.messagebox.showwarning("Warning", "Name cannot be empty!!")
                    

                elif check(name)==True:
                    
                    tk.messagebox.showwarning("Warning", "Contact with same name already exists!!")
                    
                
                else:
                    
                    try:
                        phno=nphnotk.get()
                        l=len(phno)
                        phno=int(phno)
                        
                        if l==10:
                            tk.messagebox.showinfo("Information", "Contact updated successfully!!")    
                            pwindow.destroy()
                            promote(tname,name,phno)
                        else:
                            tk.messagebox.showwarning("Warning", "Phone No must be of 10 digits!!")

                    except:
                        
                        tk.messagebox.showwarning("Warning", "New Phone No must be a 10 digit integer only!!")



        
            Submit = tk.Button(pwindow, text="Update", bg="green", fg="white", command=to_change).place(x=100, y=360)
        
            
    
    
    l_1 = tk.Label(pwindow, text="Enter Name: ",bg="#FFE4B5").place(x=70, y=100)
    
    tnametk = tk.Entry(pwindow, fg='blue', bg='white', width=30)
    tnametk.place(x=140, y=100)

    
    Ok = tk.Button(pwindow, text="OK", bg="green", fg="white", command=to_dispns).place(x=350, y=100)
    
    back3_button = tk.Button(text="Back", bg="blue", fg="white", height=1, width=10, command=back3)
    back3_button.place(x=400,y=100)

    pwindow.mainloop()


# In[378]:


# ..................................display contact...............................................

def Display():
    
    global dnwindow
    dnwindow = tk.Tk()
    dnwindow.geometry("400x350")
    dnwindow.configure(bg="#FFE4B5")
    dnwindow.title("Contacts")
    
    
    head = tk.Label(dnwindow, text="\nSearch Contact\n", font=("Arial", 20),bg="#FFE4B5").pack()
                
    def back3() :
        dnwindow.destroy()
        proceed()

    def display(name):
        a="SELECT * FROM contacts WHERE NAME=?"
        data=(name,)
        c=con.cursor()
        x=c.execute(a,data)
       
        for i in x:
            
            name=i[0]
            phno=i[1]
            
            return phno
        
    def to_disp() :
        name=nametk.get()
        
        if check(name)==False:
            
            tk.messagebox.showwarning("Warning", "No contact with this name!!The system is case sensitive.")
        
    
        else:

            phno=display(name)
    
            l_4 = tk.Label(text="Phone No: " + str(phno),bg="#FFE4B5").place(x=70, y=150)
            

    
    l_1 = tk.Label(dnwindow, text="Enter Name: ",bg="#FFE4B5").place(x=70, y=100)
    
    nametk = tk.Entry(dnwindow, fg='blue', bg='white', width=30)
    nametk.place(x=150, y=100)
    
    Ok = tk.Button(dnwindow, text="OK", bg="green", fg="white", command=to_disp).place(x=190, y=300)
    
    back3_button = tk.Button(text="Back", bg="blue", fg="white", height=1, width=10, command=back3)
    back3_button.place(x=280,y=300)
    
    dnwindow.mainloop()


# In[379]:


# ..................................call contact using name...............................................

def CallName():
    
    global cnwindow
    cnwindow = tk.Tk()
    cnwindow.geometry("500x400")
    cnwindow.configure(bg="#FFE4B5")
    cnwindow.title("Contacts")

    head = tk.Label(cnwindow, text="\nCall using Name\n", font=("Arial", 20),bg="#FFE4B5").pack()
                
    def to_proceed() :
        cnwindow.destroy()
        proceed()
        
    def back3() :
        cnwindow.destroy()
        Call()
    
    def display(name):
        a="SELECT * FROM contacts WHERE NAME=?"
        data=(name,)
        c=con.cursor()
        x=c.execute(a,data)
       
        for i in x:            
            name=i[0]
            phno=i[1]
            return name,phno   
    
    def to_dispns() :
        
        name=tnametk.get()     
                   
        if check(name)==False:
            
            tk.messagebox.showwarning("Warning", "Contact does not exist!!")
            
        else:
            nametk,phnotk=display(name)

            l_3 = tk.Label(text="Phone no: " + str(phnotk),bg="#FFE4B5").place(x=50, y=250)           
            
        
            def to_ncall():
                x=tk.messagebox.askyesno("Call", "Are you sure you want to call {}?".format(name))
                
                if x==True:
                    tk.messagebox.showinfo("Calling....", "Call to {} will start after you press ok".format(name))
                    os.system(f'cmd /k "adb shell am start -a android.intent.action.CALL -d tel:{phnotk}"')
                    os.system(f'cmd /k "adb kill-server"')
                    cnwindow.destroy()
                    Call()
                else:
                    pass

                            
            
            Submit = tk.Button(cnwindow, text="CALL", bg="#DC143C", fg="white", command=to_ncall).place(x=100, y=300)
        
                
            

    
    l_1 = tk.Label(cnwindow, text="Enter Name: ",bg="#FFE4B5").place(x=50, y=100)
    
    tnametk = tk.Entry(cnwindow, fg='blue', bg='white', width=30)
    tnametk.place(x=120, y=100)

    
    Ok = tk.Button(cnwindow, text="OK", bg="green", fg="white", command=to_dispns).place(x=330, y=100)
    
    back3_button = tk.Button(text="Back", bg="blue", fg="white", height=1, width=10, command=back3)
    back3_button.place(x=380,y=100)

    head3 = tk.Label(cnwindow, text="\nNote: Your phone must be connected with USB\n",bg="#FFE4B5")
    head3.place(x=100,y=140)
    
    head4= tk.Label(cnwindow, text="\nNote: Your system must have ADB connect service\n",bg="#FFE4B5")
    head4.place(x=95,y=180)
    cnwindow.mainloop()


# In[380]:


# ................................call contact using phone no...............................................

def CallPhno():
    
    global cpwindow
    cpwindow = tk.Tk()
    cpwindow.geometry("500x400")
    cpwindow.configure(bg="#FFE4B5")
    cpwindow.title("Contacts")

    head = tk.Label(cpwindow, text="\nCall using Phone No\n", font=("Arial", 20),bg="#FFE4B5").pack()
                
    def to_proceed() :
        cpwindow.destroy()
        proceed()
        
    def back3() :
        cpwindow.destroy()
        Call()
   
    
    def to_dispns():  
        tphno=phnotk.get()
        
        try:
            l=len(tphno)
            phno=int(tphno)

            if l==10:
                
                def pcall():
                    tphno=phnotk.get()
                    x=tk.messagebox.askyesno("Call", "Are you sure you want to call {}?".format(tphno))

                    if x==True:
                        tk.messagebox.showinfo("Calling....", "Call to {} will start after you press ok".format(tphno))
                        os.system(f'cmd /k "adb shell am start -a android.intent.action.CALL -d tel:{tphno}"')
                        os.system(f'cmd /k "adb kill-server"')
                        cpwindow.destroy()
                        Call()

                    else:
                        pass
                
                Submit = tk.Button(cpwindow, text="CALL", bg="#DC143C", fg="white", command=pcall).place(x=100, y=300)
                
            else:
                tk.messagebox.showwarning("Warning", "Phone No must be of 10 digits!!")

            
        except:
            tk.messagebox.showwarning("Warning", "Phone No must be a 10 digit Integer!!")
            
        
       
   
            
    
    l_1 = tk.Label(cpwindow, text="Enter Phone No: ",bg="#FFE4B5").place(x=40, y=100)
    
    phnotk = tk.Entry(cpwindow, fg='blue', bg='white', width=30)
    phnotk.place(x=135, y=100)

    
    Ok = tk.Button(cpwindow, text="OK", bg="green", fg="white", command=to_dispns).place(x=330, y=100)
    
    back3_button = tk.Button(text="Back", bg="blue", fg="white", height=1, width=10, command=back3)
    back3_button.place(x=370,y=100)

    head3 = tk.Label(cpwindow, text="\nNote: Your phone must be connected with USB\n",bg="#FFE4B5")
    head3.place(x=100,y=140)
    
    head4= tk.Label(cpwindow, text="\nNote: Your system must have ADB connect service\n",bg="#FFE4B5")
    head4.place(x=95,y=180)
    cpwindow.mainloop()


# In[381]:


# ..................................call contact main window...............................................

def Call():
    
    global cwindow
    cwindow = tk.Tk()
    cwindow.geometry("400x550")
    cwindow.configure(bg="#FFE4B5")
    cwindow.title("Contacts")

    head = tk.Label(cwindow, text="\nPlace a Call\n", font=("Arial", 20),bg="#FFE4B5").pack()
    head3 = tk.Label(cwindow, text="\nNote: Your phone must be connected with USB\n",bg="#FFE4B5").pack()
    
    head4= tk.Label(cwindow, text="\nNote: Your system must have ADB connect service\n",bg="#FFE4B5").pack()     
    x=tk.Label(cwindow, text="",bg="#FFE4B5").pack()
    head2 = tk.Label(cwindow, text="\nSelect Operation\n",bg="#FFE4B5").pack()
    y=tk.Label(cwindow, text="",bg="#FFE4B5").pack()
    
    def back3() :
        cwindow.destroy()
        proceed()
        
    def to_name():
        cwindow.destroy()
        CallName()
    
    def to_phno():
        cwindow.destroy()
        CallPhno()
        
    def exit1() :
        cwindow.destroy()
        exit()


    name_button = tk.Button(text="Call by Name", bg="green", fg="white", height=1, width=15, command=to_name)
    name_button.place(x=140, y=280)
    
    phno_button = tk.Button(text="Call by Phone No", bg="green", fg="white", height=1, width=15, command=to_phno)
    phno_button.place(x=140, y=330)
    

    
    back3_button = tk.Button(text="Back", bg="blue", fg="white", height=1, width=10, command=back3)
    back3_button.place(x=90,y=450)
    
    exit_button = tk.Button(text="Exit", bg="red", fg="white", height=1, width=10, command=exit1)
    exit_button.place(x=220, y=450)
    
    cwindow.mainloop()


# In[382]:


# ..................................menu...............................................

def proceed():
    global window2
    window2 = tk.Tk()

    window2.geometry("400x500")
    window2.configure(bg="#F3E3C3")
    window2.title("Contacts")
    head = tk.Label(window2, text="\nMenu\n", font=("Arial", 25),bg="#F3E3C3").pack()
    
    def to_Add() :
        window2.destroy()
        Add()
    
    def to_Remove() :
        window2.destroy()
        Remove()
    
    def to_Promote() :
        window2.destroy()
        Promote()
    
    def to_Display() :
        window2.destroy()
        Display()

    def to_Call() :
        window2.destroy()
        Call()

    def exit1() :
        window2.destroy()
        exit()
        
    def back1() :
        window2.destroy()
        main_screen()

    add_button = tk.Button(text="Add New Contact", bg="green", fg="white", height=1, width=15, command=to_Add)
    add_button.place(x=50, y=150)

    remove_button = tk.Button(text="Remove Contact", bg="green", fg="white", height=1, width=15, command=to_Remove)
    remove_button.place(x=230, y=150)

    promote_button = tk.Button(text="Update Contact", bg="green", fg="white", height=1, width=15, command=to_Promote)
    promote_button.place(x=50, y=220)

    display_button = tk.Button(text="Display Contact", bg="green", fg="white", height=1, width=15, command=to_Display)
    display_button.place(x=230, y=220)

    call_button = tk.Button(text="Place a call", bg="#DC143C", fg="white", height=1, width=15, command=to_Call)
    call_button.place(x=135, y=290)
    
    back_button = tk.Button(text="Back", bg="blue", fg="white", height=1, width=10, command=back1)
    back_button.place(x=80,y=400)
    
    exit_button = tk.Button(text="Exit", bg="red", fg="white", height=1, width=10, command=exit1)
    exit_button.place(x=240, y=400)
    
    
    window2.mainloop()


# In[383]:


# ..................................main window...............................................

def main_screen() :
    
    main_window = tk.Tk()

    main_window.geometry("450x500")
    
    main_window.title("Contacts")

    bg = tk.PhotoImage( file ="cbp.png")
  
    label1 = tk.Label( main_window, image = bg)
    label1.place(x = 0, y = 0)

    label2 = tk.Label( main_window, text = "Contacts Book",font=("Arial", 25), bg="white")
    
    label2.pack(pady = 40)
    
    def to_proceed() :
        main_window.destroy()
        proceed()

    def exit() :
        main_window.destroy()
        exit()


    proceed_button = tk.Button(text="Menu", bg="green", fg="white", height=1, width=10, command=to_proceed)
    proceed_button.place(x=90, y=430)
    

    exit_button = tk.Button(text="Exit", bg="red", fg="white", height=1, width=10, command=exit)
    exit_button.place(x=290, y=430)
    main_window.mainloop()



# In[384]:


#......................................start program...................................

main_screen()

