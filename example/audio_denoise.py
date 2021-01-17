import numpy as np
import soundfile

from wavelet import FastWaveletTransform, VisuShrinkCompressor

INPUT_FILE = ""
OUTPUT_FILE = ""
WAVELET_NAME = "coif1"  # coif1 works vey well

info = soundfile.info(INPUT_FILE)  # getting info of the audio
rate = info.samplerate

t = FastWaveletTransform(WAVELET_NAME)
c = VisuShrinkCompressor()

with soundfile.SoundFile(OUTPUT_FILE, "w", samplerate=rate, channels=1) as of:
    for block in soundfile.blocks(INPUT_FILE, int(rate * info.duration * 0.1)):

        # converting to mono [can do 2D, bit with 2 channels that is useless & slow]
        if block.ndim > 1:
            block = block.sum(axis=1) / 2

        coefficients = t.wavedec(block)
        coefficients = c.compress(coefficients)
        clean = t.waverec(coefficients)

        clean = np.asarray(clean, dtype=np.float_)
        of.write(clean)
