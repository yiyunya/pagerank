from numpy import *
from operator import itemgetter, attrgetter
from author_citation_network import AuthorCitationNetwork
from pagerank import PageRank

def rank_author():
    ac_net=AuthorCitationNetwork()
    ac_net_m,ac_net_list=ac_net.make_matrix()
    print("Caculate pagerank...")
    ac_net_pgr=PageRank(ac_net_m)
    ac_net_pr=ac_net_pgr.caculate("author_iter.txt",m_d=1e-5)
    ac_net_results=list(zip(ac_net_list,ac_net_pr.tolist()))
    ac_net_results.sort(key=itemgetter(1),reverse=True)
    results=[]
    for result in ac_net_results:
        results.append(str(result[0][1])+"  "+str(result[1][0])+"\n")
    # results.sort(key=itemgetter(2),reverse=True)
    print("Writing results...")
    f = open("2014/results/author.txt",'w')
    # f.writelines(str(ac_net_results))
    f.writelines(str(results))




