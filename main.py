
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sys
from Scripts.Show_Net import Show_Net as show_network_devices
from Scripts.Add_User import Add_User
from Scripts.Users_Manager import *
from Scripts.Del_Net import Del_Net


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Cisco DNA Center")
        self.geometry("500x500")
        self.resizable(False, False)
        self._frame = None
        self.switch_frame(LoginPage)
        #color everything in the same color
        self.configure(bg="dark slate gray")
        
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

#create a login page before the start page 
class LoginPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Login") #type:ignore
        self.master.geometry("500x200") #type:ignore
        self.master.resizable(False, False) #type:ignore
        self.configure(bg="dark slate gray")
        self.create_widgets()


    def create_widgets(self):
        #make the login page look nice
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.username_label = tk.Label(self, text="Username", font=('Helvetica', 15), bg="dark slate gray", fg="white")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self, textvariable=self.username, font=("Arial", 15))
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)
        self.password_label = tk.Label(self, text="Password", font=('Helvetica', 15), bg="dark slate gray", fg="white")
        self.password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self, textvariable=self.password, font=('Helvetica', 15), show="•")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)
        self.login_button = tk.Button(self,width=20, text="Login", font=('Helvetica', 12,"bold"), command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=10, padx=10, pady=20)
    
    def login(self):
        #verify the user
        username = self.username.get()
        password = self.password.get()
        if Verify_User(username, password) == False: 
            messagebox.showerror("Error", "Invalid username or password")
        else:
            self.master.switch_frame(StartPage) #type:ignore
            # resizew the StartPage window
            self.master.geometry("500x450") #type:ignore


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Welcome to Cisco DNA Center", font=('Helvetica', 18, "bold"),bg="dark slate gray",fg="white").pack(side="top", fill="x", pady=10)
        #adding a button to the frame to show network devices in the same frame
        tk.Button(self, text="Show Network Devices", command=lambda: master.switch_frame(PageOne)).pack(side="top", fill="x", pady=10)
        #adding a button to the frame to add a user in the same frame
        tk.Button(self, text="Add User", command=lambda: master.switch_frame(PageThree)).pack(side="top", fill="x", pady=10)
        #adding a button to the frame to Users Manager in the same frame
        tk.Button(self, text="Users Manager", command=lambda: master.switch_frame(PageFour)).pack(side="top", fill="x", pady=10)
        #adding a button to the frame to delete a network in the same frame
        tk.Button(self, text="Delete Network", command=lambda: master.switch_frame(PageFive)).pack(side="top", fill="x", pady=10)
        E_A_frame=tk.Frame(self, bg="dark slate gray")
        E_A_frame.pack(side="top", fill="x", pady=60)
        tk.Button(E_A_frame, text="About", command=lambda: messagebox.showinfo("About","This program was created by Ilyes Benaissa\n2021-2022")).pack(side="top", fill="x", pady=5)
        #adding Exit button to the frame to exit the program
        tk.Button(E_A_frame, text="Exit", command=lambda: sys.exit()).pack(side="top", fill="both", pady=10)
        self.configure(bg="dark slate gray")



class Redirect():
    def __init__(self, widget):
        self.widget = widget
    def write(self, text):
        self.widget.insert('end', text)
        #add a scroll bar to the frame
        self.widget.see('end')
        self.widget.update_idletasks()
        self.widget.config(state='disabled')


class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="Back to Home", command=lambda: master.switch_frame(StartPage)).pack(
            side="top", fill="x", pady=10, padx=200) 
        #add output to the frame
        tk.Label(self, text="Network Devices", bg="dark slate gray",fg="dark slate gray",font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=10)
        #redirecting the output to a widget in the frame
        output = Text(self, width=100, height=25)
        output.pack()
        sys.stdout = Redirect(output)
        show_network_devices()
        self.configure(bg="dark slate gray")





class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg="dark slate gray")
        tk.Button(self, text="Back to Home", command=lambda: master.switch_frame(StartPage)).pack(
            side="top", fill="x", pady=10, padx=200)
        #add a field to enter the username
        tk.Label(self, text="Username", fg="white",bg="dark slate gray",font=('Helvetica', 12, "bold")).pack(side="top", fill="x", pady=5)
        username = tk.Entry(self, width=50)
        username.pack()
        #field to enter the password label on the left and the field on the right
        tk.Label(self, text="Password",fg="white",bg="dark slate gray", font=('Helvetica', 12, "bold")).pack(side="top", fill="x", pady=10)
        password = tk.Entry(self, width=50)
        password.pack()
    
        #tk.Label(self).pack()
        tk.Label(self, text="Select a role", fg="white",bg="dark slate gray",font=('Helvetica', 12, "bold")).pack(side="top", fill="x", pady=5)
        role = tk.StringVar(self)
        role.set("Select a role")
        role_list = ["ROLE_ADMIN", "ROLE_INSTALLER", "ROLE_OBSERVER"]
        role_menu = tk.OptionMenu(self, role, *role_list)
        role_menu.pack(side="top", fill="x", pady=5)

        #user and button frame
        frame = tk.Frame(self,pady=15, bg="dark slate gray")
        frame.pack()
        tk.Button(frame, text="Add User", command=lambda: Add_User(username.get(), password.get(), role.get())).pack(
            side="left", fill="x",padx=10)
        tk.Button(frame, text="Refresh", command=lambda: master.switch_frame(PageThree)).pack(
            side="left", fill="x")
        #add output to the frame
        output = Text(self, width=100, height=25)
        output.pack()
        sys.stdout = Redirect(output)
        
#make a new page for the users manager
class PageFour(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #create a frame to put two buttons in the same row
        frame = tk.Frame(self,pady=5,bg="dark slate gray")
        frame.pack(fill="x",side="top")
        tk.Button(frame, text="Back to Home", command=lambda: master.switch_frame(StartPage)).pack(
            side="top", fill="x", pady=0, padx=200)
        #add a field to enter the username
        tk.Label(frame, text="Enter Username",bg="dark slate gray",fg="white",font=('Helvetica', 12, "bold")).pack(side="top", fill="x", pady=10)
        username = tk.Entry(frame, width=50)
        username.pack(pady=10)
        tk.Button(frame, text="Delete User", command=lambda: Delete_User(username.get())).pack(
            side="left", fill="x",padx=120)
        tk.Button(frame, text="Refresh", command=lambda: master.switch_frame(PageFour)).pack(
            side="left", fill="x")
        #another frame2 to get the users
        frame2 = tk.Frame(self,pady=25,bg="dark slate gray")
        frame2.pack()
        tk.Button(frame2, text="Get Users", command=lambda: Get_Users()).pack(pady=10,side="top", fill="y")
        output2 = Text(frame2, width=100, height=10)
        #adding scroll bar to the frame
        scroll = Scrollbar(frame2, command=output2.yview)
        output2.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right",fill="y")
        output2.pack()
        sys.stdout = Redirect(output2)
        
#make a new page for deleting the network devices
class PageFive(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #create a frame to put two buttons in the same row
        frame = tk.Frame(self,pady=5,bg="dark slate gray")
        frame.pack(fill="x",side="top")
        tk.Button(frame, text="Back to Home", command=lambda: master.switch_frame(StartPage)).pack(
            side="top", fill="x", pady=0, padx=200)
        #add a field to enter the username
        tk.Label(frame, text="Enter Network ID, example: 192.168.1.0",bg="dark slate gray",fg="white",font=('Helvetica', 12, "bold")).pack(side="top", fill="x", pady=10)
        device_name = tk.Entry(frame, width=50)
        device_name.pack(pady=10)
        tk.Button(frame, text="Delete Network", command=lambda: Del_Net(device_name.get())).pack(
            side="left", fill="x",padx=120)
        tk.Button(frame, text="Refresh", command=lambda: master.switch_frame(PageFive)).pack(
            side="left", fill="x")
        #add an updating output
        output = Text(self, width=100, height=25)
        output.pack()
        sys.stdout = Redirect(output)

if __name__ == "__main__":
    app = App()
    app.mainloop()