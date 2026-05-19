import librosa
import numpy as np
import soundfile as sf
from scipy.signal import correlate

audio_file = "audio_auv.mpeg"

waveform, sample_rate = librosa.load(audio_file)
#print("Sample loaded")
#print("sample rate:", sample_rate)

sf.write("audio_auv.wav", waveform, sample_rate)

def create_delay(sig, delay_sec,sr):
    delay_samples = int(delay_sec *sr)
    
    delayed = np.concatenate((np.zeros(delay_samples),sig))
    return delayed


signal0 = create_delay(waveform,0,sample_rate)
signal1 = create_delay(waveform,1,sample_rate)
signal2 = create_delay(waveform,2,sample_rate)

sf.write("delay0.wav",signal0,sample_rate)
sf.write("delay1.wav",signal1,sample_rate)
sf.write("delay2.wav",signal2,sample_rate)

def pad(sig,length):
    return np.pad(sig,(0,length-len(sig)))

def normalised_corr(a,b):
    corr=correlate(a,b,mode='full')
    max_corr = np.max(np.abs(corr))

    norm = np.linalg.norm(a) * np.linalg.norm(b)
    return max_corr/norm

max_len = max(len(signal0), len(signal1), len(signal2))

sig0_p = pad(signal0, max_len)
sig1_p = pad(signal1, max_len)
sig2_p = pad(signal2, max_len)

corr01 = normalised_corr(sig0_p, sig1_p)
corr11 = normalised_corr(sig1_p, sig1_p)
corr21 = normalised_corr(sig2_p, sig1_p)


print("Correlation - 0s vs 1s:", corr01)
print("Correlation - 1s vs 1s:", corr11)
print("Correlation - 2s vs 1s:", corr21)

# b part

signal3 = create_delay(waveform,3,sample_rate)
new=sig0_p +sig2_p

new_len = max(len(new), len(signal3))

new_sig = pad(new,new_len)

signal0_p =pad(sig0_p,new_len)
signal1_p =pad(sig1_p,new_len)
signal2_p =pad(sig2_p,new_len)
signal3_p =pad(signal3,new_len)

corr0 = normalised_corr(signal0_p,new_sig)
corr1 = normalised_corr(signal1_p,new_sig)
corr2 = normalised_corr(signal2_p,new_sig)
corr3 = normalised_corr(signal3_p,new_sig)

print("\n")
print("Correlation - 0s vs new signal:", corr0)
print("Correlation - 1s vs new signal:", corr1)
print("Correlation - 2s vs new signal:", corr2)
print("Correlation - 3s vs new signal:", corr3)

