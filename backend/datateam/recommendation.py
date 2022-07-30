def recommendation(viewlist):
    taglist = list()
    tmp1 = max(viewlist)    
    index1 = viewlist.index(tmp1)
    viewlist[index1] = -1
    tmp2 = max(viewlist)
    index2 = viewlist.index(tmp2)
    viewlist[index2] = -1
    tmp3 = max(viewlist)
    index3 = viewlist.index(tmp3)
    viewlist[index3] = -1
    if tmp1 != 0:
        taglist.append(index1)
    if tmp2 != 0:
        taglist.append(index2)
    if tmp3 != 0:
        taglist.append(index3)    
    return taglist