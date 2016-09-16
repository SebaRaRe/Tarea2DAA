
def minloc(A):
    f = len(A)
    fin = len(A)-1
    ini = 0
    mid = int((f/2))
    while 1:
        if A[mid] == A[fin] and A[mid] < A[mid-1]:
            return print ("la zona montanosa ubicada en la posicion %d podria contener agua"% mid)
        elif mid == fin:
            return
        if A[mid] == A[ini] and A[mid] < A[mid+1]:
            return print ("la zona montanosa ubicada en la posicion %d podria contener agua"% mid)
        elif mid == 0:
            return
        if A[mid] < A[mid-1] and A[mid] < A[mid+1]:
            return print ("la zona montanosa ubicada en la posicion %d podria contener agua"% mid)
        else:
            if A[mid-1] < A[mid] and A[mid] < A[mid+1]:
                ini = mid
                mid = int(((fin-mid)/2)+ini)
            if A[mid+1] > A[mid] and A[mid] > A[mid-1]:
                fin = mid
                mid = int(mid/2)
            fin = mid
            mid = int(mid/2)

    return 0
