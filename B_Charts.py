# -*- coding: utf-8 -*-
"""B_CHARTS.py"""


def main():
    
    """Returns List Containing Tuple Pairings of SQL Querys and Titles for B-Graphs"""
    
    Charts = []               
    '''B1'''
    Query = """select 
        Language,
        sum(case when Network = 'ATTT'  then 1 else 0 end) ATTT,
        sum(case when Network = 'CAC'  then 1 else 0 end) CAC,
        sum(case when Network = 'xls' then 1 else 0 end) XLS
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        group by Language
        order by count(*) desc;"""# % (i)
    
    Title ='B1 - All Calls by Language, Handled by Interpreting Networks'
    Charts += [(Query, Title)]
    '''B2'''
    
    Query = """select 
        Language,
        
        sum(case when Network = 'ATTT'  then 1 else 0 end) ATTT,
        sum(case when Network = 'CAC'  then 1 else 0 end) CAC,
        sum(case when Network = 'xls' then 1 else 0 end) XLS
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        Where Language <> 'Spanish'
        group by Language
        order by count(*) desc;"""# % (i)
  
    Title ='B2 - All Calls by Language, Handled by Interpreting Networks X Spanish'
    Charts += [(Query, Title)]
    
    
    '''B3'''
    
    Query = """select 
        Language,
        sum(case when Network = 'ATTT'  then 1 else 0 end) ATTT,
        sum(case when Network = 'CAC'  then 1 else 0 end) CAC,
        sum(case when Network = 'xls' then 1 else 0 end) XLS
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        Where Language <> 'Spanish'
        group by Language
        order by count(*) desc
        limit 25;"""# % (i)
    
    Title ='B3 - All Calls by Top 25 Languages X Spanish\n Handled by Interpreting Networks '
    Charts += [(Query, Title)]
    
    '''B4'''
    
    Query = """select 
        Language,
        sum(case when Network = 'ATTT'  then 1 else 0 end) ATTT,
        sum(case when Network = 'CAC'  then 1 else 0 end) CAC,
        sum(case when Network = 'xls' then 1 else 0 end) XLS
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        Where Language <> 'Spanish'
        group by Language
        order by count(*) desc
        limit 10;"""# % (i)
    
    Title ='B4 - All Calls by Top 10 Languages X Spanish\n Handled by Interpreting Networks '
    Charts += [(Query, Title)]
    
    '''B5'''
    
    Query = """select 
        Language,
        sum(case when Network = 'ATTT'  then 1 else 0 end) ATTT,
        sum(case when Network = 'CAC'  then 1 else 0 end) CAC,
        sum(case when Network = 'xls' then 1 else 0 end) XLS
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        Where Language <> 'Spanish'
        and hour(pst_datetime) >= 8
        and hour(pst_datetime) < 16
        and dayofweek(pst_datetime) <> 7
        and dayofweek(pst_datetime) <> 1 
        group by Language
        order by count(*) desc
        limit 10;"""# % (i)
    
    Title ='B5 - All Calls by Top 10 Languages X Spanish, Handled by Interpreting Networks\nM-F Day Shift PST '
    Charts += [(Query, Title)]
    
    '''B6'''
    
    Query = """select 
        Language,
        sum(case when Network = 'ATTT'  then 1 else 0 end) ATTT,
        sum(case when Network = 'CAC'  then 1 else 0 end) CAC,
        sum(case when Network = 'xls' then 1 else 0 end) XLS
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        Where Language <> 'Spanish'
        and hour(pst_datetime) >= 10
        and hour(pst_datetime) < 18
        and dayofweek(pst_datetime) <> 7
        and dayofweek(pst_datetime) <> 1 
        group by Language
        order by count(*) desc
        limit 10;"""# % (i)
    
    Title ='B6 - All Calls by Top 10 Languages X Spanish\nHandled by Interpreting Networks, M-F Day Shift CST '
    Charts += [(Query, Title)]
    
    '''B7'''
    
    Query = """select 
        Language,
        sum(case when Network = 'ATTT'  then 1 else 0 end) ATTT,
        sum(case when Network = 'CAC'  then 1 else 0 end) CAC,
        sum(case when Network = 'xls' then 1 else 0 end) XLS
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        Where Language = 'Spanish'
        group by Language
        order by count(*) desc
        ;"""# % (i)
    
    Title ='B7 - All Spanish Calls by Interpretation Network '
    Charts += [(Query, Title)]
    
    '''B8'''
    
    Query = """select 
        Language,
        sum(case when Network = 'ATTT'  then 1 else 0 end) ATTT,
        sum(case when Network = 'CAC'  then 1 else 0 end) CAC,
        sum(case when Network = 'xls' then 1 else 0 end) XLS
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        Where Language = 'Spanish'
        and hour(pst_datetime) >= 8
        and hour(pst_datetime) < 16
        and dayofweek(pst_datetime) <> 7
        and dayofweek(pst_datetime) <> 1 
        group by Language
        order by count(*) desc
        ;"""# % (i)
    
    Title ='B8 - All Spanish Calls by Interpretation Network - M-F Day Shift '
    Charts += [(Query, Title)]
    
    '''B9'''
    
    Query = """select 
        Language,
        sum(case when Network = 'ATTT'  then 1 else 0 end) ATTT,
        sum(case when Network = 'CAC'  then 1 else 0 end) CAC,
        sum(case when Network = 'xls' then 1 else 0 end) XLS
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        Where Language = 'Spanish'
        and hour(pst_datetime) >= 8
        and hour(pst_datetime) < 16
        and dayofweek(pst_datetime) <> 7
        and dayofweek(pst_datetime) <> 1 
        and ORG_CAC in (
        select distinct(ORG_CAC) from calllogs where Resource_Group like 'XLS')
        and ORG_CAC <> 'BTTB'
        group by Language
        order by count(*) desc
        ;"""# % (i)
    
    Title ='B9 - Spanish Calls by Interpretation Network\n Only XLS Data Provider Hospitals X BTTB \nM-F Day Shift '
   
        
    Charts += [(Query, Title)]
    return Charts
    
    
