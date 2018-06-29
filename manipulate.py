#! /usr/bin/python3
#This is a program to search through a file tree and copy or delete files with a certain file extension to a directory
#This will also allow the same thing to be done with command line argument in MB
####### !!!!!!!!!I want to try flags so the syn will be program.py -dc -R DIR <DIR> [arg]
#I think the flags may be causing an issue because I am dumb, so I am giving up on them.
#I will try flags in a later program
import os, sys, shutil, re

def main():
        checker()
#First going to start a checker for syntax, and send err/help, then return var to select method
def checker():
        recurs = False
        dirArg = 2
        destArg = 3
        ArgArg = 4
        if sys.argv[2].lower() == 'recursive':
                recurs = True
                dirArg += 1
                destArg += 1
                ArgArg += 1
        target = sys.argv[dirArg]
        if os.path.isdir(sys.argv[dirArg]) == False:
            if os.path.isdir(os.path.join(os.getcwd(),sys.argv[dirArg])):
                target = os.getcwd()+'/'+sys.argv[dirArg]
            else:
                errMsg(3)

        if len(sys.argv) < 4 or len(sys.argv) > 7:
            errMsg(0)
            sys.exit(0)
            
        elif sys.argv[1] == 'copy':
            print('Copy Selected')
            if os.path.isdir(sys.argv[destArg]):
                os.mkdir(sys.argv[destArg]);
            if ArgArg >= len(sys.argv):
                errMsg(1)
            else:
                cpSel(recurs,target, sys.argv[destArg], sys.argv[ArgArg], ArgArg+1)
             
            print('no')
        elif sys.argv[1] == 'delete':
            print('Delete Selected')
            if destArg >= len(sys.argv) + 1:
                errMsg(2)
            delSel(recurs, target, sys.argv[ArgArg - 1], ArgArg)
        elif sys.argv[1] == 'help':
            helper()
        else:
            errMsg(0)

#Error Msg. Should offer specific help def errMsg(x):
def errMsg(x):
    if x == 0:
        print('Poor Syntax: Argument number is incorrect See Help\n\n' + ('*'*50) + '\n\n')
    elif x ==1:
        print('Not Enough Arguments. To copy files in a directory, you must include the relevant flag, the target directory, the destination directory, the type (\'size\' or \'ext\'), and the argument\n\n')
    elif x ==2:
        print('Not Enough Arguments. To delete files, you must include the relevant flag, the target directory, the type of file (\'size\' or \'ext\'), and the argument\n\n')
    elif x == 3:
        print('Target Directory Does not exist!\n\n')
    elif x == 4:
        print('Invalid file selector: Valid types are \'all\', \'size\', or \'ext\'\n\n')
    helper()
    sys.exit(0)

#Help Function
def helper():
    print('The format should be \'program.py (delete|copy) [recursive] targetDIRECTORY <destinationDIRECTORY> type arg\n\n\tdelete\t-specifies files to be deleted\n\tcopy\t-specifies files will be copied\n\thelp\t-displays this help screen\n\trecursive\t-optional -directory will be walked recursively\n\ttargetDIRECTORY\tis the affected directory\n\tdestinationDIRECTORY\tis only used with -c. Files will be copied here\n\ttype use size,ext to filter files by size or extension\n\targ\t-if size is specified, use number in MB (no Suffix), if extension is specified, supply extention (e.g. .pdf)')


def listFiles(rec,direct,cp=False):
    lst = []
    if rec == True:
        for path,subdir,filenames in os.walk(direct):
            for files in filenames:
                if cp == False:
                    fullfile = (path+'/'+files)
                lst.append(fullfile)

    else:
        for filenames in os.listdir(direct):
            lst.append(direct+'/'+filenames)
    print(lst)
    for i in lst:
        if os.path.isdir(i):
            lst.remove(i)
    return lst
    
#Method for copying
def cpSel(rec, direct, destin, argum, argarg):
    fileList = listFiles(rec, direct)
    nameList = listFiles(rec, direct, True)
    destin = pathChecker(destin)
    
    if argum.lower() == 'all':
        for i in fileList:
            finale += destin+i
            shutil.copy(i,finale)
    elif argum.lower() == 'ext':
        for i in fileList:
            if i.endswith(sys.argv[argarg]):

                finale += destin+i
                shutil.copy(i,finale)
    elif argum.lower() == 'size':
        for i in fileList:
            finale = destin+i
            shutil.copy(i,finale)
    else:
        errMsg(4)

    print('slectrt wrkng')

#Method for deleting
def delSel(rec, direct, argum, argarg):
    fileList = listFiles(rec, direct)
    chopBlock = []
    direct = pathChecker(direct)
    if argum.lower() == 'all':
       for i in fileList:
           print(i)
    elif argum.lower() == 'size':
        for i in fileList:
            if os.getsize(i) >= sys.argv[ArgArg-1]:
                print(i)
                chopBlock = chopBlock.append(i)
    elif argum.lower() == 'ext':

        for i in fileList:
            if i.endswith(sys.arg[var]):
                print(i)
                chopBlock += chopBlock.append(i)
    else:
        errMsg(4)
    print("\nThese files will be deleted... Is this okay (y/n)?\n>>",end="")

    confirm = input()
    if confirm.lower() == 'y':
        for i in chopBlock:
            os.unlink(i)
    else:
        print('*********************\nDELETION ABORTED\n\n\n')
    
#Ensure paths all have / at the end
def pathChecker(path):
    if path.endswith('/') == False:
        path += '/'
        return path
    
    #Pluggable method for searching 

#
main()
