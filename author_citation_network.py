from numpy import *

__all__ = [
    'AuthorCitationNetwork'
]
class AuthorCitationNetwork:

    def read_author_index(self):
        f = open("2014/author_ids.txt")
        print("Loading Author...")
        lines = f.readlines()
        count = 0
        author_index = {}
        author_list = []
        for line in lines:
            tmp = line.split()
            id = tmp[0]
            tmp_1 = tmp[1:]
            name = " ".join(tmp_1)
            author_index[str(id)] = [count,name,0]
            author_list.append([id,name])
            count=count+1
        f_outcites = open("2014/author_outcites.txt")
        print("Loading Author Outcites...")
        oc_lines = f_outcites.readlines()
        for line in oc_lines:
            tmp=line.split()
            author_index[str(tmp[0])][2]=int(tmp[1])
        return author_index,author_list


    def read_author_network(self):


        f_net = open("2014/author_citation_network.txt")

        lines = f_net.readlines()
        index,author_list=self.read_author_index()
        print("Mapping")
        edges=[]
        for line in lines:
            tmp = line.split()
            out_node = tmp[0]
            in_node = tmp[2]
            out_script = index[str(out_node)][0]
            in_script = index[str(in_node)][0]
            edges.append([out_script,in_script,out_node,in_node])
        return edges,index,author_list

    def make_matrix(self):
        print("Mapping Matrix")
        edges,index,author_list = self.read_author_network()
        M = zeros([len(index),len(index)])
        for edge in edges:
            M[edge[0],edge[1]]=1/(index[str(edge[2])][2])
        return M,author_list







