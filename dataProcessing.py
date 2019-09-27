import jieba

'''def read_order():
    file=open('data/order.txt','r',encoding='utf-8')

    order_list=[]

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
    print(order_list[0],order_list[1])
'''

def read_ware():
    file=open('data/ware.txt','r',encoding='utf-8')
    ware_dict={}
    lines=file.readlines()
    for i in range(1,len(lines)):
        line=lines[i].strip()
        line_list=line.split('\t')
        ware_dict[line_list[0]]=line_list[1]
        #if i==968:
            #print(line_list)

    return ware_dict

def read_chat(line_num=10000):
    file=open('data/chat.txt','r',encoding='utf-8')
    lines=file.readlines()
    conversation_id=lines[1].strip().split('\t')[0]
    conversations=[]
    #单次对话的所有句子
    sentences=[]
    nowsentence=''
    nowspeaker='0'
    print(lines[-1])
    for i in range(1,line_num+1):
        line=lines[i].strip()
        line_list=line.split('\t')
        if line_list[0]!=conversation_id or i==line_num:
            sentences.append(nowsentence)
            nowspeaker=line_list[2]
            nowsentence=line_list[-1]
            conversations.append(make_sentences_pair(sentences))
            conversation_id=line_list[0]
        else:
            if line_list[2]==nowspeaker:
                if nowsentence=='':
                    nowsentence=line_list[-1]
                else:
                    nowsentence+='，'+line_list[-1]
            else:
                sentences.append(nowsentence)
                nowsentence=line_list[-1]
                nowspeaker=line_list[2]

    print(conversations[0])
    return conversations


def make_sentences_pair(sentences):
    result=[]
    for i in range(len(sentences)-1):
        result.append([sentences[i],sentences[i+1]])
    return result

if __name__=='__main__':
    #read_order()
    read_ware()
    read_chat()
