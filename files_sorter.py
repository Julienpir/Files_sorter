import os
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
# - - - - - - - - - - -  Predefined arguments - - - - - - - - - - - -
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# Reminder : 

# "YYYY corresponds to the year"
# "MM   corresponds to the month"
# "DD   corresponds to the day"
# "hh   corresponds to the hour"
# "mm   corresponds to the minute"
# "ss   corresponds to the seconde"
# "JDs  corresponds to the Julian Days"
# "yy   corresponds to the Julian Year"
# "GpsF corresponds to the GNSS encoder"

# "ypor189s.20n.Z" 


# mode          ->      (The data will be stored in seperate folders by), possible values : ['YYYY', 'MM', 'DD', 'hh', 'mm'] 
# form          ->      file/folder format
# path_data     ->      source path
# path_result   ->      result path
# path3         ->      folders name


# mode = 'MM'                   
# form = "0062_YYYYMMDD_hhmm_Demo_Line00 - 0001.db"               
# path_data = "/home/julienpir/Desktop/Benoit/DB"       
# path_result = "output"              
# path3 = "File"       


mode = 'mm'                   
form = "yporGpsF.yyn.Z"               
path_data = "/home/julienpir/Desktop/Benoit/GNSS DATA/20200707_YPORT/Compressed"       
path_result = "output2"              
path3 = "File"       



decode_filename(mode, form, path_data, path_result, path3)