import tkinter as tk
from tkinter import messagebox
import time

current_balance = 15000

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data = {'Balance':tk.IntVar()}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage, WithdrawPage, DepositPage, BalancePage , ChangePinPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

pin = '123'

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#1E6068')
        self.controller = controller

        self.controller.title('BSI CORPORATION')
        self.controller.state('zoomed')
        #self.controller.iconphoto(False,tk.PhotoImage(file='C:/Users/urban boutique/Documents/atm tutorial/atm.png'))

        heading_label = tk.Label(self,
                                                     text='BSI ATM',
                                                     font=('orbitron',60,'bold'),
                                                     foreground='#FF5733',
                                                     background='#1E6068')
        heading_label.pack(pady=25)

        space_label = tk.Label(self,height=4,bg='#1E6068')
        space_label.pack()

        password_label = tk.Label(self,
                                                      text='Enter your password',
                                                      font=('orbitron',14),
                                                      bg='#1E6068',
                                                      fg='white')
        password_label.pack(pady=10)

        my_password = tk.StringVar()
        password_entry_box = tk.Entry(self,
                                                              textvariable=my_password,
                                                              font=('orbitron',14),
                                                              width=20)
        password_entry_box.focus_set()
        password_entry_box.pack(ipady=7)

        def handle_focus_in(_):
            password_entry_box.configure(fg='black',show='*')
            
        password_entry_box.bind('<FocusIn>',handle_focus_in)

        def check_password():
           if my_password.get() == pin:
               my_password.set('')
               incorrect_password_label['text']=''
               controller.show_frame('MenuPage')
           else:
               incorrect_password_label['text']='INCORRECT PASSWORD'
                
        enter_button = tk.Button(self,
                                                     text='Enter',
                                                     command=check_password,
                                                     relief='raised',
                                                     borderwidth = 3,
                                                     width=30,
                                                     height=2)
        enter_button.pack(pady=10)

        incorrect_password_label = tk.Label(self,
                                                                        text='',
                                                                        font=('orbitron',13),
                                                                        fg='white',
                                                                        bg='#1E6068',
                                                                        anchor='n')
        incorrect_password_label.pack(fill='both',expand=True)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')


class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#1E6068')
        self.controller = controller
   
        heading_label = tk.Label(self,
                                                     text='BSI ATM',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#FF5733',
                                                     background='#1E6068')
        heading_label.pack(pady=25)

        main_menu_label = tk.Label(self,
                                                           text='Main Menu',
                                                           font=('orbitron',20),
                                                           fg='yellow',
                                                           bg='#1E6068')
        main_menu_label.pack()

        selection_label = tk.Label(self,
                                                           text='PLEASE MAKE A SELECTION',
                                                           font=('orbitron',20),
                                                           fg='light blue',
                                                           bg='#1E6068',
                                                           anchor='w')
        selection_label.pack(fill='x',padx=555)

        button_frame = tk.Frame(self,bg='#1E6068')
        button_frame.pack(fill='both',expand=True)

        def withdraw():
            controller.show_frame('WithdrawPage')
            
        withdraw_button = tk.Button(button_frame,
                                                            text='WITHDRAW',
                                                            command=withdraw,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=50,
                                                            height=5)
        withdraw_button.grid(row=0,column=0,pady=10,padx=150)

        def deposit():
            controller.show_frame('DepositPage')
            
        deposit_button = tk.Button(button_frame,
                                                            text='DEPOSIT',
                                                            command=deposit,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=50,
                                                            height=5)
        deposit_button.grid(row=1,column=0,pady=10,padx=150)

        def balance():
            controller.show_frame('BalancePage')
            
        balance_button = tk.Button(button_frame,
                                                            text='CHECK BALANCE',
                                                            command=balance,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=50,
                                                            height=5)
        balance_button.grid(row=0,column=1,pady=10,padx=250)

        def changepin():
            controller.show_frame('ChangePinPage')
            
        changepin_button = tk.Button(button_frame,
                                                            text='CHANGE PIN',
                                                            command=changepin,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=50,
                                                            height=5)
        changepin_button.grid(row=1,column=1,pady=10,padx=250)

        def exit():
            controller.show_frame('StartPage')
            
        exit_button = tk.Button(button_frame,
                                                            text='EXIT',
                                                            command=exit,
                                                            relief='raised',
                                                            borderwidth=3,
                                                            width=50,
                                                            height=5)
        exit_button.grid(row=2,column=0,pady=10,padx=150)


        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')


class WithdrawPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#1E6068')
        self.controller = controller


        heading_label = tk.Label(self,
                                                     text='BSI ATM',
                                                     font=('orbitron',60,'bold'),
                                                     foreground='#FF5733',
                                                     background='#1E6068')
        heading_label.pack(pady=25)

        choose_amount_label = tk.Label(self,
                                                           text='Choose the amount you want to withdraw',
                                                           font=('orbitron',25),
                                                           fg='white',
                                                           bg='#1E6068')
        choose_amount_label.pack()

        button_frame = tk.Frame(self,bg='#1E6068')
        button_frame.pack(fill='both',expand=True)

        def withdraw(amount):
            global current_balance
            if int(amount)>current_balance:
                messagebox.showinfo(title='Check Balance', message='INSUFFICIENT BALANCE')
                return
            current_balance -= amount
            messagebox.showinfo(title='Withdrawn', message='MONEY SUCCESSFULLY WITHDRAWN')
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')
            
        hundred_button = tk.Button(button_frame,
                                                       text='100',
                                                       command=lambda:withdraw(100),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=50,
                                                       height=5)
        hundred_button.grid(row=0,column=0,pady=5)

        twohundred_button = tk.Button(button_frame,
                                                       text='200',
                                                       command=lambda:withdraw(200),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=50,
                                                       height=5)
        twohundred_button.grid(row=1,column=0,pady=5)

        fivehundred_button = tk.Button(button_frame,
                                                       text='500',
                                                       command=lambda:withdraw(500),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=50,
                                                       height=5)
        fivehundred_button.grid(row=2,column=0,pady=5)

        onethousand_button = tk.Button(button_frame,
                                                       text='1000',
                                                       command=lambda:withdraw(1000),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=50,
                                                       height=5)
        onethousand_button.grid(row=0,column=1,pady=5,padx=800)

        twothousand_button = tk.Button(button_frame,
                                                       text='2000',
                                                       command=lambda:withdraw(2000),
                                                       relief='raised',
                                                       borderwidth=3,
                                                       width=50,
                                                       height=5)
        twothousand_button.grid(row=1,column=1,pady=5,padx=800)

        cash = tk.StringVar()
        other_amount_entry = tk.Entry(button_frame,
                                                              textvariable=cash,
                                                              width=59,
                                                              justify='right')
        other_amount_entry.grid(row=2,column=1,pady=5,ipady=30)

        def other_amount(_):
            global current_balance
            if int(cash.get())>current_balance:
                messagebox.showinfo(title='Check Balance', message='INSUFFICIENT BALANCE')
                return
            current_balance -= int(cash.get())
            messagebox.showinfo(title='Withdrawn', message='MONEY SUCCESSFULLY WITHDRAWN')
            controller.shared_data['Balance'].set(current_balance)
            cash.set('')
            controller.show_frame('MenuPage')
            
        other_amount_entry.bind('<Return>',other_amount)

        def menu():
            controller.show_frame('MenuPage')

        menu_button = tk.Button(button_frame,
                                                    command=menu,
                                                    text='Menu',
                                                    relief='raised',
                                                    borderwidth=3,
                                                    width=50,
                                                    height=5)
        menu_button.grid(row=3,column=0,pady=5)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')       

class DepositPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#1E6068')
        self.controller = controller

        heading_label = tk.Label(self,
                                                     text='BSI ATM',
                                                     font=('orbitron',60,'bold'),
                                                     foreground='#FF5733',
                                                     background='#1E6068')
        heading_label.pack(pady=25)

        space_label = tk.Label(self,height=4,bg='#1E6068')
        space_label.pack()

        enter_amount_label = tk.Label(self,
                                                      text='Enter amount',
                                                      font=('orbitron',25),
                                                      bg='#1E6068',
                                                      fg='white')
        enter_amount_label.pack(pady=10)

        cash = tk.StringVar()
        deposit_entry = tk.Entry(self,
                                                  textvariable=cash,
                                                  font=('orbitron',12),
                                                  width=22)
        deposit_entry.pack(ipady=7)

        def deposit_cash():
            global current_balance
            current_balance += int(cash.get())
            messagebox.showinfo(title='Money Deposited', message='MONEY SUCCESSFULLY DEPOSITED')
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')
            cash.set('')
            
        enter_button = tk.Button(self,
                                                     text='Enter',
                                                     command=deposit_cash,
                                                     relief='raised',
                                                     borderwidth=3,
                                                     width=30,
                                                     height=2)
        enter_button.pack(pady=10)

        button_frame = tk.Frame(self,bg='#1E6068')
        button_frame.pack(fill='both',expand=True)

        def menu():
            controller.show_frame('MenuPage')

        menu_button = tk.Button(button_frame,
                                                    command=menu,
                                                    text='Menu',
                                                    relief='raised',
                                                    borderwidth=3,
                                                    width=30,
                                                    height=2)
        menu_button.grid(row=6,column=0,pady=10,padx=657)

        two_tone_label = tk.Label(self,bg='#1E6068')
        two_tone_label.pack(fill='both',expand=True)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

class BalancePage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#1E6068')
        self.controller = controller

        
        heading_label = tk.Label(self,
                                                     text='BSI ATM',
                                                     font=('orbitron',60,'bold'),
                                                     foreground='#FF5733',
                                                     background='#1E6068')
        heading_label.pack(pady=25)

        global current_balance
        controller.shared_data['Balance'].set(current_balance)
        balance_label = tk.Label(self,
                                                  textvariable=controller.shared_data['Balance'],
                                                  font=('orbitron',60),
                                                  fg='#F06DF6',
                                                  bg='#1E6068',
                                                  anchor='w')
        balance_label.pack(fill='x')

        button_frame = tk.Frame(self,bg='#1E6068')
        button_frame.pack(fill='both',expand=True)

        def menu():
            controller.show_frame('MenuPage')
            
        menu_button = tk.Button(button_frame,
                                                    command=menu,
                                                    text='Menu',
                                                    relief='raised',
                                                    borderwidth=3,
                                                    width=50,
                                                    height=5)
        menu_button.grid(row=4,column=0,pady=10)

        def exit():
            controller.show_frame('StartPage')
            
        exit_button = tk.Button(button_frame,
                                                 text='Exit',
                                                 command=exit,
                                                 relief='raised',
                                                 borderwidth=3,
                                                 width=50,
                                                 height=5)
        exit_button.grid(row=5,column=0,pady=10)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

class ChangePinPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#1E6068')
        self.controller = controller

        heading_label = tk.Label(self,
                                                     text='BSI ATM',
                                                     font=('orbitron',60,'bold'),
                                                     foreground='#FF5733',
                                                     background='#1E6068')
        heading_label.pack(pady=25)

        new_pin_label = tk.Label(self,
                                                           text='ENTER OLD PIN TO CHANGE PIN',
                                                           font=('orbitron',30),
                                                           fg='white',
                                                           bg='#1E6068')
        new_pin_label.pack()

        button_frame = tk.Frame(self,bg='#1E6068')
        button_frame.pack(fill='both',expand=True)


        def menu():
            controller.show_frame('MenuPage')

        def newPin():
            global pin;
            oldpin=oldPasswordEntry.get()
            newpin=newPasswordEntry.get()
            renewpin=renewPasswordEntry.get()
            if oldpin==pin:
                if newpin==renewpin:
                    pin=newpin
                    controller.show_frame('StartPage')
                else:
                    messagebox.showinfo(title='Check Please', message='NEW PASSWORDS DO NOT MATCH')
            else:
                messagebox.showinfo(title='Wrong Password', message='INCORRECT OLD PASSWORD')

        oldPassword = tk.Label(button_frame, text="YOUR OLD PASSWORD",font=('orbitron',15),fg='yellow',bg='#1E6068')
        oldPassword.grid(row=2,column=0,pady=5)
        oldPasswordEntry = tk.Entry(button_frame, width=20, bd=1,font=('Arial 24'))
        oldPasswordEntry.grid(row=3,column=0,pady=5)

        EmptyField = tk.Label(button_frame, text="",bg='#1E6068')
        EmptyField.grid(row=4,column=0,pady=5)

        newPassword = tk.Label(button_frame, text="YOUR NEW PASSWORD",font=('orbitron',15),fg='yellow',bg='#1E6068')
        newPassword.grid(row=5,column=0,pady=5)
        newPasswordEntry = tk.Entry(button_frame, width=20, bd=1,font=('Arial 24'))
        newPasswordEntry.grid(row=6,column=0,pady=5)

        EmptyField2 = tk.Label(button_frame, text="",bg='#1E6068')
        EmptyField2.grid(row=7,column=0,pady=5)

        renewPassword = tk.Label(button_frame, text="RE-ENTER NEW PASSWORD",font=('orbitron',15),fg='yellow',bg='#1E6068')
        renewPassword.grid(row=8,column=0,pady=5)
        renewPasswordEntry = tk.Entry(button_frame, width=20, bd=1,font=('Arial 24'))
        renewPasswordEntry.grid(row=9,column=0,pady=5)

        EmptyField2 = tk.Label(button_frame, text="",bg='#1E6068')
        EmptyField2.grid(row=10,column=0,pady=5)

        changepin_button = tk.Button(button_frame,
                                                    command=newPin,
                                                    text='Change Password',
                                                    relief='raised',
                                                    borderwidth=3,
                                                    width=50,
                                                    height=5)
        changepin_button.grid(row=13,column=0,pady=5)

        menu_button = tk.Button(button_frame,
                                                    command=menu,
                                                    text='Menu',
                                                    relief='raised',
                                                    borderwidth=3,
                                                    width=50,
                                                    height=5)
        menu_button.grid(row=14,column=0,pady=5)



        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
  

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
