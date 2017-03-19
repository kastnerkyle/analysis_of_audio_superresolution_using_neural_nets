import matplotlib.pyplot as plt
import sys
from scipy.io import wavfile

fname1 = sys.argv[1]
fs1, d1 = wavfile.read(fname1)


fname2 = sys.argv[2]
fs2, d2 = wavfile.read(fname2)

f, axarr = plt.subplots(1, 2)

nfft = 2048
noverlap = int(.8 * nfft)
kwargs = {"interpolation":None,
        "noverlap":noverlap,
        "NFFT":nfft,
        "cmap":"gray"}
axarr[0].specgram(d1, **kwargs)
axarr[0].set_title(fname1)
axarr[1].specgram(d2, **kwargs)
axarr[1].set_title(fname2)
plt.show()
