import os
import pandas as pd
def ReadFile(path):

    alldata = pd.DataFrame()
    for root,dirs,files in os.walk(path):
        print(root,dirs,files)
        print('#'*100)
        for ind,file  in enumerate(files):
            # 使用join函数将文件名称和文件所在根目录连接起来


            # if ind<2:

                full=os.path.join(root, file)
                print(full)

                JanAllData=pd.read_excel(full)
                #数据太大啦 随机抽一点
                JanAllData=JanAllData.sample(20000)

                alldata=pd.concat([alldata,JanAllData])
        #
        alldata.to_excel('JanAllData.xlsx')
    return alldata
path1=r'.\1月'
ReadFile(path1)
print('aaa')