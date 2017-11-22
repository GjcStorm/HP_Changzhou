# coding=gbk  
'''
Created on 2017年11月13日

@author: gjc1211
'''

#<span style="font-size:12px;">from urllib import request  


import requests

class HtmlDownLoader:  

        def downloade(self,new_url):
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
                        'Chrome/51.0.2704.63 Safari/537.36'}  
            if(new_url is None):  
                return None  
            r = requests.get(new_url,headers) 
            if (r.status_code) != 200:
                return None
            html = r.text
            return html
    