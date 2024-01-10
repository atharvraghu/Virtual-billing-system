from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime

class customer:

    def __init__(self,root):
        self.root=root
        self.root.title('customer billing system')
        self.root.geometry('1350x750+0+0')
        self.root.config(background='cyan')

        ABC=Frame(self.root,bg='powder blue',bd=20,relief=RIDGE)
        ABC.grid()
        ABC1=Frame(ABC,bd=14,width=1350,height=300,padx=10,bg='olive',relief=SUNKEN)
        ABC1.grid(row=0,column=0,columnspan=10,sticky=W)
        ABC2=Frame(ABC,bd=14,width=1350,height=488,padx=10,bg='olive',relief=RIDGE)
        ABC2.grid(row=1,column=0,sticky=W)
        ABC3=Frame(ABC,bd=14,width=450,height=488,padx=10,bg='olive',relief=RIDGE)
        ABC3.grid(row=1,column=1,sticky=W)
        ABC4=Frame(ABC,bd=14,width=460,height=488,padx=10,bg='olive',relief=RIDGE)
        ABC4.grid(row=1,column=2,sticky=W)
        ABC5=Frame(ABC4,bd=14,width=370,height=340,padx=10,bg='olive',relief=RIDGE)
        ABC5.grid(row=0,column=0,sticky=W)
        ABC6=Frame(ABC4,bd=14,width=370,height=120,padx=10,bg='olive',relief=RIDGE)
        ABC6.grid(row=1,column=0,columnspan=4,sticky=W)

        import time as tm

        Date1=StringVar()
        Time1=StringVar()
        Date1.set(tm.strftime('%d/%m/%y'))
        Time1.set(tm.strftime('%H:%M:%S'))

        #==============================================================================================
        customerNo=StringVar()
        shopname=StringVar()
        Address=StringVar()
        state=StringVar()
        pincode=StringVar()
        Gstin=StringVar()
        invoiceNo=StringVar()
        BookNo=StringVar()
        Date=StringVar()
        TotalCost=StringVar()
        SubTotal=StringVar()
        PaidTax=StringVar()



        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()
        var9=IntVar()
        var10=IntVar()
        var11=IntVar()
        var12=IntVar()
        var13=IntVar()
        var14=IntVar()
        var15=IntVar()
        var16=IntVar()
        
            


        E_soyakatori=StringVar()
        E_soyasticks=StringVar()
        E_soyachips=StringVar()
        E_south_indian_mix=StringVar()
        E_Diet_snax=StringVar()
        E_salted_peanut=StringVar()
        E_Black_chana=StringVar()
        E_Diet_mix=StringVar()
       
        
        E_soyakatori.set('0')
        E_soyasticks.set('0')
        E_soyachips.set('0')
        E_south_indian_mix.set('0')
        E_Diet_snax.set('0')
        E_salted_peanut.set('0')
        E_Black_chana.set('0')
        E_Diet_mix.set('0')
       
        #==============================================================================================

        self.lblTitle=Label(ABC1,textvariable=Date1,font=('Arial',30),pady=9,
                        bd=5,bg='black',fg='cornsilk').grid(row=0,column=0)
        
        self.lblTitle=Label(ABC1,text='customer billing system',font=('Goudy Stout',27),pady=9,
                        bd=0,bg='black',fg='cornsilk', justify= CENTER).grid(row=0,column=1)
        
        self.lblTitle=Label(ABC1,textvariable=Time1,font=('Arial',30),pady=9,
                        bd=5,bg='black',fg='cornsilk').grid(row=0,column=2)
        #==============================================================================================
        def iExit():
            iExit=tkinter.messagebox.askyesno('customer billing system','confirm if you want to exit')
            if iExit > 0:
                root.destroy()
                return

        #==============================================================================================
        def Reset():
            self.txtReceipt.delete('1.0',END)
            E_soyakatori.set('0')
            E_soyasticks.set('0')
            E_soyachips.set('0')
            E_south_indian_mix.set('0')
            E_Diet_snax.set('0')
            E_salted_peanut.set('0')
            E_Black_chana.set('0')
            E_Diet_mix.set('0')


            

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)
            var9.set(0)
            var10.set(0)
            var11.set(0)
            var12.set(0)
            var13.set(0)
            var14.set(0)
            var15.set(0)
            var16.set(0)

            customerNo.set('')
            shopname.set('')
            Address.set('')
            
            state.set('')
            pincode.set('')
            Gstin.set('')
            invoiceNo.set('')
            BookNo.set('')
            Date.set('')
            TotalCost.set('')
            SubTotal.set('')
            PaidTax.set('')
            
        #==============================================================================================

        def chksoyakatori():
            if (var1.get()==1):
                self.txtsoyakatori.configure(state=NORMAL)
                self.txtsoyakatori.focus()
                self.txtsoyakatori.delete('0',END)
                E_soyakatori.set('')
            elif var1.get()==0:
                self.txtsoyakatori.configure(state=DISABLED)
                E_soyakatori.set('0')
                
        def chksoyasticks():
            if (var2.get()==1):
                self.txtsoyasticks.configure(state=NORMAL)
                self.txtsoyasticks.focus()
                self.txtsoyasticks.delete('0',END)
                E_soyasticks.set('')
            elif var2.get()==0:
                self.txtsoyasticks.configure(state=DISABLED)
                E_soyasticks.set('0')


        def chksoyachips():
            if (var3.get()==1):
                self.txtsoyachips.configure(state=NORMAL)
                self.txtsoyachips.focus()
                self.txtsoyachips.delete('0',END)
                E_soyachips.set('')
            elif var3.get()==0:
                self.txtsoyachips.configure(state=DISABLED)
                E_soyachips.set('0')


        def chkDiet_snax():
            if (var4.get()==1):
                self.txtDiet_snax.configure(state=NORMAL)
                self.txtDiet_snax.focus()
                self.txtDiet_snax.delete('0',END)
                E_Diet_snax.set('')
            elif var4.get()==0:
                self.txtDiet_snax.configure(state=DISABLED)
                E_Diet_snax.set('0')
                

        def chksouth_indian_mix():
            if (var5.get()==1):
                self.txtsouth_indian_mix.configure(state=NORMAL)
                self.txtsouth_indian_mix.focus()
                self.txtsouth_indian_mix.delete('0',END)
                E_south_indian_mix.set('')
            elif var5.get()==0:
                self.txtsouth_indian_mix.configure(state=DISABLED)
                E_south_indian_mix.set('0')

        def chkBlack_chana():
            if (var6.get()==1):
                self.txtBlack_chana.configure(state=NORMAL)
                self.txtBlack_chana.focus()
                self.txtBlack_chana.delete('0',END)
                E_Black_chana.set('')
            elif var6.get()==0:
                self.txtBlack_chana.configure(state=DISABLED)
                E_Black_chana.set('0')

        def chksalted_peanut():
            if (var7.get()==1):
                self.txtsalted_peanut.configure(state=NORMAL)
                self.txtsalted_peanut.focus()
                self.txtsalted_peanut.delete('0',END)
                E_salted_peanut.set('')
            elif var7.get()==0:
                self.txtsalted_peanut.configure(state=DISABLED)
                E_salted_peanut.set('0')

        def chkDiet_mix():
            if (var8.get()==1):
                self.txtDiet_mix.configure(state=NORMAL)
                self.txtDiet_mix.focus()
                self.txtDiet_mix.delete('0',END)
                E_Diet_mix.set('')
            elif var8.get()==0:
                self.txtDiet_mix.configure(state=DISABLED)
                E_Diet_mix.set('0')
        #==============================================================================================
        def costofitems():
            import mysql.connector
            import MySQLdb
            db=mysql.connector.connect(host='localhost',user='root',passwd='',database='arufood')
            c=db.cursor()
            
            
            I1=float(E_soyakatori.get())
            I2=float(E_soyasticks.get())
            I3=float(E_soyachips.get())
            I4=float(E_south_indian_mix.get())
            I5=float(E_Diet_snax.get())
            I6=float(E_Black_chana.get())
            I7=float(E_salted_peanut.get())
            I8=float(E_Diet_mix.get())

            c.execute('select iprice from Aprice')
            row = [e[0] for e in c.fetchall()]
            
            

            priceofitems=(I1*row[0])+(I2*row[1])+(I3*row[2])+(I4*row[3])+(I5*row[4])+(I6*row[5])+(I7*row[6])+(I8*row[7])
            SubTotalofITEMS='Rs',str('%.2f'%priceofitems)

            SubTotal.set(SubTotalofITEMS)
            Tax='Rs',str('%.2f'%((priceofitems)*0.1))
            PaidTax.set(Tax)
            TTax=((priceofitems)*0.15)
            TCost='Rs',str('%.2f'%(priceofitems+TTax))
            TotalCost.set(TCost)

            self.txtReceipt.insert(END,'Items\t\t\t\t'+'No. of Items \n')
            self.txtReceipt.insert(END,'soyakatori:\t\t\t\t\t'+E_soyakatori.get()+ '\n')
            self.txtReceipt.insert(END,'soyasticks\t\t\t\t\t'+E_soyasticks.get()+'\n')
            self.txtReceipt.insert(END,'soyachips\t\t\t\t\t'+E_soyachips.get()+'\n')
            self.txtReceipt.insert(END,'south indian mix\t\t\t\t\t'+E_south_indian_mix.get()+'\n')
            self.txtReceipt.insert(END,'Diet snax\t\t\t\t\t'+E_Diet_snax.get()+'\n')
            self.txtReceipt.insert(END,'Black chana\t\t\t\t\t'+E_Black_chana.get()+'\n')
            self.txtReceipt.insert(END,'salted peanut\t\t\t\t\t'+E_salted_peanut.get()+'\n')
            self.txtReceipt.insert(END,'Diet mix\t\t\t\t\t'+E_Diet_mix.get()+'\n')

            self.txtReceipt.insert(END,'\nTax Paid\t\t\t\t'+PaidTax.get()+'\n')
            self.txtReceipt.insert(END,'\nSubTotal\t\t\t\t'+str(SubTotal.get())+'\n')
            self.txtReceipt.insert(END,'\nTotalCost\t\t\t\t'+str(TotalCost.get()))
            
            

            
                
        


        #==============================================================================================


        self.txtReceipt=Text(ABC5,height=19,width=43,bd=10,font=('arial',9,'bold'))
        self.txtReceipt.grid(row=0,column=0) 


        #==============================================================================================
        
        self.lblcustomerNo=Label(ABC2,font=('Arial',12,'bold'),text='customerNo',padx=2,bg='cadet blue')
        self.lblcustomerNo.grid(row=0,column=0,sticky=W)
        self.txtcustomerNo=Entry(ABC2,font=('Arial',12,'bold'),textvariable=customerNo,width=18)
        self.txtcustomerNo.grid(row=0,column=1,pady=3,padx=20)

        self.lblshopname=Label(ABC2,font=('Arial',12,'bold'),text='shopname',padx=2,bg='cadet blue')
        self.lblshopname.grid(row=1,column=0,sticky=W)
        self.txtshopname=Entry(ABC2,font=('Arial',12,'bold'),textvariable=shopname,width=18)
        self.txtshopname.grid(row=1,column=1,pady=3,padx=20)

        self.lblAddress=Label(ABC2,font=('Arial',12,'bold'),text='Address',padx=2,bg='cadet blue')
        self.lblAddress.grid(row=3,column=0,sticky=W)
        self.txtAddress=Entry(ABC2,font=('Arial',12,'bold'),textvariable=Address,width=18)
        self.txtAddress.grid(row=3,column=1,pady=3,padx=20)

        self.lblstate=Label(ABC2,font=('Arial',12,'bold'),text='state',padx=2,bg='cadet blue')
        self.lblstate.grid(row=4,column=0,sticky=W)
        self.txtstate=Entry(ABC2,font=('Arial',12,'bold'),textvariable=state,width=18)
        self.txtstate.grid(row=4,column=1,pady=3,padx=20)

        self.lblpincode=Label(ABC2,font=('Arial',12,'bold'),text='pincode',padx=2,bg='cadet blue')
        self.lblpincode.grid(row=5,column=0,sticky=W)
        self.txtpincode=Entry(ABC2,font=('Arial',12,'bold'),textvariable=pincode,width=18)
        self.txtpincode.grid(row=5,column=1,pady=3,padx=20)

        self.lblGstin=Label(ABC2,font=('Arial',12,'bold'),text='Gstin',padx=2,bg='cadet blue')
        self.lblGstin.grid(row=6,column=0,sticky=W)
        self.txtGstin=Entry(ABC2,font=('Arial',12,'bold'),textvariable=Gstin,width=18)
        self.txtGstin.grid(row=6,column=1,pady=3,padx=20)

        self.lblinvoiceNo=Label(ABC2,font=('Arial',12,'bold'),text='invoiceNo',padx=2,bg='cadet blue')
        self.lblinvoiceNo.grid(row=8,column=0,sticky=W)
        self.txtinvoiceNo=Entry(ABC2,font=('Arial',12,'bold'),textvariable=invoiceNo,width=18)
        self.txtinvoiceNo.grid(row=8,column=1,pady=3,padx=20)


        self.lblBookNo=Label(ABC2,font=('Arial',12,'bold'),text='BookNo',padx=2,bg='cadet blue')
        self.lblBookNo.grid(row=10,column=0,sticky=W)
        self.txtBookNo=Entry(ABC2,font=('Arial',12,'bold'),textvariable=BookNo,width=18)
        self.txtBookNo.grid(row=10,column=1,pady=3,padx=20)
    

        self.lblDate=Label(ABC2,font=('Arial',12,'bold'),text='Date',padx=2,bg='cadet blue')
        self.lblDate.grid(row=16,column=0,sticky=W)
        self.txtDate=Entry(ABC2,font=('Arial',12,'bold'),textvariable=Date,width=18)
        self.txtDate.grid(row=16,column=1,pady=3,padx=20)

        
        #==============================================================================================
        self.soyakatori=Checkbutton(ABC3,text='soyakatori',variable=var1,onvalue=1,offvalue=0,
                               font=('arial',12,'bold'),bg='powder blue',command=chksoyakatori).grid(row=0,sticky=W)
        self.txtsoyakatori=Entry(ABC3,font=('arial',12,'bold'),textvariable=E_soyakatori,bd=8,
                            width=20,justify='left',state=DISABLED)
        self.txtsoyakatori.grid(row=0,column=1)
        

        

        self.soyasticks=Checkbutton(ABC3,text='soyasticks',variable=var2,onvalue=1,offvalue=0,
                          font=('arial',12,'bold'),bg='powder blue',command=chksoyasticks).grid(row=1,
                                                                                           sticky=W)
        self.txtsoyasticks=Entry(ABC3,font=('arial',12,'bold'),textvariable=E_soyasticks,bd=8,
                            width=20,justify='left',state=DISABLED)
        self.txtsoyasticks.grid(row=1,column=1)



        self.soyachips=Checkbutton(ABC3,text='soyachips',variable=var3,onvalue=1,offvalue=0,
                          font=('arial',12,'bold'),bg='powder blue',command=chksoyachips).grid(row=2,
                                                                                           sticky=W)
        self.txtsoyachips=Entry(ABC3,font=('arial',12,'bold'),textvariable=E_soyachips,bd=8,
                            width=20,justify='left',state=DISABLED)
        self.txtsoyachips.grid(row=2,column=1)




        self.Diet_snax=Checkbutton(ABC3,text='Diet snax',variable=var4,onvalue=1,offvalue=0,
                          font=('arial',12,'bold'),bg='powder blue',command=chkDiet_snax).grid(row=3,
                                                                                           sticky=W)
        self.txtDiet_snax=Entry(ABC3,font=('arial',12,'bold'),textvariable=E_Diet_snax,bd=8,
                            width=20,justify='left',state=DISABLED)
        self.txtDiet_snax.grid(row=3,column=1)



        self.south_indian_mix=Checkbutton(ABC3,text='south indian mix',variable=var5,onvalue=1,offvalue=0,
                          font=('arial',12,'bold'),bg='powder blue',command=chksouth_indian_mix).grid(row=4,
                                                                                           sticky=W)
        self.txtsouth_indian_mix=Entry(ABC3,font=('arial',12,'bold'),textvariable=E_south_indian_mix,bd=8,
                            width=20,justify='left',state=DISABLED)
        self.txtsouth_indian_mix.grid(row=4,column=1)



        self.Black_chana=Checkbutton(ABC3,text='Black chana',variable=var6,onvalue=1,offvalue=0,
                          font=('arial',12,'bold'),bg='powder blue',command=chkBlack_chana).grid(row=5,
                                                                                           sticky=W)
        self.txtBlack_chana=Entry(ABC3,font=('arial',12,'bold'),textvariable=E_Black_chana,bd=8,
                            width=20,justify='left',state=DISABLED)
        self.txtBlack_chana.grid(row=5,column=1)



        self.salted_peanut=Checkbutton(ABC3,text='salted peanut',variable=var7,onvalue=1,offvalue=0,
                          font=('arial',12,'bold'),bg='powder blue',command=chksalted_peanut).grid(row=6,
                                                                                           sticky=W)
        self.txtsalted_peanut=Entry(ABC3,font=('arial',12,'bold'),textvariable=E_salted_peanut,bd=8,
                            width=20,justify='left',state=DISABLED)
        self.txtsalted_peanut.grid(row=6,column=1)



        self.Diet_mix=Checkbutton(ABC3,text='Diet mix',variable=var8,onvalue=1,offvalue=0,
                          font=('arial',12,'bold'),bg='powder blue',command=chkDiet_mix).grid(row=7,sticky=W)
                                
        self.txtDiet_mix=Entry(ABC3,font=('arial',12,'bold'),textvariable=E_Diet_mix,bd=8,
                            width=20,justify='left',state=DISABLED)
        self.txtDiet_mix.grid(row=7,column=1)


        self.lblspace=Label(ABC3,text='Tax and Total sum',font=('arial',18,'bold'),pady=1,bd=9,
                            bg='cadet blue',fg='cornsilk',width=26,justify=CENTER).grid(row=8,column=0,columnspan=4)
        #======================================reciept===================================================
        self.lblPaidTax=Label(ABC3,font=('arial',12,'bold'),text='Paid Tax',bd=7,bg='powder blue',fg='black')
        self.lblPaidTax.grid(row=10,column=0,sticky=W)
        self.txtPaidTax=Entry(ABC3,font=('arial',12,'bold'),textvariable=PaidTax,bd=7,bg='white',width=20,justify=LEFT)
        self.txtPaidTax.grid(row=10,column=1)

        self.lblSubTotal=Label(ABC3,font=('arial',12,'bold'),text='Sub Total',bd=7,bg='powder blue',fg='black')
        self.lblSubTotal.grid(row=11,column=0,sticky=W)
        self.txtSubTotal=Entry(ABC3,font=('arial',12,'bold'),textvariable=SubTotal,bd=7,bg='white',width=20,justify=LEFT)
        self.txtSubTotal.grid(row=11,column=1)

        self.lblTotalCost=Label(ABC3,font=('arial',12,'bold'),text='TotalCost',bd=7,bg='powder blue',fg='black')
        self.lblTotalCost.grid(row=12,column=0,sticky=W)
        self.txtTotalCost=Entry(ABC3,font=('arial',12,'bold'),textvariable=TotalCost,bd=7,bg='white',width=20,justify=LEFT)
        self.txtTotalCost.grid(row=12,column=1)
        
        
        #==============================================================================================
        
        #==============================================================================================
        selfbtnTotal=Button(ABC6,padx=14,pady=7,bd=5,fg='cornsilk',font=('Arial',16,'bold'),width=5,
                            height=2,text='Total',command=costofitems,bg='black').grid(row=0,column=0)

        selfbtnReset=Button(ABC6,padx=14,pady=7,bd=5,fg='cornsilk',font=('Arial',16,'bold'),width=5,
                            height=2,text='Reset',command=Reset,bg='black').grid(row=0,column=1)

        selfbtnExit=Button(ABC6,padx=14,pady=7,bd=5,fg='cornsilk',font=('Arial',16,'bold'),width=5,
                            height=2,text='Exit',command=iExit,bg='black').grid(row=0,column=2)
        #==============================================================================================



if __name__=="__main__":
    root=Tk()
    application=customer(root)
    root.mainloop()
