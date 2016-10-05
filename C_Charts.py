# -*- coding: utf-8 -*-
"""C_CHARTS.py"""



def main():
    
    """Returns List Containing Tuple Pairing of SQL Querys and Titles for C-Graphs"""
    Charts = [] 
    
    "C1"
    Query = """Select dayname(pst_datetime) as dayofweek,
        count(*)
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        Where language = 'Spanish'
        and hour(pst_datetime) >= 8
        and hour(pst_datetime) < 16
        and dayofweek(pst_datetime) <> 1
        and dayofweek(pst_datetime) <> 7
        and resource_group = 'XLS'
        group by day(pst_datetime)
        order by day(pst_datetime)
        ;"""

    Title ='C1 - All Spanish Calls M-F Day Shift PST'
    Charts += [(Query, Title)]
    
    "C1xP"
    Query = """Select dayname(pst_datetime) as dayofweek,
        count(*)
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        Where language = 'Spanish'
        and hour(pst_datetime) >= 8
        and hour(pst_datetime) < 16
        and dayofweek(pst_datetime) <> 1
        and dayofweek(pst_datetime) <> 7
        and ORG_CAC <> 'BTTB'
        and resource_group = 'XLS'
        group by day(pst_datetime)
        order by day(pst_datetime)
        ;"""
    
    Title ='C1 - All Spanish Calls M-F Day Shift PST X BTTB'

    Charts += [(Query, Title)]
    
    "C2"
    
    Query = """Select dayname(pst_datetime) as dayofweek,
        count(*)
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        Where language = 'Spanish'
        and hour(pst_datetime) >= 16
        and hour(pst_datetime) <= 23
        and dayofweek(pst_datetime) <> 1
        and dayofweek(pst_datetime) <> 7
        and resource_group = 'XLS'
        group by day(pst_datetime)
        order by day(pst_datetime)
        ;"""

    Title ='C2 - All Spanish Calls M-F Evening Shift PST'
    Charts += [(Query, Title)]
    
    "C2xBTTB"
    Query = """Select dayname(pst_datetime) as dayofweek,
        count(*)
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        Where language = 'Spanish'
        and hour(pst_datetime) >= 16
        and hour(pst_datetime) <= 23
        and dayofweek(pst_datetime) <> 1
        and dayofweek(pst_datetime) <> 7
        and resource_group = 'XLS'
        and ORG_CAC <> 'BTTB'
        group by day(pst_datetime)
        order by day(pst_datetime)
        ;"""

    Title ='C2 - All Spanish Calls M-F Evening Shift PST X BTTB'
    Charts += [(Query, Title)]
    
    "C3"
    
    Query = """Select dayname(pst_datetime) as dayofweek,
        count(*)
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        Where language = 'Spanish'
        and hour(pst_datetime) >= 0
        and hour(pst_datetime) < 8
        and dayofweek(pst_datetime) <> 1
        and dayofweek(pst_datetime) <> 7
        and resource_group = 'XLS'
        group by day(pst_datetime)
        order by day(pst_datetime)
        ;"""

    Title ='C3 - All Spanish Calls M-F Night Shift PST'
    Charts += [(Query, Title)]
    
    "C3xBTTB"
    Query = """Select dayname(pst_datetime) as dayofweek,
        count(*)
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        Where language = 'Spanish'
        and hour(pst_datetime) >= 0
        and hour(pst_datetime) < 8
        and dayofweek(pst_datetime) <> 1
        and dayofweek(pst_datetime) <> 7
        and resource_group = 'XLS'
        and ORG_CAC <> 'BTTB'
        group by day(pst_datetime)
        order by day(pst_datetime)
        ;"""

    Title ='C3 - All Spanish Calls M-F Night Shift PST X BTTB'
    Charts += [(Query, Title)]
    
    "C4"
    Query = """Select dayname(pst_datetime) as dayofweek,
        count(*)
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        Where language = 'Spanish'
        and hour(pst_datetime) >= 8
        and hour(pst_datetime) < 16
        and (dayofweek(pst_datetime) = 1
        or dayofweek(pst_datetime) = 7)
        and resource_group = 'XLS'
        group by day(pst_datetime)
        order by day(pst_datetime)
        ;"""

    Title ='C4 - All Spanish Calls S-S Day Shift PST'
    Charts += [(Query, Title)]
    
    "C4xP"
    Query = """Select dayname(pst_datetime) as dayofweek,
        count(*)
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        Where language = 'Spanish'
        and hour(pst_datetime) >= 8
        and hour(pst_datetime) < 16
        and (dayofweek(pst_datetime) = 1
        or dayofweek(pst_datetime) = 7)
        and ORG_CAC <> 'BTTB'
        and resource_group = 'XLS'
        group by day(pst_datetime)
        order by day(pst_datetime)
        ;"""
    
    Title ='C4 - All Spanish Calls S-S Day Shift PST X BTTB'

    Charts += [(Query, Title)]
    
    "C5"
    
    Query = """Select dayname(pst_datetime) as dayofweek,
        count(*)
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        Where language = 'Spanish'
        and hour(pst_datetime) >= 16
        and hour(pst_datetime) <= 23
        and (dayofweek(pst_datetime) = 1
        or dayofweek(pst_datetime) = 7)
        and resource_group = 'XLS'
        group by day(pst_datetime)
        order by day(pst_datetime)
        ;"""

    Title ='C5 - All Spanish Calls S-S Evening Shift PST'
    Charts += [(Query, Title)]
    
    "C5xBTTB"
    Query = """Select dayname(pst_datetime) as dayofweek,
        count(*)
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        Where language = 'Spanish'
        and hour(pst_datetime) >= 16
        and hour(pst_datetime) <= 23
        and (dayofweek(pst_datetime) = 1
        or dayofweek(pst_datetime) = 7)
        and resource_group = 'XLS'
        and ORG_CAC <> 'BTTB'
        group by day(pst_datetime)
        order by day(pst_datetime)
        ;"""

    Title ='C5 - All Spanish Calls S-S Evening Shift PST X BTTB'
    Charts += [(Query, Title)]
    
    "C6"
    
    Query = """Select dayname(pst_datetime) as dayofweek,
        count(*)
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        Where language = 'Spanish'
        and hour(pst_datetime) >= 0
        and hour(pst_datetime) < 8
        and (dayofweek(pst_datetime) = 1
        or dayofweek(pst_datetime) = 7)
        and resource_group = 'XLS'
        group by day(pst_datetime)
        order by day(pst_datetime)
        ;"""

    Title ='C6 - All Spanish Calls S-S Night Shift PST'
    Charts += [(Query, Title)]
    
    "C6xBTTB"
    Query = """Select dayname(pst_datetime) as dayofweek,
        count(*)
        from calllogs a
        join networkref b
        on a.Resource_Group = b. Entity
        Where language = 'Spanish'
        and hour(pst_datetime) >= 0
        and hour(pst_datetime) < 8
        and (dayofweek(pst_datetime) = 1
        or dayofweek(pst_datetime) = 7)
        and resource_group = 'XLS'
        and ORG_CAC <> 'BTTB'
        group by day(pst_datetime)
        order by day(pst_datetime)
        ;"""

    Title ='C6 - All Spanish Calls S-S Night Shift PST X BTTB'
    Charts += [(Query, Title)]

    return Charts
