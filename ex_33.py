n1 = int(input("Insert a number: "))
n2 = int(input("Insert a number: "))
n3 = int(input("Insert a number: "))
#if n1 > n2 and n1 > n3:
#    print("The bigger is {}".format(n1))
#elif n2 > n1 and n2 > n3:
#    print("The bigger one is {}".format(n2))
#else:
#    n3 > n1 and n3 > n2
#    print("The bigger one is {}".format(n3))
#
#if n1 < n2 and n1 < n3:
#    print("The smaller is {}".format(n1))
#elif n2 < n1 and n2 < n3:
#    print("The smaller one is {}".format(n2))
#else:
#    n3 < n1 and n3 < n2
#    print("The smaller one is {}".format(n3))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print("The smaller one is {}".format(menor))

maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print("The bigger one is {}".format(maior))