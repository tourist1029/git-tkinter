import tkinter.messagebox
import tkinter as tk

import os
import pickle

#print(os.path)


root = tk.Tk()
root.title('Welcome to Login Window')
root.geometry('450x500')

#welcome image
canvas = tk.Canvas(root, height=200, width=500)
image_file = tk.PhotoImage(file="/Users/daniel/Documents/py/ins.gif")
image = canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack(side='top')

#名字和密码的标签
tk.Label(root, text='User name: ').place(x=50,y=250)
tk.Label(root, text='Passwords: ').place(x=50,y=280)

#用来存储数据的全局变量
var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
var_usr_pwd = tk.StringVar()

#名字和密码的输入框
entry_usr_name = tk.Entry(root, textvariable=var_usr_name)
entry_usr_name.place(x=160,y=250)

entry_usr_pwd = tk.Entry(root, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160,y=280)

#注册和登陆的Button

def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()

    try:
        with open('usr_info.pickle', 'wb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb')as usr_file:
            usrs_info = {'admin:''admin'}
            pickle.dump(usrs_info, usr_file)

    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome', message='How are you: ' + usr_name)
        else:
            tk.messagebox.showerror(message='Error, your password was wrong, try again.')
    else:
        is_sign_up = tk.messagebox.askyesno('Welcome', 'You have not sign up yet, Sign up today?')
        if is_sign_up:
            usr_sign_up()




def usr_sign_up():
    #Toplevel是在现有窗口上再创建一个新的窗口的用法,相当于root的子窗口，然后尅在这个子窗口下再建立新的控件

    def sign_to_Daniel_Python():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn  = new_name.get()
        #打开存储的用户信息文件
        with open('usr_info.pickle', 'wb') as usr_file:
            exit_usr_info = pickle.load(usr_file)
        if np != npf:
            tk.messagebox.showerror('Error', 'Password and confirmpassword must be same!')
        elif nn in exit_usr_info:
            tk.messagebox.showerror('Error','The user has exit, Please, Log in!')
        else:
            exit_usr_info[nn] = np
            with open('usr_info.pickle', 'wb') as usr_file:
                pickle.dump(exit_usr_info, usr_file)
            tk.messagebox.showinfo('Welcome', 'You have successfully signed up')
        window_sing_up.destroy()




    window_sing_up = tk.Toplevel(root)
    window_sing_up.geometry('350x200')
    window_sing_up.title('Sign up window')

    new_name = tk.StringVar()
    new_name.set('example@python.com')

    tk.Label(window_sing_up, text='User name:').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sing_up, textvariable=new_name)
    entry_new_name.place(x=150, y=15)

    new_pwd = tk.StringVar()
    tk.Label(window_sing_up, text='Password:').place(x=10, y=50)
    entry_new_pwd = tk.Entry(window_sing_up, textvariable=new_pwd, show='*')
    entry_new_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sing_up, text='Confirm password:').place(x=10, y=90)
    entry_usr_pwd_confirm = tk.Entry(window_sing_up, textvariable=new_pwd, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)

    btn_confirm_sing_up = tk.Button(window_sing_up, text='Sign up', command=sign_to_Daniel_Python)
    btn_confirm_sing_up.place(x=150, y=130)

btn_login = tk.Button(root, text='Login',command=usr_login)
btn_login.place(x=160, y=360)

btn_sign_up = tk.Button(root, text='Sign up',command=usr_sign_up)
btn_sign_up.place(x=260, y=360)






























root.mainloop()
