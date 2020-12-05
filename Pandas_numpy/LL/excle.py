import pandas as pd
import string
import os
import re
import sys
def csvtest(filename) :
    fileter = open('log.txt',"a+")
    text = 'check file :' + filename + '\n'
    print('check file :', filename)
    fileter.write(text)
    df1 = pd.read_csv(filename, usecols=["A_count", "T_count", "C_count", "G_count"],
                      encoding='unicode_escape')
    #print(type(df1))
    #print(int(df1['A_count'][2]), int(df1['T_count'][2]),int(df1['A_count'][2]) + int(df1['T_count'][2]))
    #print(len(df1))
#print(df1.cumsum)
#print(df1.index)
    df1list = df1.values.tolist()
    #print(df1list)
    del df1list[0]
    #print(df1list)
    #print(len(df1list))
    tmplist = list()
    for i in df1list :
        test = list(map(lambda x: int(x), i))
        tmplist.append(test)

    #print(tmplist)
    #print(len(tmplist))
    count1 = 0
    for i in range(len(tmplist)) :
        if tmplist[i][0] < 100 :
            count1 += 1
        if tmplist[i][1] < 100 :
            count1 += 1
        if tmplist[i][2] < 100 :
            count1 += 1
        if tmplist[i][3] < 100 :
            count1 += 1

        if count1 == 4 :
            #print(i+3 , ":", df1list[i])
            txt = str(i+3) +":" + str(df1list[i][0]) + ' ' + str(df1list[i][1]) + ' ' + str(df1list[i][2]) + ' ' +str(df1list[i][3]) + '\n'
            fileter.writelines(txt)
        count1 = 0

def check_file(file_path) :
    os.chdir(file_path)
    #print(os.path.abspath(os.curdir))
    all_file = os.listdir()
    files = []
    for f in all_file:
        if os.path.isdir(f) :
            files.extend(check_file(file_path+'\\'+f))
            os.chdir(file_path)
        else:
            files.append(file_path + '\\' + f)
    os.chdir(file_path)
    return files

def re_matchfile(filelist) :
    tmpfilelist = []
    for i in range(len(filelist)) :
        if re.search(r'\.csv',filelist[i]) :
            tmpfilelist.append(filelist[i])
    return tmpfilelist


if __name__ == '__main__' :
    #test()
    arg1 = sys.argv[1]
    filename = check_file(arg1)
    #print(filename)
    filelist_new = re_matchfile(filename)
    #print(filelist_new)
    for i in range(len(filelist_new)) :
        csvtest(filelist_new[i])





