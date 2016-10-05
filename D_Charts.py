# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 15:37:01 2016

@author: jvonkaenel
"""

def main():
    
    """Returns List Containing Tuple Pairing of SQL Querys and Titles for D-Graphs"""
    
    Charts = []
    
    "D1"
    Query = """select 
        Org,
        
        sum(case when AU_VD = 'AU'  then 1 else 0 end) Audio,
        sum(case when AU_VD = 'VD'  then 1 else 0 end) Video
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        group by Org
        order by count(*) desc;"""
    
    Title ='D1 - Number of Calls Video v Audio'
    Charts += [(Query, Title)]
    
    "D2"
    Query = """select 
        Org,
        
        sum(case when AU_VD = 'AU'  then 1 else 0 end) Audio,
        sum(case when AU_VD = 'VD'  then 1 else 0 end) Video
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        Where Org <> 'PHHS'
        group by Org
        order by count(*) desc;"""
    
    Title ='D2 - Number of Calls Video v Audio, Except PHHS'
    Charts += [(Query, Title)]
    
    return Charts