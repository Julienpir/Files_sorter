import os
from tkinter import *
from datetime import datetime
import operator
import shutil

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

class file(object):

    def __init__(self, name, Path, path_data, path_result, dic):

        self.name = name
        self.path = Path
        self.path_data = path_data
        self.path_result = path_result

        self.YYYY_index = dic["YYYY_index"]
        self.MM_index = dic["MM_index"]
        self.DD_index = dic["DD_index"]
        self.hh_index = dic["hh_index"]
        self.mm_index = dic["mm_index"]
        self.ss_index = dic["ss_index"]
        self.JDs_index = dic["JDs_index"]
        self.yy_index = dic["yy_index"]
        self.GpsF_index = dic["GpsF_index"]


        self.data_process()

    def data_process(self):

        L = self.name

        l = L.split('_')
        l1 = l[0].split('-')
        for val in l[1:]:
            l1.extend(val.split('-'))
        l2 = l1[0].split('-')
        for val in l1[1:]:
            l2.extend(val.split('.'))

        Year, Months, Days, Minutes, Hours, Seconds = 0, 0, 0, 0, 0, 0


        if self.JDs_index:
            yy = "00"
            JDs = str(l2[self.JDs_index[0]][self.JDs_index[1]:self.JDs_index[1] + 3])

            if self.yy_index:
                yy = str(l2[self.yy_index[0]][self.yy_index[1]:self.yy_index[1] + 2])

            t = yy + JDs

            D = datetime.strptime(t, '%y%j').date()

            Days = int(D.strftime("%d"))
            Months = int(D.strftime("%m"))
            Year = int(D.strftime("%Y"))


        if self.GpsF_index:

            GpsF = str(l2[self.GpsF_index[0]][self.GpsF_index[1]:self.GpsF_index[1] + 4])
            JDs = GpsF[0:-2]
            

            l = {'0' : 0,'a': 0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14, 'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23}

            Hours = l[str(GpsF[-1])]

            if GpsF[-1] != '0':
                Minutes = 30

            if self.yy_index:
                yy = str(l2[self.yy_index[0]][self.yy_index[1]:self.yy_index[1] + 2])
                d = yy + '/' + JDs
                D = datetime.strptime(d, '%y/%j').date()

            else:
                D = datetime.strptime(JDs, '%j').date()

            Days = int(D.strftime("%d"))
            Months = int(D.strftime("%m"))
            Year = int(D.strftime("%Y"))

      
        if self.YYYY_index:
            Year = int(l2[self.YYYY_index[0]][self.YYYY_index[1]:self.YYYY_index[1] + 4])

        if self.MM_index:
            Months = int(l2[self.MM_index[0]][self.MM_index[1]:self.MM_index[1] + 2])

        if self.DD_index:
            Days = int(l2[self.DD_index[0]][self.DD_index[1]:self.DD_index[1] + 2])

        if self.hh_index:
            Hours = int(l2[self.hh_index[0]][self.hh_index[1]:self.hh_index[1] + 2])

        if self.mm_index:
            Minutes = int(l2[self.mm_index[0]][self.mm_index[1]:self.mm_index[1] + 2])

        if self.ss_index:
            Seconds = int(l2[self.ss_index[0]][self.ss_index[1]:self.ss_index[1] + 2])

        date = datetime(Year, Months, Days, Hours, Minutes, Seconds)

        self.date = date

    def display(self):

        print("File : ", self.name)
        print(self.date)
        print('-----------------')


def decode_filename(mode, L, path_data, path_result, path3):

    YYYY_index, MM_index, DD_index, hh_index, mm_index, ss_index, JDs_index, yy_index, GpsF_index = [], [], [], [], [], [], [], [], []
    dic_mode = {'YYYY': "%Y", 'MM': "%m", 'DD': "%d", 'hh': "%H", 'mm': "%M", "ss": "%S"}
    l_mode = list(dic_mode.keys())

    # - - - - Predefined arguments - - - - -

    # L = "YYYY-MM-DD_blabla_hhmmss.bag"
    # path_data = "/home/julienpir/Desktop/Benoit/data"
    # path_result = "output"
    # path3 = "File"

    # - - - - - - - -

    if not path3:
        path3 = "File"

    original = path_data
    target = "backup"

    shutil.copytree(original, target, dirs_exist_ok=True)  # in order to protect the initial data, we work on copy data
    path_data = target

    # - - - - - File format extraction - - - - -

    l = L.split('_')

    l1 = l[0].split('-')
    for val in l[1:]:
        l1.extend(val.split('-'))

    l2 = l1[0].split('-')
    for val in l1[1:]:
        l2.extend(val.split('.'))

    for k in range(len(l2)):
        if l2[k].find('YYYY') != -1:
            YYYY_index = [k, l2[k].find('YYYY')]

        if l2[k].find('MM') != -1:
            MM_index = [k, l2[k].find('MM')]

        if l2[k].find('DD') != -1:
            DD_index = [k, l2[k].find('DD')]

        if l2[k].find('hh') != -1:
            hh_index = [k, l2[k].find('hh')]

        if l2[k].find('mm') != -1:
            mm_index = [k, l2[k].find('mm')]

        if l2[k].find('ss') != -1:
            ss_index = [k, l2[k].find('ss')]

        if l2[k].find('JDs') != -1:
            JDs_index = [k, l2[k].find('JDs')]

        if l2[k].find('yy') != -1:
            yy_index = [k, l2[k].find('yy')]

        if l2[k].find('GpsF') != -1:
            GpsF_index = [k, l2[k].find('GpsF')]

    dic = {"YYYY_index": YYYY_index, "MM_index": MM_index, "DD_index": DD_index, "hh_index": hh_index,"mm_index": mm_index, "ss_index": ss_index, "JDs_index" : JDs_index, "yy_index" : yy_index, "GpsF_index" : GpsF_index}
    
    # - - - - - Directory recovery - - - -

    files = os.listdir(path_data)  # list of the files contained in the source path
    L = []

    for name in files:
        Path = path_data + "/" + name

        f = file(name, Path, path_data, path_result, dic)

        try:
            f = file(name, Path, path_data, path_result, dic)
            L.append(f)
        except:  # if the file is not in the good format, we don't deal with it
            pass

    # - - - - - Sorting the files - - - - - -

    L.sort(key=operator.attrgetter('date'))

    # - - - - - Checking of the folder format - - - - - -

    ajout = []

    for k in range(0, l_mode.index(mode) + 1):

        if l_mode[k] not in path3:
            ajout.append(l_mode[k])

    if ajout:
        path3 = ":".join(ajout) + '_' + path3


    if not path_result:
        path_result = 'output'

    # - - - - - Moving of the data - - - - - -

    if len(L) < 1:
        print("Error no data found")

    date = L[0].date
    path_3 = filter_title(path3, date)
    path_folder = path_result + '/' + path_3

    try:
        os.makedirs(path_folder)  # if the output directory is not already created

    except:
        pass

    original = L[0].path
    target = path_folder
    shutil.move(original, target)

    past_date = date.strftime(dic_mode[mode])
    D_past = date

    for k in range(1, len(L)):
        date = L[k].date

        if date_lim_cond(date,D_past, mode):

            D_past = date

            path_3 = filter_title(path3, date)
            path_folder = path_result + '/' + path_3

            try:
                os.makedirs(path_folder)

            except:
                pass

        target = path_folder
        original = L[k].path
        shutil.move(original, target)

    # - - - - - History saving - - - - - -

    d1 = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    f = open("log.txt", "a")
    f.write("\n" + d1 + " : " + str(len(L)) + " files sorted")
    f.close()

    print("Done")


# - - - - - - - - - - - - - - - - - - - - - - -

def filter_title(path3, date):
    path3 = path3.replace('YYYY', date.strftime('%Y'))
    path3 = path3.replace('MM', date.strftime('%m'))
    path3 = path3.replace('DD', date.strftime('%d'))
    path3 = path3.replace('hh', date.strftime('%H'))
    path3 = path3.replace('mm', date.strftime('%M'))
    path3 = path3.replace('ss', date.strftime('%S'))

    return (path3)

# - - - - - - - 

def date_lim_cond(D,D_past, mode):

    dic_mode2 = {'YYYY': 1, 'MM': 2, 'DD': 3, 'hh':4, 'mm': 5, "ss": 6}
    L_mode =  ["%Y", "%m", "%d",  "%H", "%M", "%S"]

    for k in range(1,dic_mode2[mode]):
        truc = L_mode[k-1]

        if D.strftime(truc) != D_past.strftime(truc):
            return(True)

    return(False)




# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# - - - - - - - - - - - - Tkinter IHM Part - - - - - - - - - - - - -
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =


def show_entry_fields():
    decode_filename(varGr.get(), path0.get(), path1.get(), path2.get(), path3.get())


# = = = =


def createNewWindow():
    newWindow = Toplevel(Frame01_l)
    newWindow.title('Help Window')

    label = Label(newWindow, text="Nomenclature : ", width=80, height=1)
    label.config(font=("Courier", 20))
    label.pack()

    label = Label(newWindow, text="YYYY corresponds to the year", width=80)
    label.pack()
    label = Label(newWindow, text="MM corresponds to the month", width=80)
    label.pack()
    label = Label(newWindow, text="DD corresponds to the day", width=80)
    label.pack()
    label = Label(newWindow, text="hh corresponds to the hour", width=80)
    label.pack()
    label = Label(newWindow, text="mm corresponds to the minute", width=80)
    label.pack()
    label = Label(newWindow, text="ss corresponds to the seconde", width=80)
    label.pack()

    label = Label(newWindow, text="JDs corresponds to the Julian Days", width=80)
    label.pack()
    label = Label(newWindow, text="yy corresponds to the Julian Year", width=80)
    label.pack()
    label = Label(newWindow, text="GpsF corresponds to the GNSS encoder", width=80)
    label.pack()

    label = Label(newWindow, text="", width=80)
    label.pack()

    label = Label(newWindow, text="Examples : ", width=80, height=1)
    label.config(font=("Courier", 20))
    label.pack()

    label = Label(newWindow,
                  text="Drix6_INS_Postprocessing_2021-01-20_083506_part1.log -> Drix6_INS_Postprocessing_YYYY-MM-DD_hhmmss_part1.log ",
                  width=100)
    label.pack()

    label = Label(newWindow, text="VL_67816_210120140628.asvp -> VL_67816_DDMMYYYYhhmm.asvp ", width=100)
    label.pack()


def createNewWindow1():
    newWindow = Toplevel(Frame01_l)
    newWindow.title('Help Window')

    label = Label(newWindow, text="It's the name format of the folders where the data will be sorted", width=100,
                  height=2)
    label.pack()

    label = Label(newWindow, text="Examples : ", width=40, height=1)
    label.config(font=("Courier", 20))
    label.pack()

    label = Label(newWindow, text="YYYY-drix_data", width=40)
    label.pack()

    label = Label(newWindow, text="MM_hh-data", width=40)
    label.pack()

    label = Label(newWindow, text="MM_YYYY_phins_DD:hh", width=40)
    label.pack()


def createNewWindow3():
    newWindow = Toplevel(Frame01_l)
    newWindow.title('Help Window')

    label = Label(newWindow, text="Examples : ", width=80, height=1)
    label.config(font=("Courier", 20))
    label.pack()

    label = Label(newWindow, text="If you want to sort all the folder/file in the folder mission_logs", width=100)
    label.pack()

    label = Label(newWindow, text="Enter : /home/julienpir/Documents/iXblue/20210120 DriX6 Survey OTH/mission_logs",
                  width=100)
    label.pack()


def createNewWindow4():
    newWindow = Toplevel(Frame01_l)
    newWindow.title('Help Window')

    label = Label(newWindow, text="Enter the directory where the data will be sorted ", width=80, height=1)
    label.pack()

    label = Label(newWindow, text="By default it will store in the directory output next to the source code", width=100,
                  height=1)
    label.pack()


# - - - - - - - - - Window Creation - - - - - - - - -


fenetre = Tk()
fenetre.title('File sorter')

# frame 01
Frame01 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame01.pack(side=TOP, padx=20, pady=20)

Frame01_l = Frame(Frame01, borderwidth=2, relief=GROOVE)
Frame01_l.pack(side=LEFT, padx=20, pady=30)

Frame01_l3 = Frame(Frame01_l, borderwidth=2, relief=GROOVE)
Frame01_l3.pack(side=BOTTOM, padx=20, pady=30)

Frame01_l2 = Frame(Frame01_l, borderwidth=2, relief=GROOVE)
Frame01_l2.pack(side=BOTTOM, padx=20, pady=30)

Frame01_l1 = Frame(Frame01_l, borderwidth=2, relief=GROOVE)
Frame01_l1.pack(side=BOTTOM, padx=20, pady=30)

Frame01_r = Frame(Frame01, borderwidth=2, relief=GROOVE)
Frame01_r.pack(side=RIGHT, padx=20, pady=30)

Frame01_r2 = Frame(Frame01_r, borderwidth=2, relief=GROOVE)
Frame01_r2.pack(side=BOTTOM, padx=20, pady=30)

Frame01_r1 = Frame(Frame01_r, borderwidth=2, relief=GROOVE)
Frame01_r1.pack(side=BOTTOM, padx=20, pady=30)

# frame 02
Frame02 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame02.pack(side=TOP, padx=20, pady=30)

# frame 03
Frame03 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame03.pack(side=TOP, padx=20, pady=30)

Frame03_1 = Frame(Frame03, borderwidth=2, relief=GROOVE)
Frame03_1.pack(side=BOTTOM, padx=20, pady=30)

# frame 04
Frame04 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame04.pack(side=TOP, padx=20, pady=30)

# = = = = = = =


label = Label(Frame01_l, text="Set Up", bg="green", width=50, height=2)
label.config(font=("Courier", 20))
label.pack()

label = Label(Frame01_l1, text="Enter the file/folder type", width=100)
label.pack()

path0 = Entry(Frame01_l1, width=80)
path0.pack(side=LEFT)

B3 = Button(Frame01_l1, text="Help", command=createNewWindow)
B3.pack(side=LEFT, padx=20)

label = Label(Frame01_l2, text="Enter Source path", width=100)
label.pack()

path1 = Entry(Frame01_l2, width=80)
path1.pack(side=LEFT)

B3 = Button(Frame01_l2, text="Help", command=createNewWindow3)
B3.pack(side=LEFT, padx=20)

label = Label(Frame01_l3, text="Enter Result path", width=100)
label.pack()

path2 = Entry(Frame01_l3, width=80)
path2.pack(side=LEFT)

B3 = Button(Frame01_l3, text="Help", command=createNewWindow4)
B3.pack(side=LEFT, padx=20)

# = = = = = = = = = =


label = Label(Frame01_r, text="Optional", width=40, height=2, bg='grey')
label.config(font=("Courier", 20))
label.pack()

label = Label(Frame01_r, text="The data file will be stored in seperate folders by : ", width=100)
label.pack()

vals = ['YYYY', 'MM', 'DD', 'hh', 'mm']
etiqs = ['years', 'months', 'days', 'hours', 'minutes']
varGr = StringVar()
varGr.set(vals[0])
for i in range(5):
    b = Radiobutton(Frame01_r, variable=varGr, text=etiqs[i], value=vals[i])
    b.pack()

label = Label(Frame01_r1, text="The different folders will be named : ", width=100)
label.pack()

path3 = Entry(Frame01_r1, width=80)
path3.pack(side=LEFT, padx=20)

B4 = Button(Frame01_r1, text="Help", command=createNewWindow1)
B4.pack(side=LEFT, padx=20)

B2 = Button(Frame03_1, text='Run program', command=show_entry_fields, bg='green')
B2.config(height=2, width=40)
B2.pack(side=LEFT, padx=20)

B1 = Button(Frame03_1, text="Quit", command=Frame01.quit, bg='red')
B1.config(height=2, width=40)
B1.pack(side=LEFT, padx=20)

fenetre.mainloop()




