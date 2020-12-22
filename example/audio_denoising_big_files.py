import numpy as np
import soundfile

from wavelet.compression import VisuShrinkCompressor
from wavelet.fast_transform import FastWaveletTransform, getExponent
from wavelet.util.utility import snr

INPUT_FILE = "input.wav"
OUTPUT_FILE = "input_denoised.wav"
WAVELET_NAME = "coif1"  # coif1 works vey well

info = soundfile.info(INPUT_FILE)  # getting info of the audio
rate = info.samplerate

t = FastWaveletTransform(WAVELET_NAME)
c = VisuShrinkCompressor()

with soundfile.SoundFile(OUTPUT_FILE, "w", samplerate=rate, channels=info.channels) as of:
    for block in soundfile.blocks(INPUT_FILE, int(rate * info.duration * 0.1)):  # reading 10 % of duration

        print(f"SNR before denoising :: {snr(block)}")

        # coefficients at max level
        level = getExponent(len(block))
        coefficients = t.wavedec(block, level=level)
        coefficients = c.compress(coefficients)
        clean = t.waverec(coefficients, level=level)

        print(f"SNR after denoising :: {snr(clean)}")

        clean = np.asarray(clean)

        of.write(clean)
