from libs.io import FileWriter
from recorders.audio.stream_audio_recorder import StreamAudioRecorder
from transcribers.whisper_transcriber import WhisperTranscriber


if __name__ == "__main__":
    print("Initializing transcriber deps...")
    transcriber = WhisperTranscriber(FileWriter("./transcription.txt"))
    audio_rec = StreamAudioRecorder()
    try:
        print("Recording started. Press Ctrl+C to stop.")
        audio_rec.start(transcriber.transcribe)

    except KeyboardInterrupt:
        print("\nRecording stopped.")
    except Exception as e:
        print(f"error running recognizer: {str(e)}")
