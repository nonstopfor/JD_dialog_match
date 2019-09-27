import torch
import torch.nn as nn
from torch.autograd import Variable

use_cuda=torch.cuda.is_available()
class BaseEncoder(nn.Module):
    def __init__(self,hidden_size,embedding,n_layers=1):
        super(BaseEncoder,self).__init__()
        self.hidden_size=hidden_size
        self.embedding=embedding
        self.n_layers=n_layers

        # suppose hidden_size=input_size
        self.gru=nn.GRU(hidden_size,hidden_size,n_layers)

    def forward(self,input_seq,input_lengths,hidden=None):
        embedded=self.embedding(input_seq)
        packed = nn.utils.rnn.pack_padded_sequence(embedded, input_lengths)
        outputs, hidden = self.gru(packed, hidden)
        outputs,_=nn.utils.rnn.pad_packed_sequence(outputs)

        return outputs,hidden



class SessionEncoder(nn.Module):
    def __init__(self,hidden_size,batch_size):
        super(SessionEncoder, self).__init__()
        self.hidden_size=hidden_size
        self.gru=nn.GRU(hidden_size,hidden_size)
        init_hidden=Variable(torch.zeros(1,batch_size,hidden_size))

        self.last_hidden=init_hidden
        if use_cuda:
            self.last_hidden=self.last_hidden.cuda()


    def forward(self,x):
        output,hidden=self.gru(x,self.last_hidden)
        self.last_hidden=hidden
        return output,hidden

class Decoder(nn.Module):
    def __init__(self,hidden_size):
        super(Decoder,self).__init__()
        self.gru=nn.GRU(hidden_size,hidden_size)
        self.last_hidden=None

    def forward(self,input,hidden=None):
        if hidden==None:
            output,hidden=self.gru(input,self.last_hidden)
            self.last_hidden=hidden
        else:
            output,hidden=self.gru(input,hidden)
            self.last_hidden=hidden
        return output





