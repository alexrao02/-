import catch
import tkinter as tk
import algorithm

def get_user_songlist(uid):
    return catch.catch_songlist(uid)

def func1():
    window = tk.Tk()
    window.title('歌单获取')
    window.geometry('500x300')
    l = tk.Label(window, text='输入用户的uid以获取其歌单', bg='white', font=('Arial', 20), width=30, height=2)
    l.pack()
    e = tk.Entry(window, show=None)
    e.pack()
    def dis_songlist():
        t.delete('1.0', 'end')
        var = e.get()
        # songli = get_user_songlist(var)
        # for i in songli:
        #     print(i)
        #     t.insert('insert', i)
        #     t.insert('insert', '\n')
        # songli.clear()
        for i in get_user_songlist(var):
            t.insert('insert', '                        ' +i)
            t.insert('insert', '\n')


    def insert_songlist():
        t.delete('1.0', 'end')
        var = e.get()
        algorithm.insert(get_user_songlist(var))
        t.insert('insert', '                           该用户的歌单已成功提交至后台。')


    def put():
        t.delete('1.0', 'end')
        t.insert('insert', algorithm.put())

    b1 = tk.Button(window, text='预览歌单', width=10,
                   height=2, command=dis_songlist)
    b1.pack()
    b2 = tk.Button(window, text='提交歌单', width=10,
                   height=2, command=insert_songlist)
    b2.pack()
    b3 = tk.Button(window, text='完成', width=10,
                   height=2, command=put)
    b3.pack()
    t = tk.Text(window, height=50)
    t.pack()


    window.mainloop()



def func2():

    window2 = tk.Tk()
    window2.title('歌单匹配度算法')
    window2.geometry('500x300')



    def matching():
        u1 = uide1.get()
        u2 = uide2.get()
        u1list = get_user_songlist(u1)
        u2list = get_user_songlist(u2)
        r = algorithm.findMatchPercent(u1list, u2list) * 100
        res = '                      两位用户的歌单匹配度为%f' % (r)
        t.insert('insert', res)
        t.insert('insert', '%')
        t.insert('insert', '\n')
        t.insert('insert', '\n')
        t.insert('insert', '                      两位用户歌单中重复的歌曲有:')
        t.insert('insert', '\n')
        for i in algorithm.song_repeat:
            t.insert('insert', '                      ')
            t.insert('insert', i)
            t.insert('insert', '\n')

    uidt1 = tk.Label(window2, text='请输入第1位用户的uid', bg='white', fg='black', font=('Arial', 12), width=30, height=2)
    uidt1.pack()
    uide1 = tk.Entry(window2, show=None)
    uide1.pack()
    uidt2 = tk.Label(window2, text='请输入第2位用户的uid', bg='white', fg='black', font=('Arial', 12), width=30, height=2)
    uidt2.pack()
    uide2 = tk.Entry(window2, show=None)
    uide2.pack()
    uidsubmit = tk.Button(window2, text='计算匹配度', width=10,
                   height=2, command=matching)
    uidsubmit.pack()
    t = tk.Text(window2, height=50)
    t.pack()



def func3():
    window3 = tk.Tk()
    window3.title('歌单变换算法')
    window3.geometry('500x300')

    def changing():
        t.delete('1.0', 'end')
        u1 = uide1.get()
        u2 = uide2.get()
        u1list = get_user_songlist(u1)
        u2list = get_user_songlist(u2)
        r = algorithm.listChange(u1list, u2list)
        res = '                      歌单改变的最少匹配次数为%f' % (r)
        t.insert('insert', res)

    uidt1 = tk.Label(window3, text='请输入第1位用户的uid', bg='white', fg='black', font=('Arial', 12), width=30, height=2)
    uidt1.pack()
    uide1 = tk.Entry(window3, show=None)
    uide1.pack()
    uidt2 = tk.Label(window3, text='请输入第2位用户的uid', bg='white', fg='black', font=('Arial', 12), width=30, height=2)
    uidt2.pack()
    uide2 = tk.Entry(window3, show=None)
    uide2.pack()
    uidsubmit = tk.Button(window3, text='计算最少的变换次数', width=15,
                          height=2, command=changing)
    uidsubmit.pack()
    t = tk.Text(window3, height=50)
    t.pack()



def ui():
    mainwindow = tk.Tk()
    mainwindow.title('歌曲推荐和歌单匹配度算法演示')
    mainwindow.geometry('500x300')
    ti = tk.Label(mainwindow, text='Welcome', bg='white', fg='black', font=('Arial', 12), width=30, height=2)
    ti.pack()

    b1 = tk.Button(mainwindow, text='基于用户数据的歌曲推荐', width=25,
                   height=2, command=func1)
    b1.pack()
    b2 = tk.Button(mainwindow, text='用户歌单匹配度计算', width=25,
                   height=2, command=func2)
    b2.pack()
    b3 = tk.Button(mainwindow, text='计算用户歌单的最少改变次数', width=25,
                   height=2, command=func3)
    b3.pack()
    mainwindow.mainloop()





