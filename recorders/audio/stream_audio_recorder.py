import queue
from recorders.audio.audio_recorder import AudioRecorder
import sounddevice as sd
import numpy as np


class StreamAudioRecorder(AudioRecorder):
    def __init__(self, rec_sample_time: int = 5, rec_sample_rate: int = 16000) -> None:
        self.__rec_sample_time = rec_sample_time
        self.__rec_sample_rate = rec_sample_rate
        self.__audio_queue = queue.Queue()

    def start(self, callback):
        with sd.InputStream(
            callback=self.__audio_callback,
            channels=1,
            samplerate=self.__rec_sample_rate,
        ):
            # Initialize an empty list to store audio frames
            audio_buffer = np.empty((0, 1), dtype=np.float32)

            try:
                while True:
                    # Wait until the queue has some data
                    audio_data = self.__audio_queue.get()

                    # Append new audio data to the buffer
                    audio_buffer = np.vstack((audio_buffer, audio_data))

                    # Process the buffer in chunks
                    if (
                        len(audio_buffer)
                        >= self.__rec_sample_rate * self.__rec_sample_time
                    ):
                        # Normalize and convert buffer to a format Whisper expects
                        audio_array = audio_buffer.flatten()
                        audio_buffer = np.empty(
                            (0, 1), dtype=np.float32
                        )  # Clear the buffer

                        # Perform transcription
                        callback(audio_array)

            except KeyboardInterrupt:
                print("\nRecording stopped.")

    def __audio_callback(self, indata, frames, time, status):
        if status:
            print(status)
        # Add the captured audio data to the queue
        self.__audio_queue.put(indata.copy())

    def stop(self):
        return super().stop()
