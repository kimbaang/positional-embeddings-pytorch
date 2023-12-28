import math
import torch

from einops import rearrange

def sinusoidal_embed_1d(channel_dim, time_dim, max_scale=1e4):
    assert channel_dim % 2 == 0

    logtime_delta = math.log(max_scale) / (channel_dim // 2 - 1)
    inv_timescales = torch.exp(-logtime_delta * torch.arange(channel_dim // 2))
    scaled_time = torch.einsum('i,j->ij', torch.arange(time_dim), inv_timescales)
    
    return torch.cat([torch.sin(scaled_time), torch.cos(scaled_time)], dim=1)

if __name__ == '__main__':
    embeds = sinusoidal_embed_1d(channel_dim=64, time_dim=256)
    print(embeds)
    print(embeds.shape)