from cmath import sin, cos, log, pi

def W(nk, N):
    angle = 2 * pi * nk / N
    return cos(angle) - 1j * sin(angle)

def recursive_fft(seq):
    if len(seq) == 2:
        return [seq[0] + seq[1], seq[0] - seq[1]]
    else:
        even = recursive_fft(seq[0::2])
        odd = recursive_fft(seq[1::2])
        N = len(seq)
        w = [W(k, N) for k in range(0, N // 2)]
        left = [even[k] + odd[k] * w[k] for k in range(0, N // 2)]
        right = [even[k] - odd[k] * w[k] for k in range(0, N // 2)]
        return left + right

#def fft(generator):
#    seq, len = generator()
#    try:
#        if not (len & (len - 1)) == 0:
#            raise ValueError('len')
#    except ValueError:
#        print('len')
#    layer = int(abs(log(len, 2)))
    
import numpy as np
seq = range(0, 128)
print(np.fft.fft(seq))
print(recursive_fft(seq))