import jieba

def read_order():
    file=open('data/order.txt','r',encoding='utf-8')

    '''order_list=[]

    lines=file.readlines()
    print(lines[0],lines[1])
    print(len(lines))
    for i in range(1,len(lines)):
        line=lines[i].strip()
        words=line.split('\t')
        if i==1:
            #print(words[-1])
            for word in words:
                mydist={}
                #mydist[]
                print(word)
        mydist={}
        mydist['orderid']=words[0]
        mydist['userid']=words[1]
        mydist['sku']=words[2]
        mydist['kind']=words[3]
        mydist['status']=words[4]
        order_list.append(mydist)
    print(order_list[0],order_list[1])'''

if __name__=='__main__':
    read_order()
