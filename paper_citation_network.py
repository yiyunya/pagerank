from numpy import *

__all__ = [
    'PaperCitationNetwork'
]
class PaperCitationNetwork:

    def read_paper_index(self):
        f = open("2014/paper_ids.txt")
        print("Loading papers...")
        lines = f.readlines()
        count = 0
        paper_index = {}
        paper_list = []
        for line in lines:
            tmp = line.split()
            id = tmp[0]
            tmp_1 = tmp[1:]
            name = " ".join(tmp_1)
            paper_index[str(id)] = [count,name,0]
            paper_list.append([id,name])
            count=count+1
        f_outcites = open("2014/paper_outcites.txt")
        print("Loading papers outcites...")
        oc_lines = f_outcites.readlines()
        for line in oc_lines:
            tmp=line.split()
            paper_index[str(tmp[0])][2]=int(tmp[1])
        return paper_index,paper_list


    def read_paper_network(self):


        f_net = open("2014/networks/paper-citation-network.txt")

        lines = f_net.readlines()
        index,paper_list=self.read_paper_index()
        print("Mapping...")
        edges=[]
        for line in lines:
            tmp = line.split()
            out_node = tmp[0]
            in_node = tmp[2]
            out_script = index[str(out_node)][0]
            in_script = index[str(in_node)][0]
            edges.append([out_script,in_script,out_node,in_node])
        return edges,index,paper_list

    def make_matrix(self):
        print("Mapping Matrix...")
        edges,index,paper_list = self.read_paper_network()
        M = zeros([len(index),len(index)])
        for edge in edges:
            M[edge[0],edge[1]]=1/(index[str(edge[2])][2])
        return M,paper_list



