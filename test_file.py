from numpy import *
from pagerank import PageRank
# a='916	Bunting,Karl Dieter'
# tmp=a.split()
# print(tmp)
# print(tmp[0])
# ida=tmp[0]
# tmp = tmp[1:]
# print(tmp)
# a=" ".join(tmp)
#
# b='911	Bundy,Alan'
#
# tmp=b.split()
# print(tmp)
# print(tmp[0])
# idb=tmp[0]
# tmp = tmp[1:]
# print(tmp)
# b=" ".join(tmp)
#
# list1=[ida,idb]
#
# list2=[a,b]
#
# d=dict(zip(list1,list2))
#
# aaaa=str(911)
# print(d['911'])
# print(d.get(aaaa))
#
# a=array([[1,2,3],[5,6,7],[8,10,12]])
# print(a[0,1])
# print(a.shape)
# print(a/3)
#
# cccc=1
# bbbb=array([1,2,3,4])
# print(str(cccc)+" "+str(bbbb))
#
# bc="999	17"
# bcc=bc.split()
# print(bcc[1])

# pg=array([[1,1/2,0,1/3],[0,0,1/3,0],[0,0,1/3,1/3],[0,1/2,1/3,1/3]])
# pg_test=PageRank(pg)
# rank=pg_test.caculate("test")
# print(pg_test.matrix)
# print(pg_test.n)
#
# print(rank)
# print(rank.shape)


# a=[1,3,5]
# b=[6,4,2]
# c=list(zip(a,b))
# print(c)

# a=[1,2]
# b=['a']
# print(a+b)

# a=[[1,4],[2,3],[3,1],[8,8],[0,0]]
#
# a.sort(key=lambda x:x[1])
# print(a)

# a='venue = {IJCNLP}'
# b=a.split()
# c=b[2][1:len(b[2])-1]
# print(c)

a='venue = {EACL}'
print(len(a))
print(a[9:len(a)-1])