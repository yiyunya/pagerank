from numpy import *
from operator import itemgetter, attrgetter
from paper_citation_network import PaperCitationNetwork
from pagerank import PageRank


def rank_paper():
    pp_net=PaperCitationNetwork()
    pp_net_m,pp_net_list=pp_net.make_matrix()
    print("Caculating pagerank...")
    pp_net_pgr=PageRank(pp_net_m)
    pp_net_pr=pp_net_pgr.caculate("paper_iter.txt",m_d=1e-7)
    pp_net_results=list(zip(pp_net_list,pp_net_pr.tolist()))
    pp_net_results.sort(key=itemgetter(1))
    results=[]
    for result in pp_net_results:
        results.append(str(result[0][1])+"  "+str(result[1][0])+"\n")
    # results.sort(key=lambda x:-1*x[2])
    # printer=[]
    # for r in results:
    #     printer.append(str(r[1])+"  "+str(r[2])+"\n")
    print("Writing results...")
    f = open("2014/results/paper.txt",'w')
    f.writelines(str(results))





