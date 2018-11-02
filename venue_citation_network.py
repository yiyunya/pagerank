from numpy import *
from paper_citation_network import PaperCitationNetwork
__all__ = [
    'VenueCitationNetwork'
]
class VenueCitationNetwork:

    def read_unit(self,f):
        im={}
        im_list=[]
        while True:
            l_1=f.readline()
            if l_1:
                w1=l_1.split()
                if w1:
                    if w1[0] == 'id':
                        paper_id = w1[2][1:len(w1[2]) - 1]
                        l_2 = f.readline()
                        l_3 = f.readline()
                        l_4 = f.readline()
                        l_5 = f.readline()
                        w2 = l_4[9:len(l_4)-2]
                        venue_id = w2
                        w3 = l_5.split()
                        year_id = w3[2][1:len(w3[2]) - 1]
                        if [venue_id, year_id, 0] not in im_list:
                            im_list.append([venue_id, year_id, 0])
                        im[str(paper_id)] = [venue_id, year_id, im_list.index([venue_id, year_id, 0])]

            else:
                break
        return im,im_list



    def read_venue_index(self):
        f = open("2014/acl-metadata.txt")
        print("Loading metadata...")
        venue_index,venue_list=self.read_unit(f)
        count = 0
        pcn=PaperCitationNetwork()
        f_net = open("2014/networks/paper-citation-network.txt")
        print("Loading paper citation...")

        lines = f_net.readlines()
        pp_index, paper_list = pcn.read_paper_index()
        edges = []
        for line in lines:
            tmp = line.split()
            out_node = tmp[0]
            in_node = tmp[2]
            out_script = venue_index[str(out_node)][2]
            in_script = venue_index[str(in_node)][2]
            edges.append([out_script, in_script])
            venue_list[venue_index[str(out_node)][2]][2]=venue_list[venue_index[str(out_node)][2]][2]+1
        return edges,venue_index,venue_list
        #
        # for line in lines:
        #     tmp = line.split()
        #     id = tmp[0]
        #     tmp_1 = tmp[1:]
        #     name = " ".join(tmp_1)
        #     author_index[str(id)] = [count,name,0]
        #     author_list.append([id,name])
        #     count=count+1
        # f_outcites = open("2014/author_outcites.txt")
        # oc_lines = f_outcites.readlines()
        # for line in oc_lines:
        #     tmp=line.split()
        #     author_index[str(tmp[0])][2]=int(tmp[1])
        # return author_index,author_list


    def make_matrix(self):
        print("Mapping...")
        edges,index,venue_list = self.read_venue_index()
        M = zeros([len(venue_list),len(venue_list)])
        for edge in edges:
            M[edge[0],edge[1]]=1/(venue_list[edge[0]][2])
        return M,venue_list



