
"""A_CHARTS.py"""

def main():
    
    """Returns List Containing Tuple Pairings of SQL Querys and Titles for A-Graphs"""
    Charts = []
    '''A1 '''
    Query = """select 
        sum(case when ORG_CAC = Resource_Group then 1 else 0 end) Internal,
        sum(case when Network = 'ATTT' and Resource_Group <> ORG_CAC then 1 else 0 end) ATTT,
        sum(case when Network = 'CAC' and Resource_Group <> ORG_CAC then 1 else 0 end) CAC,
        sum(case when Network = 'xls' then 1 else 0 end) XLS
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity;"""# % (i)
    
    Title ='A1 - Number of Calls by Type of Interpreting Network'
    Charts += [(Query, Title)]
    
    '''A2  '''
    
    Query = """select 
        sum(case when Network = 'ATTT' then 1 else 0 end) ATTT,
        sum(case when Network = 'CAC' then 1 else 0 end) CAC,
        sum(case when Network = 'XLS' then 1 else 0 end) XLS
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        """# % (i)
   
    Title ='A2 - Number of Calls by Network'
    Charts += [(Query, Title)]
    
    
    '''A2 X BTTB '''
    
    Query = """select 
        sum(case when Network = 'ATTT' then 1 else 0 end) ATTT,
        sum(case when Network = 'CAC' then 1 else 0 end) CAC,
        sum(case when Network = 'XLS' then 1 else 0 end) XLS
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        and ORG_CAC <> 'BTTB'"""# % (i)
    
    Title ='A2 - Number of Calls by Network, BTTB not Included'
    Charts += [(Query, Title)]
    
    '''A3 - Only XLS Providers X BTTB '''
    
    Query = """select 
        sum(case when Network = 'ATTT' then 1 else 0 end) ATTT,
        sum(case when Network = 'CAC' then 1 else 0 end) CAC,
        sum(case when Network = 'XLS' then 1 else 0 end) XLS
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
    
        WHERE ORG_CAC in (
        select distinct(ORG_CAC) from calllogs where Resource_Group like 'XLS')
        and ORG_CAC <> 'BTTB'"""# % (i)
    
    Title ='A3 - Number of Calls by Network\n Only XLS Data Provider Hospitals X BTTB'
    Charts += [(Query, Title)]
    return Charts

