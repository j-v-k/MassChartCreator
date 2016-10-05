# -*- coding: utf-8 -*-
"""ChartPullClass.py"""


import MySQLdb
import pandas
import matplotlib.pyplot as plt
class PullClass:
    """Creates Each type of Chart"""
    
    def __init__(self, Query, Title, savePath, view):
        self.Query = Query.replace("calllogs", view)
        self.Title = Title
        self.savePath = savePath
        self.view= view
    
    @staticmethod
    def execute(ax, plt, Query, Title, savePath):
        """Portion of chart execution which is the same with every chart type"""
        
        '''Adjusts the bottom margin to make room for the axis-label'''
        plt.subplots_adjust(bottom=0.15)
        ax.set_ylabel('Number of Calls')
        ax.set_title(Title,  y=1.04)
        plt.tight_layout()
        '''save to folder'''
        saveTitle = Title.replace(" - ", "_").replace(" ", "_").replace("-","").replace(",","").replace("\n","").rstrip('_')
        plt.savefig(savePath + saveTitle, dpi=250)            
    
    "A/B Charts"
    def abChart(self):
        plt.ioff()

        plt.style.use('ggplot')
    
        db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                             user="root",         # your username
                             passwd="xxxx",  # your password
                             db="July2016")        # name of the data base
        """Reads the provide query with pandas"""
        df0 = pandas.read_sql(self.Query,db)
        pos = .5
        
        """Chceks whether query gives an 'internal' column, if it does, it is 'A1' """
        if 'internal' in self.Query.lower():
            ax =  df0[['Internal','ATTT', 'CAC','XLS']].plot(kind='bar', stacked=True,  position=pos, align='center')
        else:
            ax =  df0[['ATTT', 'CAC', 'XLS']].plot(kind='bar', stacked=True, position=pos, align='center')
        
        ax = plt.subplot(111)
        """A "B Chart if the query contains a language column, an A chart otherwise""" 
        if "language" in self.Query.lower():
            
            if len(df0.Language) > 25:
                """Makes font smaller if there are more then 25 languages"""
                ax.set_xticklabels(df0.Language, fontsize = 5)
                ax.set_xticklabels(df0.Language)
            else:
                ax.set_xticklabels(df0.Language)
        else:
            ax.set_xticklabels([""])
        PullClass.execute(ax, plt, self.Query, self.Title, self.savePath)
        
    "C Charts"    
    def cChart(self):
        plt.ioff()

        plt.style.use('ggplot')
        
        db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                             user="root",         # your username
                             passwd="Boqw7778",  # your password
                             db="July2016")        # name of the data base
        
        """Reads the provide query with pandas"""                     
        df0 = pandas.read_sql(self.Query,db)
        
        pos = .5
        ax =  df0.plot(kind='bar',  position=pos)
        ax.legend_.remove()
        ax.set_xticklabels(df0.dayofweek)
        PullClass.execute(ax, plt, self.Query, self.Title, self.savePath)
    
    "D Charts"    
    def dChart(self):
        plt.ioff()
        plt.style.use('ggplot')
        db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                             user="root",         # your username
                             passwd="Boqw7778",  # your password
                             db="July2016")        # name of the data base
                             
        """Reads the provide query with pandas"""
        df0 = pandas.read_sql(self.Query,db)
        print df0
        pos = .5
        ax =  df0[['Audio', 'Video']].plot(kind='bar', stacked=True,  position=pos, align='center')
        ax = plt.subplot(111)
        try:
            ax.set_xticklabels(df0.Org)
        except:
            ax.set_xticklabels(df0.ORG)
        PullClass.execute(ax, plt, self.Query, self.Title, self.savePath)
        
    