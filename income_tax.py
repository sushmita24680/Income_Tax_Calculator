from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageFilter,ImageTk
import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
import tkinter.messagebox
import cv2

class Calculation:
     def __init__(self,root):

         #=====================================variables=================================#
         taxble_sal=StringVar()
         incm_intrst=StringVar()
         retal_incm_recieve=StringVar()
         intrst_paid_lon=StringVar()
         intrst_paid_homlon=StringVar()
         bsic_deducton=StringVar()
         intrst_frm_depst=StringVar()
         medcal_insrance=StringVar()
         donation_charity=StringVar()
         intrst_on_ed_lon=StringVar()
         intrst_on_housing_loan=StringVar()
         Cal_tax=StringVar()
         
         #=====================================variables=================================#
         #=====================================function==================================#
         
         def cal():
              taxble_sal_= float((taxble_sal.get()))
              incm_intrst_=float(incm_intrst.get())
              retal_incm_recieve_=float(retal_incm_recieve.get())
              intrst_paid_lon_=float(intrst_paid_lon.get())
              intrst_paid_homlon_=float(intrst_paid_homlon.get())
              bsic_deducton_=float(bsic_deducton.get())
              intrst_frm_depst_=float(intrst_frm_depst.get())
              medcal_insrance_=float(medcal_insrance.get())
              donation_charity_=float(donation_charity.get())
              intrst_on_ed_lon_=float(intrst_on_ed_lon.get())
              intrst_on_housing_loan_=float(intrst_on_housing_loan.get())
              
              retal_incm_recieve_=retal_incm_recieve_-8000
              if(retal_incm_recieve_<=0):
                   retal_incm_recieve_=0
             
              totalsal=(taxble_sal_+incm_intrst_-retal_incm_recieve_- intrst_paid_lon_-intrst_paid_homlon_-donation_charity_-intrst_on_housing_loan_-intrst_on_ed_lon_)
              bsic_deducton_=bsic_deducton_-150000
              if(bsic_deducton_<=0):
                   bsic_deducton_=0
              intrst_frm_depst_=intrst_frm_depst_-10000
              if(intrst_frm_depst_<=0):
                   intrst_frm_depst_=0
              medcal_insrance_=medcal_insrance_-50000
              if(medcal_insrance_<=0):
                   medcal_insrance_=0


              grosssalary=(bsic_deducton_+intrst_frm_depst_+medcal_insrance_)+totalsal
              
              income= grosssalary
              tax=0.0
              cess=0.0
              if income<=250000:
                   tax=0
              elif income<=500000:
                   tax=(income-250000)*0.05
              elif income<=1000000:    
                   tax=12500+(income-500000)*0.2
              else:
                   tax=12500+100000+(income-1000000)*0.3
              cess=tax*0.04
              ttax=0.0
              ttax=tax+cess
              if not(ttax==0):
                   
                   ttax=ttax/12
              Cal_tax.set(ttax)
               

         #=====================================function====================================#    
         

         def framing(frame):
             
            
            
            Manage_Frame=frame
            #Manage_Frame.place(x=20,y=70,width=500,height=600)
            
            i=0
            for i in range(0,1):
                m_title=Label(Manage_Frame,text="Basic Details:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
                m_title.grid(row=i,columnspan=2,pady=20)
                i=i+1
                lbl_fin=Label(Manage_Frame,text="Which Financial Year do you want to calculate taxes for?",bg="white",fg="black",font=("times new roman",20,"bold"))
                lbl_fin.grid(row=i,column=0,pady=10,padx=20,sticky="w")
                

                txt_fin=Label(Manage_Frame,text="2019-20",font=("times new roman",15,"bold"),bd=5,width=17,relief=GROOVE)
                txt_fin.grid(row=i,column=1,pady=10,padx=20,sticky="w")
                i=i+1

                lbl_age=Label(Manage_Frame,text="Your Age:",bg="white",fg="black",font=("times new roman",20,"bold"))
                lbl_age.grid(row=i,column=0,pady=10,padx=20,sticky="w")
                
                                   
                txt_age=Label(Manage_Frame,text="below 60",font=("times new roman",15,"bold"),bd=5,width=17,relief=GROOVE)
                txt_age.grid(row=i,column=1,pady=10,padx=20,sticky="w")
                i=i+1

                m_title2=Label(Manage_Frame,text="Income Details:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
                m_title2.grid(row=i,columnspan=2,pady=20)
                i=i+1

                lbl_Tble_Sal=Label(Manage_Frame,text="Taxable Salary:",bg="white",fg="black",font=("times new roman",20,"bold"))
                lbl_Tble_Sal.grid(row=i,column=0,pady=10,padx=20,sticky="w")
                

                txt_Tble_Sal=Entry(Manage_Frame,textvariable=taxble_sal,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                txt_Tble_Sal.grid(row=i,column=1,pady=10,padx=20,sticky="w")
                i=i+1

                '''combo_gender=ttk.Combobox(Manage_Frame,font=("times new roman",14,"bold"))
                combo_gender['value']=("male","female","other")
                combo_gender.grid(row=i,column=1,padx=20,pady=10)
                i=i+1'''

                lbl_Infint=Label(Manage_Frame,text="Income From Interest:",bg="white",fg="black",font=("times new roman",20,"bold"))
                lbl_Infint.grid(row=i,column=0,pady=10,padx=20,sticky="w")
                

                txt_Infint=Entry(Manage_Frame,textvariable=incm_intrst,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                txt_Infint.grid(row=i,column=1,pady=10,padx=20,sticky="w")
                i=i+1

                lbl_Inphl=Label(Manage_Frame,text="Income Paid on Home Loan:",bg="white",fg="black",font=("times new roman",20,"bold"))
                lbl_Inphl.grid(row=i,column=0,pady=10,padx=20,sticky="w")
                

                txt_Inphl=Entry(Manage_Frame,textvariable=intrst_paid_homlon,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                txt_Inphl.grid(row=i,column=1,pady=10,padx=20,sticky="w")
                i=i+1

                lbl_Rentir=Label(Manage_Frame,text="Rental Income Received:",bg="white",fg="black",font=("times new roman",20,"bold"))
                lbl_Rentir.grid(row=i,column=0,pady=10,padx=20,sticky="w")
                

                txt_Rentir=Entry(Manage_Frame,textvariable=retal_incm_recieve,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                txt_Rentir.grid(row=i,column=1,pady=10,padx=20,sticky="w")
                i=i+1

                
                lbl_Iponl=Label(Manage_Frame,text="Interest Paid on Loan:",bg="white",fg="black",font=("times new roman",20,"bold"))
                lbl_Iponl.grid(row=i,column=0,pady=10,padx=20,sticky="w")
                

                txt_Iponl=Entry(Manage_Frame,textvariable=intrst_paid_lon,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                txt_Iponl.grid(row=i,column=1,pady=10,padx=20,sticky="w")
                i=i+1

                m_title2=Label(Manage_Frame,text="Deduction:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
                m_title2.grid(row=i,columnspan=2,pady=20)
                i=i+1

                lbl_BsicDedton=Label(Manage_Frame,text="Basic Deductions-80C:",bg="white",fg="black",font=("times new roman",20,"bold"))
                lbl_BsicDedton.grid(row=i,column=0,pady=10,padx=20,sticky="w")
                

                txt_BsicDedton=Entry(Manage_Frame,textvariable=bsic_deducton,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                txt_BsicDedton.grid(row=i,column=1,pady=10,padx=20,sticky="w")
                i=i+1

                '''combo_gender=ttk.Combobox(Manage_Frame,font=("times new roman",14,"bold"))
                combo_gender['value']=("male","female","other")
                combo_gender.grid(row=i,column=1,padx=20,pady=10)
                i=i+1'''

                lbl_InfrmDpst=Label(Manage_Frame,text="Interest from Deposits-80TTA :",bg="white",fg="black",font=("times new roman",20,"bold"))
                lbl_InfrmDpst.grid(row=i,column=0,pady=10,padx=20,sticky="w")
                

                txt_InfrmDpst=Entry(Manage_Frame,textvariable=intrst_frm_depst,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                txt_InfrmDpst.grid(row=i,column=1,pady=10,padx=20,sticky="w")
                i=i+1

                lbl_MdclIn=Label(Manage_Frame,text="Medical Insurance-80D:",bg="white",fg="black",font=("times new roman",20,"bold"))
                lbl_MdclIn.grid(row=i,column=0,pady=10,padx=20,sticky="w")
                

                txt_MdclIn=Entry(Manage_Frame,textvariable=medcal_insrance,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                txt_MdclIn.grid(row=i,column=1,pady=10,padx=20,sticky="w")
                i=i+1

                lbl_Dontocrity=Label(Manage_Frame,text="Donations to Charity-80G:",bg="white",fg="black",font=("times new roman",20,"bold"))
                lbl_Dontocrity.grid(row=i,column=0,pady=10,padx=20,sticky="w")
                

                txt_Dontocrity=Entry(Manage_Frame,textvariable=donation_charity,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                txt_Dontocrity.grid(row=i,column=1,pady=10,padx=20,sticky="w")
                i=i+1

                
                lbl_InoEdl=Label(Manage_Frame,text="Interest on Education Loan-80E:",bg="white",fg="black",font=("times new roman",20,"bold"))
                lbl_InoEdl.grid(row=i,column=0,pady=10,padx=20,sticky="w")
                

                txt_InoEdl=Entry(Manage_Frame,textvariable=intrst_on_ed_lon,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                txt_InoEdl.grid(row=i,column=1,pady=10,padx=20,sticky="w")
                i=i+1

                lbl_Inohml=Label(Manage_Frame,text="Interest on Housing Loan-80EEA:",bg="white",fg="black",font=("times new roman",20,"bold"))
                lbl_Inohml.grid(row=i,column=0,pady=10,padx=20,sticky="w")
                

                txt_Inohml=Entry(Manage_Frame,textvariable=intrst_on_housing_loan,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                txt_Inohml.grid(row=i,column=1,pady=10,padx=20,sticky="w")
                i=i+1

                
                Button(Manage_Frame, text='Calculate',width=20,font=("bold",25),bg='brown',fg='white',command=cal).grid(row=i,columnspan=2,pady=20)
                i=i+1
                lbl_Calculate=Label(Manage_Frame,text=" Monthly income Tax: ",bg="white",fg="black",font=("times new roman",20,"bold"))
                lbl_Calculate.grid(row=i,column=0,pady=10,padx=20,sticky="w")
                
                Calculate=Entry(Manage_Frame,textvariable=Cal_tax,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                Calculate.grid(row=i,column=1,pady=10,padx=20)
                i=i+1



        
         def onFrameConfigure(canvas):
            '''Reset the scroll region to encompass the inner frame'''
            canvas.configure(scrollregion=canvas.bbox("all"))
        
        

       
         title=Label(root,text="tax calculation",font=("times new roman",40,"bold"),bg="yellow",fg="white")
         title.pack(side=TOP,fill=X)
         root.geometry(newGeometry= '1600x820')
         root.title("income_tax")
         root.iconbitmap(r"incometaxicon_wLC_icon.ico")
         canvas = tk.Canvas(root, borderwidth=70, background="#006666")
         frame = tk.Frame(canvas, background="#ffffff")
         vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
         canvas.configure(yscrollcommand=vsb.set)

         vsb.pack(side="right", fill="y")
         canvas.pack(side="left", fill="both", expand=True)
         canvas.create_window((4,4), window=frame, anchor="nw")

         frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

         framing(frame)

    


def c1():
    
    if __name__=="__main__":
         
        
        cal=Calculation(Toplevel())
        



  
class register:
     
     def __init__(self, root1, image_path="tasks-512.png"):

         self.root1 = root1
         
 
         
 
         # Button that lets the user blur the image
         #self.btn_blur=tkinter.Button(root1, text="Blur", width=50, command=self.blur_image)
         #def blur_image(self):
        
         #self.root1 = root
        
         self.root1.geometry(newGeometry= '1600x820')
         self.root1.title("income_tax")
         self.root1.iconbitmap(r"incometaxicon_wLC_icon.ico")
        
        
         self.root1.configure(bg='Green')
         creds="tempfile.txt"
         credd="tempfiled.txt"
        
        

         self.root1.title("Registeration ID")
        
        #==================================================variable===============================================
        
            
         Fullname=StringVar()
         Email=StringVar()
         Password=StringVar()
         cfmPassword=StringVar()
         def lgin():
              with open(credd, 'w') as f:
                f.write(Fullname.get())
                f.write('\n') 
                f.write(cfmPassword.get()) 
                f.write('\n')
                f.write(Email.get()) 
                f.write('\n') 
                f.close() 
            

         def passdverifying(p,rs,no):
           
           count=1
           passd=rs
          # passd=str(input(Entry(root,textvar=cPassword,font=("bold",20),width=20).place(x=1100,y=500) ))
           for i in range (0,no):
               if(passd[i]== p[i] and( (Fullname.get()>='a'and Fullname.get()<='z')or(Fullname.get()>='A'and Fullname.get()<='Z'))  ):
                       count=0
               else:
                   
                   count=1
                   break

           if(count==0):
               messagebox.showinfo("password","verified sucessfully");
               lgin()
               self.root1.destroy()
               
               c1()
               
                         
           else:
               messagebox.showinfo("Password"," password does not matched or invalid username ");
               self.root1.destroy()
        

         def setpassd(p,rs,no):
            
             l=d=r=n=0
             for k in range (0,no):
                     if(p[k]>='#' and p[k]<='&' or p[k]== '@'):
                                   l=1
                     elif(p[k]>='A' and p[k]<='Z'):
                                 d=1
                     elif(p[k]>='a' and p[k]<='z'):
                                       r=1
                     elif(p[k]>='0' and p[k]<='9'):
                                      n=1
             if not((l==1 and d==1) and(r==1 and n==1) ):
                     messagebox.showinfo("warning","invalid password\n include special chracter '@,#$,%,&'\ninclude numbers\ninclude upper and lower case");
                 
                     self.root1.destroy()
             else:
                   passdverifying(p,rs,no)
                     
                       

       
        
         def enter():
            
            with open(creds,'r') as f:
                data = f.readlines() 
                p = data[0].rstrip() 
                rs = data[1].rstrip()
                no=len(p)
                if(no<8):
                     messagebox.showinfo("invalidpassword"," enter atleast 8 charcters")
                     self.root1.destroy()   
                     
                else:
                     setpassd(p,rs,no)
                    
                f.close()

         def FSSignup():
            
            
            with open(creds, 'w') as f: 
                f.write(self.txtpassword.get())
                f.write('\n') 
                f.write(self.txtcfmpassword.get())
                f.close() 
                enter()
            
        

        
        
        #===================================================label==========================================
         self.lblregister = Label(self.root1, text="Registration form",bg="green",fg="white",width=50,font=("bold", 40))        
         self.lblregister.pack()
     
        
        
         self.lblusername = Label(self.root1, text="UserName:",bg="green",width=20,font=("bold", 30))
         self.lblusername.pack()
         self.lblusername.place(x=640,y=200)
         self.txtusername = Entry(self.root1,textvariable=Fullname,font=("bold",20),width=20)
         self.txtusername.pack()
         self.txtusername.place(x=1100,y=200)
         self.lblemail = Label(self.root1, text="Email:",bg="green",width=20,font=("bold", 30))
         self.lblemail.pack()
         self.lblemail.place(x=650,y=300)
         self.txtemail = Entry(self.root1,textvariable=Email,font=("bold",20),width=20)
         self.txtemail.pack()
         self.txtemail.place(x=1100,y=300)
         self.lblpassword = Label(self.root1,text=" enter Password:",bg="green",width=25,font=("bold", 30))
         self.lblpassword.pack()
         self.lblpassword.place(x=640,y=400)
         self.txtpassword = Entry(self.root1,textvariable=Password,show='*',font=("bold",20),width=20)
         self.txtpassword.pack()
         self.txtpassword.place(x=1100,y=400)
         self.lblcfmpassword = Label(self.root1,text=" confirm Password:",bg="green",width=25,font=("bold", 30))
         self.lblcfmpassword.pack()
         self.lblcfmpassword.place(x=640,y=500)
         self.txtcfmpassword = Entry(self.root1,textvariable=cfmPassword,show='*',font=("bold",20),width=20)
         self.txtcfmpassword.pack()
         self.txtcfmpassword.place(x=1100,y=500)
         self.submit=Button(self.root1, text='Submit',width=20,font=("bold",25),bg='brown',fg='white',command=FSSignup).place(x=1050,y=600)
         
         self.orig_img = Image.open(image_path)

         self.cv_img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
 
         self.height, self.width, no_channels = self.cv_img.shape
 
         self.canvas = tkinter.Canvas(root1, width = self.width, height = self.height)
         self.canvas.pack()
         self.canvas.place(x=100,y=150)
 
         self.photo = ImageTk.PhotoImage(image = Image.fromarray(self.cv_img))
 
         self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
         

         self.root1.mainloop()    
    
def r1():
 register(Toplevel())
        
        
class login:
     def __init__(self, root1, image_path="Login-512.png"):
         self.root1 = root1
 
         
 
         # Button that lets the user blur the image
         #self.btn_blur=tkinter.Button(root1, text="Blur", width=50, command=self.blur_image)
         #def blur_image(self):
        
         #self.root1 = root
        
         self.root1.geometry(newGeometry= '1600x820')
         self.root1.title("income_tax")
         self.root1.iconbitmap(r"incometaxicon_wLC_icon.ico")
        
        
         self.root1.configure(bg='#25A08C')
         creds="tempfile.txt"
         credd="tempfiled.txt"
        
        

         self.root1.title("Login  ID")
         
        
        #==================================================variable===============================================
         Fullname=StringVar()
         Password=StringVar()
         
         def enter():
            
    
            flag=0
            with open(credd,'r') as f:
                datas = f.readlines()
                data = f.readline()
                i=0
                for i in datas:
                     uname = datas[0].rstrip()
                     pword = datas[1].rstrip()
                     email = datas[2].rstrip()
                    
                     if( Fullname.get()==uname and Password.get()==pword):
                          flag=1
                     
                if (flag==1):
                      messagebox.showinfo("Verification","Logged in sucessfully!")
                      self.root1.destroy()
                      c1()
                else:
                      messagebox.showinfo("Verification"," Invalid Username or Password")
                      self.root1.destroy()   
                f.close()

           
        

        
        
        #===================================================label==========================================
         self.lblregister = Label(self.root1, text=" Login User:",bg='#25A08C',fg="white",width=50,font=("bold", 40))        
         self.lblregister.pack()
         self.lblregister.place(x=340,y=50)
        
         self.lblusername = Label(self.root1, text="UserName:",bg='#25A08C',width=20,font=("bold", 30))
         self.lblusername.pack()
         self.lblusername.place(x=640,y=200)
         self.txtusername = Entry(self.root1,textvariable=Fullname,font=("bold",20),width=20)
         self.txtusername.pack()
         self.txtusername.place(x=1100,y=200)
         self.lblpassword = Label(self.root1, text="enter Password:",bg='#25A08C',width=20,font=("bold", 30))
         self.lblpassword.pack()
         self.lblpassword.place(x=650,y=300)
         self.txtpassword = Entry(self.root1,textvariable=Password,show='*',font=("bold",20),width=20)
         self.txtpassword.pack()
         self.txtpassword.place(x=1100,y=300)
         self.submit=Button(self.root1, text='Submit',width=20,font=("bold",25),bg='#076757',fg="white",command=enter).place(x=1050,y=450)
         
         self.orig_img = Image.open(image_path)

         self.cv_img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
 
         self.height, self.width, no_channels = self.cv_img.shape
 
         self.canvas = tkinter.Canvas(root1, width = self.width, height = self.height)
         self.canvas.pack()
         self.canvas.place(x=100,y=150)
 
         self.photo = ImageTk.PhotoImage(image = Image.fromarray(self.cv_img))
 
         self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
         

         self.root1.mainloop()
def l1():
     login(Toplevel())


def homepage():
    root = Tk()
    frame =Frame(root)
    frame.pack()
    root.geometry(newGeometry= '1600x820')


    root.title("income_tax")
    root.iconbitmap(r"incometaxicon_wLC_icon.ico")
    load = Image.open("incometaxicon.png")
    render = ImageTk.PhotoImage(load)
    
    root.configure(bg='White')
    boder1=Label(root,text=" ",bg="red", width=2,height=54)
    boder1.place(x=5,y=5)
    boder2=Label(root,text=" ",bg="red", width=2,height=54)
    boder2.place(x=1574,y=5)


    welcomt=Label(root,text="WELCOME TO INCOME TAX CALCULATOR",bg="white",width=40,font=("bold", 40))
    welcomt.pack()
    img = Label(image=render)
    img.image = render
    img.place(x=525, y=150)
#login=Button(self.root1, text='Submit',width=20,bg='brown',fg='white',command=self.root1.destroy).place(x=180,y=380)   
    login=Button(root, text="  Login  ",bg="#00008b", width=18,font=("bold",25),command=l1)
    login.place(x=90,y=700)
    signup= Button(root,text="  signup ",bg="green",width=18,font=("bold",25),command=r1)
    signup.place(x=460, y=700)
    feedbk=Button(root, text=" Feedback",bg="gray",width=18,font=("bold",25))
    feedbk.place(x=830,y=700)
    guid=Button(root, text="Guidlines",bg="orange",width=18,font=("bold",25))
    guid.place(x=1200,y=700)
                
    root.mainloop()


        
homepage()    
