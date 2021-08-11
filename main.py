"""Example program to show how to read a multi-channel time series from LSL."""
import mne
import numpy as np
import matplotlib.pyplot as plt
from pylsl import StreamInlet, resolve_stream



# Lab Streaming Layer running on Neurosity Crown headset
# Ensure Neurosity Crown is connected to same WiFi network as computer
# Reference: https://support.neurosity.co/hc/en-us/articles/360039387812-Reading-data-into-Python-via-LSL

try:
    # first resolve an EEG stream on the lab network
    print("looking for an EEG stream...")
    streams = resolve_stream('type', 'EEG')
    # create a new inlet to read from the stream
    inlet = StreamInlet(streams[0])
    while True:
        # get a new sample (you can also omit the timestamp part if you're not
        # interested in it)
        sample, timestamp = inlet.pull_sample()
except KeyboardInterrupt as e:
    print("Ending program")
    raise e


# MNE Stuff
# Reference: https://jasmainak.github.io/mne-workshop-brown/evoked_to_stc/stc.html

data = sample

raw = mne.io.read_raw_fif(sample)


# ??? What is stim_channel? -- Regardless the code executes
events = mne.find_events(raw, stim_channel='STI 014')







