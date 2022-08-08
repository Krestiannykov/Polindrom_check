
def polindrom_check(c1,c2):
    ## Python 3.9.13
    ## Checking strings for compliance with the polydrome principle
    ## Check length of string
    if len(c1)!=len(c2):
        return 'Polyndrom is not detected'
    ## Convertion to list
    a1=list(c1)
    a2=list(c2)
    ## Check parameter_1 symbols
    for i in a1:
        ## Check parameter_2 symbols
        for j in a2:
            ## Check matches
            if i==j:
                ## Del matches
                a2.remove(j)
                break
    ## Check remainders
    if len(a2)==0:
        return 'Polyndrom detected'
    else:
        return 'Polyndrom is not detected'
