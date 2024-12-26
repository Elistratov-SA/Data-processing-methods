from PyEMD import EMD

def EMDsmooth(t,y,nEMD,verbose=0):
    # t -- argument array (obligatory)
    # y -- values
    # nEMD -- modes number to filter (the higher, the smoother
    # verbose -- flag to print max modes number
    smooth=1*y
    if nEMD>0:
        IMF=EMD().emd(smooth,t)
        if nEMD>IMF.shape[0]:
            if verbose:print('IMF shape:',IMF.shape[0])
            nEMD=IMF.shape[0]
        for j in range(0,nEMD):
            smooth-=IMF[j]
    return smooth