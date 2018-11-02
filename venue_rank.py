from numpy import *
from operator import itemgetter, attrgetter
from venue_citation_network import VenueCitationNetwork
from pagerank import PageRank



def rank_venue():
    vn_net=VenueCitationNetwork()
    vn_net_m,vn_net_list=vn_net.make_matrix()
    print("Caculating pagerank...")
    vn_net_pgr=PageRank(vn_net_m)
    vn_net_pr=vn_net_pgr.caculate("venue_iter.txt",m_d=1e-7)
    vn_list=[]
    for vn in vn_net_list:
        vn_list.append(vn[0:2])
    vn_net_results=list(zip(vn_list,vn_net_pr.tolist()))
    vn_net_results.sort(key=itemgetter(1),reverse=True)
    # ac_net_results.sort(key=lambda x:-1*x[1])
    results=[]
    for result in vn_net_results:
        results.append(str(result[0][0])+"  "+str(result[0][1])+"   "+str(result[1][0])+"\n")
    f = open("2014/results/venue.txt",'w')
    # f.writelines(str(vn_net_results))
    f.writelines(results)
    print("Writing results...")



