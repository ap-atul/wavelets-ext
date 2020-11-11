import numpy as np
import soundfile

from wavelet.compression import VisuShrinkCompressor
from wavelet.fast_transform import FastWaveletTransform, getExponent

INPUT_FILE = "input.wav"
OUTPUT_FILE = "output.wav"
WAVELET_NAME = "coif1"  # coif1 works vey well

info = soundfile.info(INPUT_FILE)  # getting info of the audio
rate = info.samplerate

t = FastWaveletTransform(WAVELET_NAME)
c = VisuShrinkCompressor()

with soundfile.SoundFile(OUTPUT_FILE, "w", samplerate=rate, channels=1) as of:
    for block in soundfile.blocks(INPUT_FILE, int(rate * info.duration * 0.1)):  # reading 10 % of duration

        # processing only single channel [well 1D]
        if block.ndim > 1:
            block = block.T
            block = block[0]

        # coefficients at max level
        level = getExponent(len(block))
        coefficients = t.wavedec(block, level=level)
        coefficients = c.compress(coefficients)
        clean = t.waverec(coefficients, level=level)

        clean = np.asarray(clean)
        of.write(clean)
