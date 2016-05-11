
def qsort(tab,start,end):
    if end > start:
        #print 'before: ',tab
        lmost = start
        rmost = end
        pivot = tab[end]
        done = False
        while not done:
            while lmost < end and pivot > tab[lmost]:
                lmost += 1
            while rmost > start and pivot < tab[rmost]:
                rmost -= 1
            if lmost <= rmost:
                tab[lmost],tab[rmost] = tab[rmost],tab[lmost]
                lmost += 1
                rmost -= 1
            else:
                done = True
        #print 'after:  ',tab
        qsort(tab,start,rmost)
        qsort(tab,lmost,end)

if __name__ == '__main__':
    l = [5,3,1,2,6,2]
    print l
    qsort(l,0,len(l)-1)
    print l

