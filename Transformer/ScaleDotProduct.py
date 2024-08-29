import torch
import torch.nn as nn

class ScaleDotProduct(nn.Module):
    def __init__(self):
        super(ScaleDotProduct, self).__init__()

    def forward(self, q, k, v, d_k):
        matmul_qk = torch.matmul(q, k.transpose(-2, -1))
        attention_filter = torch.nn.functional.softmax(matmul_qk/torch.sqrt(torch.tensor(d_k)))
        output = torch.matmul(attention_filter, v)
        return output

batch_size=4
input_seq_length = 5
d_k = 64
d_v= 64

queries = torch.rand(batch_size, input_seq_length, d_k)
keys = torch.rand(batch_size, input_seq_length, d_k)
values = torch.rand(batch_size, input_seq_length, d_v)

attention = ScaleDotProduct()
print(attention(queries, keys, values, d_k).shape)
print(attention(queries, keys, values, d_k))

