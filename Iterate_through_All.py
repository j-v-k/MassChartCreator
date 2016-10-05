
"""Iterate_Through_All.py"""

import A_Charts
import B_Charts
import C_Charts
import D_Charts
import ChartPullClass
import shutil
import os



def Destroy_Create_Folder(savePath):
    '''Destroy and create specified folder'''
    try:
        shutil.rmtree(savePath)
    except:
        pass
    os.mkdir(savePath) 



''''Add all Queries and Titles Together in a list'''
TotalList = []
AList= A_Charts.main()
BList= B_Charts.main()
CList = C_Charts.main()
DList = D_Charts.main()
TotalList = AList + BList + CList + DList

def chartBasedOnView(TotalList, savePath,view):
    '''Loops through the querylist and calls the charts'''
        
    for qTitle in TotalList:
        Query = qTitle[0]
        Title = qTitle[1]
        if "calllogs" not in view:
            Title = Title +" - No LA County XLS"
            
        
        TitleStart = Title[:2]
        
        if "A" in TitleStart or "B" in TitleStart:
            Instance = ChartPullClass.PullClass(Query, Title, savePath, view)
            Instance.abChart()
        elif "C" in TitleStart:
            Instance = ChartPullClass.PullClass(Query, Title, savePath, view)
            Instance.cChart()
        elif "D" in TitleStart:
            Instance = ChartPullClass.PullClass(Query, Title, savePath, view)
            Instance.dChart()
        else:
            print "Title Not Executed!!:"
            print Title
            return


'''Call the reports for two seperate views'''
        
view = 'calllogs'
savePath = "C:\\Users\\James\\Documents\\July 2016 DB\\Charts and Scripts\\Charts\\"
Destroy_Create_Folder(savePath)
chartBasedOnView(TotalList, savePath,view)


view = "nolacountyxls"
savePath = "C:\\Users\\James\\Documents\\July 2016 DB\\Charts and Scripts\\Charts_No_LA_County\\"
chartBasedOnView(TotalList, savePath,view)
    