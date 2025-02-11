

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import streamlit as st

# Streamlit app title
st.title('Signal Analysis with Spectrogram and Histogram')

# File upload widget
uploaded_file = st.file_uploader("Upload CSV File", type="csv")

if uploaded_file is not None:
    # Reading the uploaded data file
    df = pd.read_csv(uploaded_file, header=None)

    # Plotting Line Plots for each Channel (3 channels)
    st.subheader('Line Plot for Each Channel')
    for channel_idx in range(df.shape[0]):
        fig, ax = plt.subplots(figsize=(10, 3))
        ax.plot(df.columns, df.iloc[channel_idx, :], label=f'Channel {channel_idx+1}')
        ax.set_title(f'Signal for Channel {channel_idx+1}')
        ax.set_xlabel('Sample Index')
        ax.set_ylabel('Amplitude')
        ax.legend()
        st.pyplot(fig)

    # Spectrogram for each channel (using scipy.signal.spectrogram)
    fs = 16000  # Assume sampling rate, adjust as per your data

    st.subheader('Spectrogram for Each Channel')
    for channel_idx in range(df.shape[0]):
        data_signal = df.iloc[channel_idx, :].values  # Convert to numpy array
        f, t, Sxx = signal.spectrogram(data_signal, fs=fs, nperseg=256)

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.pcolormesh(t, f, Sxx, shading='gouraud')
        ax.set_title(f'Spectrogram for Channel {channel_idx+1}')
        ax.set_ylabel('Frequency [Hz]')
        ax.set_xlabel('Time [s]')
        fig.colorbar(ax.pcolormesh(t, f, Sxx, shading='gouraud'), ax=ax, label='Intensity')
        st.pyplot(fig)

    # Histogram of Amplitude Distribution for each channel
    st.subheader('Amplitude Histogram for Each Channel')
    for channel_idx in range(df.shape[0]):
        fig, ax = plt.subplots(figsize=(6, 3))
        df.iloc[channel_idx, :].plot(kind='hist', bins=30, alpha=0.7, ax=ax)
        ax.set_title(f'Amplitude Histogram for Channel {channel_idx+1}')
        ax.set_xlabel('Amplitude')
        ax.set_ylabel('Frequency')
        st.pyplot(fig)

