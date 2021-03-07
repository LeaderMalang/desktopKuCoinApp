import tkinter as tk
from tkinter import ttk
from tkinter import*
from db import DB
from kuCoin import KUCoin
 
LARGEFONT =("Verdana", 35)
  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        menu=tk.Menu(self)
        self.config(menu=menu)
        subMenu=tk.Menu(menu)
        menu.add_cascade(label="File",menu=subMenu)
        # creating a container
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True) 
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {}  
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with 
            # for loop
            self.frames[F] = frame 
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class StartPage(tk.Frame):
    global balance_percent_value
    global pair_value
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="Create Market Order", font = LARGEFONT)

        self.balance_percent_value=IntVar()
        self.pair_value=StringVar()
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 2, padx = 10, pady = 10)
        balance_percent=Entry(self, width=15,textvariable=self.balance_percent_value, font="Calibri 10")
        balance_percent_label=ttk.Label(self,text="Balance Percent", font="Calibri 10")
        balance_percent_label.grid(row=1,column=2,padx = 10, pady = 10)
        balance_percent.grid(row=1,column=3,padx = 10, pady = 10)

        pair_input=Entry(self,width=15,textvariable=self.pair_value,font="Calibri 10")
        pair_label=ttk.Label(self,text="Coin Name",font="Calibri 10")
        pair_input.grid(row=2,column=3, padx = 10, pady = 10)
        pair_label.grid(row=2,column=2, padx = 10, pady = 10)
        create_order_button=ttk.Button(self,text="Create Order",command=self.getVals)
        create_order_button.grid(row=3,column=3, padx = 10, pady = 10)

        controller.bind('<Return>',lambda event=None:create_order_button.invoke())

        button1 = ttk.Button(self, text ="Api Configuration",
        command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Change Coin",
        command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

    def getVals(self):
        print("Submitting Form")
        currentResponse=str(self.balance_percent_value.get()) +"-"+self.pair_value.get()
        balance_percent=self.balance_percent_value.get()
        pair=self.pair_value.get()
        
        kuCoinClient=KUCoin(balance_percent,pair)
        response=kuCoinClient.create_market_order()

        label = ttk.Label(self, text=response, font=LARGEFONT)
        label.grid(row=5,column=2)

  
          
  
  
# second window frame page1 
class Page1(tk.Frame):
    global api_key_value
    global api_secret_value
    global api_pass_value

    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Api Configuration", font = LARGEFONT)
        label.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.api_key_value = StringVar()
        self.api_secret_value = StringVar()
        self.api_pass_value = StringVar()

        api_key_input = Entry(self, width=15, textvariable=self.api_key_value, font="Calibri 10")
        api_key_label = ttk.Label(self, text="Api Key", font="Calibri 10")
        api_key_label.grid(row=1, column=2, padx=10, pady=10)
        api_key_input.grid(row=1, column=3, padx=10, pady=10)

        api_secret_input = Entry(self, width=15, textvariable=self.api_secret_value, font="Calibri 10")
        api_secret_label = ttk.Label(self, text="Api secret", font="Calibri 10")
        api_secret_input.grid(row=2, column=3, padx=10, pady=10)
        api_secret_label.grid(row=2, column=2, padx=10, pady=10)

        api_pass_input = Entry(self, width=15, textvariable=self.api_pass_value, font="Calibri 10")
        api_pass_label = ttk.Label(self, text="Api pass", font="Calibri 10")
        api_pass_input.grid(row=3, column=3, padx=10, pady=10)
        api_pass_label.grid(row=3, column=2, padx=10, pady=10)

        create_order_button = ttk.Button(self, text="Save",command=self.getvals)
        create_order_button.grid(row=4, column=3, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place 
        # by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Change Coin",
                            command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by 
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
    def getvals(self):
        print("Submitting form")

        print(
            f"{self.api_key_value.get(),self.api_pass_value.get(),self.api_secret_value.get()} ")
        currentResponse=self.api_pass_value.get()+"--"+self.api_key_value.get()+"--"+self.api_secret_value.get()
        print(currentResponse)
        db = DB()
        response=db.insertConfig({"api_key":self.api_key_value.get(),
                             "api_secret":self.api_secret_value.get(),
                             "api_pass":self.api_pass_value.get()
                             })
        label = ttk.Label(self, text=response, font=LARGEFONT)
        label.grid(row=5, column=2)


# third window frame page2
class Page2(tk.Frame):
    global coin_name_value
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Change Coin", font = LARGEFONT)
        label.grid(row = 0, column = 2, padx = 10, pady = 10)
        self.coin_name_value=StringVar()
        coin_name_input = Entry(self, width=15, textvariable=self.coin_name_value, font="Calibri 10")
        coin_name_label = ttk.Label(self, text="Coin Name", font="Calibri 10")
        coin_name_label.grid(row=1, column=2, padx=10, pady=10)
        coin_name_input.grid(row=1, column=3, padx=10, pady=10)

        create_order_button = ttk.Button(self, text="Save",command=self.getvals)
        create_order_button.grid(row=2, column=3, padx=10, pady=10)


        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Api Configuration",
                            command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by 
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Startpage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

    def getvals(self):
        print("Submitting Form")
        currentResponse="Base Coin : "+self.coin_name_value.get()
        print(currentResponse)
        db = DB()

        response=db.insertBaseCoin({"base_coin": self.coin_name_value.get()
                   })
        label = ttk.Label(self, text=response, font=LARGEFONT)
        label.grid(row=5, column=2)


  
  
# Driver Code
app = tkinterApp()
app.mainloop()
