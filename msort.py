def get_elems(tab, a, b):
    tmp = []
    i = a
    while i <= b:
        tmp.append(tab[i])
        i += 1
    return tmp

def merge(tab, start, end, half):
    t1 = get_elems(tab,start,half)
    t2 = get_elems(tab,half+1,end)
    i,j,k = 0,0,0
    while i < len(t1) and j < len(t2):
        if t1[i] < t2[j]:
            tab[start+k] = t1[i]
            i += 1
        else:
            tab[start+k] = t2[j]
            j += 1
        k += 1
    while i < len(t1):
        tab[start+k] = t1[i]
        i += 1
        k += 1
    while j < len(t2):
        tab[start+k] = t2[j]
        j += 1
        k += 1


def msort(tab, start, end):
    if start < end:
        middle = (end+start)/2
        msort(tab,start,middle)
        msort(tab,middle+1,end)
        merge(tab,start,end,middle)


if __name__ == '__main__':
    tab = [1,3,6,78,5,2,1,4,6,1,7,5,9,5,0]
    print 'before: ',tab
    msort(tab,0,len(tab)-1)
    print 'after: ',tab
