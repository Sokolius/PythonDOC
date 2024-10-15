import matplotlib.pyplot as plt

class Graph:
    def __init__(self,x_data,y_data, title,x_lable,y_lable):
        self.x_data = x_data
        self.y_data = y_data
        self.title = title
        self.x_lable = x_lable
        self.y_lable = y_lable

    def draw(self):
        plt.plot(self.x_data,self.y_data)
        plt.title(self.title)
        plt.xlabel(self.x_lable)
        plt.ylabel(self.y_lable)
        plt.savefig('testgr.png',transparent = True)

    def drawsubject(self):
        bouthlist = self.x_data
        name_bouth = [bouth[1] for bouth in bouthlist]
        sum_bouth = [bouth[2] for bouth in bouthlist]

        soldlist = self.y_data
        name_sold = [sold[1] for sold in soldlist]
        sum_sold = [sold[2] for sold in soldlist]

        index = range(max(len(name_bouth),len(name_sold)))
        wigth = 0.35

        index_bouth = [i - wigth/2 for i in index[:len(name_bouth)]]
        index_sold = [i + wigth/2 for i in index[:len(name_sold)]]

        plt.barh(index_bouth,sum_bouth,wigth,label = 'Покупка')
        plt.barh(index_sold,[-x for x in sum_sold],wigth,label = 'Продажа')

        plt.xlabel(self.x_lable)
        plt.ylabel(self.y_lable)
        plt.title(self.title)

        name_all = name_bouth+name_sold
        if len(name_all)>len(index):
            index=range(len(name_all))
        plt.yticks(index)
        # index_all = list(index)[:len(name_sold) + len(name_bouth)]
        # name_all = name_sold+name_bouth
        # plt.gca().set_xticks(index_all)
        # plt.gca().set_xticklabels(name_all,rotation=45)
        plt.legend

        col_bouth = plt.gca().patches[:len(name_bouth)]
        col_sold = plt.gca().patches[:len(name_sold)]

        for col,name,sumb in zip(col_bouth,name_bouth,sum_bouth):
            wid_col = col.get_width()
            plt.text(wid_col/2,col.get_y()+col.get_height()/2, name + str(round(sumb,1)) +" млн. долларов США в экв.",ha ='left',va='center')

        for col_s,name,sums in zip(col_sold,name_sold,sum_sold):
            wid_cols = col_s.get_width()
            x_pos = wid_cols - sum([col1.get_width() for col1 in col_sold])
            plt.text(x_pos/2,col_s.get_y()+col_s.get_height()*1.5, name+ str(round(sums,1)) +" млн. долларов США в экв.",ha ='left',va='center')

        plt.savefig('testgr.png', transparent=True,format = 'png',dpi = 300)
    def drowpie(self):
        cur_shares = self.x_data
        cur_lable = self.y_data
        for cs in range(len(cur_shares)):
            if cur_shares[cs]<0:
                cur_shares[cs] *=-1
        plt.pie(cur_shares,labels=cur_lable,autopct='%1.1f%%')
        plt.savefig('testgr.png', transparent=True,format = 'png',dpi = 300)

    def closeplt(self):
        plt.close()