from tkinter import *
screen = Tk()
screen.title("J_Calculator")
screen.geometry('400x520')
def click(number):
    global operator
    operator += str(number)
    tex.set(operator)

def clear():
    global operator
    operator = ''
    tex.set(operator)

def equal():
    global operator
    result = eval(operator)    # eval function used for evaluation
    operator = str(result)
    tex.set(result)


def on_entry(a):
        entry1.configure(bg='yellow')
def leave_entry1(a):
    entry1.configure(bg='orange')


def on_enter7(a):
    btn7.configure(bg='pink')
def leave7(a):
    btn7.configure(bg='light green')

def on_enter8(a):
    btn8.configure(bg='pink')
def leave8(a):
    btn8.configure(bg='light green')
def on_enter9(a):
    btn9.configure(bg='pink')
def leave9(a):
    btn9.configure(bg='light green')
def on_enteradd(a):
        btnadd.configure(bg='pink')
def leaveadd(a):
        btnadd.configure(bg='light green')
def on_enter4(a):
        btn4.configure(bg='pink')
def leave4(a):
        btn4.configure(bg='light green')
def on_enter3(a):
        btn3.configure(bg='pink')
def leave3(a):
        btn3.configure(bg='light green')
def on_enter2(a):
        btn2.configure(bg='pink')

def leave2(a):
        btn2.configure(bg='light green')

def on_entersub(a):
        btnsub.configure(bg='pink')

def leavesub(a):
        btnsub.configure(bg='light green')

def on_enter1(a):
        btn1.configure(bg='pink')

def leave1(a):
        btn1.configure(bg='light green')

def on_enter5(a):
        btn5.configure(bg='pink')

def leave5(a):
        btn5.configure(bg='light green')

def on_enter6(a):
        btn6.configure(bg='pink')

def leave6(a):
        btn6.configure(bg='light green')

def on_entermul(a):
        btnmul.configure(bg='pink')

def leavemul(a):
        btnmul.configure(bg='light green')

def on_enter0(a):
        btn0.configure(bg='pink')

def leave0(a):
        btn0.configure(bg='light green')

def on_enterclr(a):
        btnclr.configure(bg='pink')
def leaveclr(a):
        btnclr.configure(bg='light green')
def on_enterdiv(a):
        btndiv.configure(bg='pink')
def leavediv(a):
        btndiv.configure(bg='light green')
def on_enter_equal(a):
        btnequal.configure(bg='pink')

def on_leave_equal(a):
        btnequal.configure(bg='light green')


tex = StringVar()
operator = ''

entry1 = Entry(screen, bg='orange', font = ('arial', '25'), bd="20", justify='right', textvariable=tex)
entry1.grid(row=0, columnspan=4)

btn7 = Button(screen, text='7', font=('arial', '25', 'italic bold'), bg='light green', bd='8', padx='15', pady='15', command = lambda:click(7), activebackground='light blue',
              activeforeground='white')
btn7.grid(row=1, column=0)

btn8 = Button(screen, text='8', font=('arial', '25', 'italic bold'), bg='light green', bd='8', padx='15', pady='15', command=lambda:click(8), activebackground='light blue',
              activeforeground='white')
btn8.grid(row=1, column=1)

btn9 = Button(screen, text='9', font=('arial', '25', 'italic bold'), bg='light green', bd='8', padx='15', pady='15', command=lambda:click(9), activebackground='light blue',
              activeforeground='white')
btn9.grid(row=1, column=2)

btnadd = Button(screen, text='+', font=('arial', ' 25', 'italic bold'), bg='light green', bd='8', padx='15', pady='15', command=lambda:click('+'), activebackground='light blue',
              activeforeground='white')

btnadd.grid(row=1, column=3)
btn4 = Button(screen, text='4', font=('arial', '25', 'italic bold'), bg='light green', bd='8', padx='15', pady='15', command=lambda:click(4), activebackground='light blue',
              activeforeground='white')
btn4.grid(row=2, column=0)

btn5 = Button(screen, text='5', font=('arial', '25', 'italic bold'), bg='light green', bd='8', padx='15', pady='15', command=lambda:click(5), activebackground='light blue',
              activeforeground='white')
btn5.grid(row=2, column=1)

btn6 = Button(screen, text='6', font=('arial', '25', 'italic bold'), bg='light green', bd='8', padx='15', pady='15', command=lambda:click(6), activebackground='light blue',
              activeforeground='white')
btn6.grid(row=2, column=2)

btnsub = Button(screen, text='-', font=('arial', '25', 'italic bold'), bg='light green', bd='8', padx='18', pady='15', command=lambda:click('-'), activebackground='light blue',
              activeforeground='white')
btnsub.grid(row=2, column=3)

btn1 = Button(screen, text='1', font=('arial', '25', 'italic bold'), bg='light green', bd='8', padx='15', pady='15', command=lambda:click(1), activebackground='light blue',
              activeforeground='white')
btn1.grid(row=3, column=0)

btn2 = Button(screen, text='2', font=('arial', '25', 'italic bold'), bg='light green', bd='8', padx='15', pady='15', command=lambda:click(2), activebackground='light blue',
              activeforeground='white')
btn2.grid(row=3, column=1)

btn3 = Button(screen, text='3', font=('arial', '25', 'italic bold'), bg='light green', bd='8', padx='15', pady='15', command=lambda:click(3), activebackground='light blue',
              activeforeground='white')
btn3.grid(row=3, column=2)

btnmul = Button(screen, text='x', font=('arial', '25', 'italic bold'), bg='light green', bd='8', padx='14', pady='15', command=lambda:click('*'), activebackground='light blue',
              activeforeground='white')
btnmul.grid(row=3, column=3)

btn0 = Button(screen, text='0', font=('arial', '25', 'italic bold'), bg='light green', bd='8', padx='15', pady='15', command=lambda:click(0), activebackground='light blue',
              activeforeground='white')
btn0.grid(row=4, column=0)

btnclr= Button(screen, text='c', font=('arial', '25', 'italic bold'), bg='light green', bd='8', padx='15', pady='15', command=lambda: clear(), activebackground='light blue',
              activeforeground='white')
btnclr.grid(row=4, column=1)

btnequal = Button(screen, text='=', font=('arial', '25', 'italic bold'), bg='light green', bd='8', padx='15', pady='15',command=lambda: equal(), activebackground='light blue',
              activeforeground='white')
btnequal.grid(row=4, column=2)

btndiv = Button(screen, text='/ ', font=('arial', '25', 'italic bold'), bg='light green', bd='8', padx='15', pady='15', command=lambda:click('/'), activebackground='light blue',
              activeforeground='white')
btndiv.grid(row=4, column=3)
########################################Binding
btn7.bind('<Enter>', on_enter7)
btn7.bind('<Leave>', leave7)

btn8.bind('<Enter>', on_enter8)
btn8.bind('<Leave>', leave8)

btn9.bind('<Enter>', on_enter9)
btn9.bind('<Leave>', leave9)

btnadd.bind('<Enter>', on_enteradd)
btnadd.bind('<Leave>', leaveadd)

btn6.bind('<Enter>', on_enter6)
btn6.bind('<Leave>', leave6)

btn5.bind('<Enter>', on_enter5)
btn5.bind('<Leave>', leave5)

btn4.bind('<Enter>', on_enter4)
btn4.bind('<Leave>', leave4)

btnsub.bind('<Enter>', on_entersub)
btnsub.bind('<Leave>', leavesub)

btn1.bind('<Enter>', on_enter1)
btn1.bind('<Leave>', leave1)

btn3.bind('<Enter>', on_enter3)
btn3.bind('<Leave>', leave3)

btn2.bind('<Enter>', on_enter2)
btn2.bind('<Leave>', leave2)

btnmul.bind('<Enter>', on_entermul)
btnmul.bind('<Leave>', leavemul)

btn0.bind('<Enter>', on_enter0)
btn0.bind('<Leave>', leave0)

btndiv.bind('<Enter>', on_enterdiv)
btndiv.bind('<Leave>', leavediv)

btnclr.bind('<Enter>', on_enterclr)
btnclr.bind('<Leave>', leaveclr)

btnequal.bind('<Enter>', on_enter_equal)
btnequal.bind('<Leave>', on_leave_equal)

entry1.bind('<Enter>', on_entry)
entry1.bind('<Leave>', leave_entry1)
screen.mainloop()