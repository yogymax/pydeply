

'''

set --
    duplicates not allowed
    seq not maintained
    single nonetype is allowed
    mutable
    DS -- Hashtable


use case --

weekdays = ("mon","tues")

## can we increase the leng
        values1 -- no
        values2 -- yes

    can we remove index 4
        v1 -- no
        v2 -- yes

    can we add the elements inside index 4
        v1 -- yes -- actual inside list
        v2  -- no -



'''
values[0]='AAA' #Not allowed-- change tuple [0] -- ref
values[4]='XXXX' #  not allowed
values[4][0]=1000  #
values[4].append(1000)
values[4].clear()
