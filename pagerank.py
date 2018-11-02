from numpy import *

__all__ = [
    'PageRank'
]

class PageRank:
    def __init__(self,M):
        self.matrix=M
        self.n=M.shape[0]
    def caculate(self,filestr,damping_factor=0.85,max_iteration=1000,m_d=0.00001):
        rank=ones((self.n,1))/self.n
        f=open("/Users/yingliu/PycharmProjects/pagerank/2014/results/"+filestr,'w')
        for i in range(0,max_iteration):
            f.write(str(i)+str(rank)+"\n")
            tmp=rank
            rank=damping_factor*dot(self.matrix,rank)+(1-damping_factor)*rank;
            diff=tmp-rank
            f.write(str(diff) + "\n")
            if amax(diff)<m_d:
                break
        f.write(str(i)+" "+str(rank))

        return rank






