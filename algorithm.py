def bubble_sort(seq,order=1):
    n = len(seq)
    while n>1:
        n=n-1
        if order==1:
            for i in range(n):
                if seq[i]>seq[i+1]:
                    seq[i],seq[i+1] = seq[i+1],seq[i]
        else:
            for i in range(n):
                if seq[i]<seq[i+1]:
                    seq[i],seq[i+1] = seq[i+1],seq[i]

    return seq

print(bubble_sort([5,4,3,2,6,1],0))