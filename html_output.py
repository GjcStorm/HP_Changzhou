
'''

@author: gjc1211
'''
import pandas as pd
import shutil
#import matplotlib.pyplot as plt  
import time

class HtmlOutPut(object):  
    def __init__(self):  
        self.datas = []
        
    def collect_data(self,new_data):  
        if(new_data is None):  
            return   
       
    def output_excel(self,area,hec,price,price_avg,title,Dist_Content):  
        #stats_history = [] # 
        local_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        writer = pd.ExcelWriter('HP_output.xlsx', engine='openpyxl')
        df1 = pd.DataFrame(data={'area':area, 'hec':hec, 'price':price, 'price_avg':price_avg, 'title':title})
        df1.sort_values(by=['area','price'],ascending=[0,1],inplace=True)  
        #pd.options.display.float_format ='{:,3f}'.format
        
        df2 = df1.describe()

        df2.to_excel(writer,'Stats_Info')

        df1.to_excel(writer,'HP_data')
        writer.save()
        file_name_append = Dist_Content+'_'+local_time
        file_name = 'HP_output_%s.xlsx' %file_name_append
        file_name = file_name
        print(file_name)
        shutil.copyfile("HP_output.xlsx", file_name)    
        #shutil.move("hello.py", "../")              #hello.txt复制到当前目录的父目录，然后删除hello.txt  
        shutil.move(file_name, "E:\eclipse-workspace\HP_Ver2\HP_Ver2\Data")      #hello2.txt移到当前目录并命名为hello3.py, 然后删除hello2.txt  
        
                
                        
                


