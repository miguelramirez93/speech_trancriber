from libs.io import Writer
from recorders.audio.stream_audio_recorder import StreamAudioRecorder
from typing import Any
from transcribers.whisper_transcriber import WhisperTranscriber


class StdWriter(Writer):
    def write(self, data: Any):
        print(data)


if __name__ == "__main__":
    print("Initializing transcriber deps...")
    transcriber = WhisperTranscriber(StdWriter())
    audio_rec = StreamAudioRecorder()
    try:
        print("Recording started. Press Ctrl+C to stop.")
        audio_rec.start(transcriber.transcribe)

    except KeyboardInterrupt:
        print("\nRecording stopped.")
    except Exception as e:
        print(f"error running recognizer: {str(e)}")
