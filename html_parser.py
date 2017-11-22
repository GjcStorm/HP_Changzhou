
'''


@author: gjc1211
'''
from bs4 import BeautifulSoup  
import re  
from urllib import parse  

class HtmlParser(object):
    
        #
        #page_url 
    def _get_new_urls(self,page_url,soup,Dist_Mark):  
        new_urls = set()
        print(Dist_Mark)
        if Dist_Mark == 1:
            Re_Profile = '/house-a0341-'
        if Dist_Mark == 2:
            Re_Profile = '/house-a0339-'
        if Dist_Mark == 3:
            Re_Profile = '/house-a0338-'
        if Dist_Mark == 4:
            Re_Profile = '/house-a0342-' 
        links = soup.find_all('a',href=re.compile(r'%s'%Re_Profile))  
        for link in links:  
            new_url = link["href"]  
            new_full_url = parse.urljoin(page_url,new_url)  
            new_urls.add(new_full_url)  
        return new_urls  
        
    def _get_new_data(self,page_url,soup,mark,title):  
        res_data = {}
#         title_data = []
#         price_data = [] 
#         area_data = []  
        #url_data = []
        #url_data.append(page_url)

        res_data['url'] = page_url  
        
        
        mark_A_node = soup.find('dt',class_="img rel floatl")
        mark_B_node = mark_A_node.find('a',href=re.compile(r'/chushou/'))
        
        
       
        area_A_node = soup.find('p',class_="mt10")
        area_B_node = area_A_node.find('a') # 
        hec_A_node = soup.find('div',class_="area alignR")
        hec_B_node = hec_A_node.find('p')
        price_A_node = soup.find('span',class_="price")
        title_A_node = soup.find('dd',class_="info rel floatr")
        title_B_node = title_A_node.find('p',class_="title") 
        
        hec_data = float(re.sub("\D", "", hec_B_node.get_text()))
        price_data = float(price_A_node.get_text())
        price_avg_data = int(price_data/hec_data*10000)
        print(hec_data)
        if  mark_B_node in mark or title_B_node.get_text() in title or hec_data<80 or hec_data>160 or price_avg_data<6000:
            mark_same = 0
            
        else:
                mark_same = 1
                
                res_data['mark'] = mark_B_node
                res_data['area'] = area_B_node.get_text() 
                res_data['hec'] = float(re.sub("\D", "", hec_B_node.get_text()))
                res_data['price'] = float(price_A_node.get_text())
                res_data['price_avg'] = int(res_data['price']/res_data['hec']*10000)
                res_data['title'] = title_B_node.get_text()

        return res_data, mark_same

    #new_url 
    def parse(self,page_url, html_context, mark, title, Dist_Mark):  
        if(page_url is None or html_context is None):  
            return  
        #python3 
        soup = BeautifulSoup(html_context, "html.parser")  
        new_urls = self._get_new_urls(page_url, soup, Dist_Mark)  
        new_data,mark_same = self._get_new_data(page_url, soup, mark, title)  
        return new_urls,new_data,mark_same