def virus_test(sample,composition):
    a = len(sample)
    b = len(composition)
    i=j=0
    while i<a and j<b:
        if sample[i] == composition[j]:
            i+=1
        j+=1
    return i==a

def input_data():
    V = input()
    N = int(input())
    x = []
    for i in range(N):
        x.append(input())
    for i in x:
        if virus_test(i,V) == True:
            print('POSITIVE')
        else:
            print('NEGATIVE')

input_data()
