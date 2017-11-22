
'''


@author: gjc1211
'''
from HP_Ver2 import url_manager, html_downloader, html_parser, html_output,\
    summary



class spiderMain(object):
    def __init__(self): #
        self.urls = url_manager.UrlManager()  
        self.downloader = html_downloader.HtmlDownLoader()  
        self.output = html_output.HtmlOutPut()  
        self.parser = html_parser.HtmlParser() 
        self.summary =summary.Excel_Summary() 
        
    def craw(self, root_url):
        
        for Dist_Mark in range(1,5): 
            count = 1
            area = []
            hec = []
            price = []
            price_avg = []
            title = []
            mark = []
            
            if Dist_Mark == 1:
                root_url = "http://esf.cz.fang.com/house-a0341/" 
            if Dist_Mark == 2:
                root_url = 'http://esf.cz.fang.com/house-a0339/'
            if Dist_Mark == 3:
                root_url = 'http://esf.cz.fang.com/house-a0338/'
            if Dist_Mark == 4:
                root_url = 'http://esf.cz.fang.com/house-a0342/'
                
            self.urls.__init__()
            self.urls.add_new_url(root_url)
            Dist_Content = []
            
            while self.urls.has_new_url():
                
                try:  
                    new_url = self.urls.get_new_url()  
                    print('craw %d : %s' %(count,new_url))  
                    # 
                     
                    html_context = self.downloader.downloade(new_url)  
                    #print(html_context)
                    new_urls,new_data,mark_same = self.parser.parse(new_url,html_context,mark,title,Dist_Mark)  
                    self.urls.add_new_urls(new_urls) 
                    print(mark_same)
                    if mark_same == 0:
                        pass
                    if mark_same == 1:
                        
                        mark.append(new_data['mark'])
                        area.append(new_data['area']) 
                        hec.append(new_data['hec'])
                        price.append(new_data['price']) 
                        price_avg.append(new_data['price_avg']) 
                        title.append(new_data['title']) 
                    #self.output.collect_data(new_data)  
                    # 
                    if(count==5000):  
                        break  
                    count+=1  
                except:  
                    print("craw failed")  
            if Dist_Mark == 1:
                Dist_Content = 'Xinbei'
            if Dist_Mark == 2:
                Dist_Content = 'Zhonglou'
            if Dist_Mark == 3:
                Dist_Content = 'Tianning'
            if Dist_Mark == 4:
                Dist_Content = 'Wujin'         
            self.output.output_excel(area,hec,price,price_avg,title,Dist_Content)  
            self.summary.output_summary(Dist_Mark)
# main
if __name__ == "__main__":  
    root_url = "http://esf.cz.fang.com/house-a0341/"  
    obj_spider = spiderMain()  
    obj_spider.craw(root_url)