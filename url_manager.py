# coding=gbk 
'''


@author: gjc1211
'''


class UrlManager:  
    'url������'  
    #���캯����ʼ��set���� 
    
    def __init__(self):  
        self.new_urls = set() #����ȡ��url  
        self.old_urls = set() #����ȡ��url  
  
    #������������һ���µ�url  
    def add_new_url(self,root_url):  
        if(root_url is None):  
            return  
        if(root_url not in self.new_urls and root_url not in self.old_urls):  
            #�Ȳ��ڴ���ȡ��urlҲ��������ȡ��url�У���һ��ȫ�µ�url����˽�����ӵ�new_urls  
            self.new_urls.add(root_url)  
  
    # �����������������µ�url  
    def add_new_urls(self,urls):  
        if(urls is None or len(urls) == 0):  
            return  
        for url in urls:  
            self.add_new_url(url) #����add_new_url()  
  
    #�ж��Ƿ����µĴ���ȡ��url  
    def has_new_url(self):  
        return len(self.new_urls) != 0  
    #��ȡһ������ȡ��url  
    def get_new_url(self):  
        new_url = self.new_urls.pop()  
        self.old_urls.add(new_url)  
        return new_url  