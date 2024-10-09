from transcribers.transcriber import Transcriber
import whisper
from libs.io import Writer


class WhisperTranscriber(Transcriber):
    def __init__(self, writer_impl: Writer) -> None:
        self.__out_writer = writer_impl
        self.__model = whisper.load_model("base")

    def transcribe(self, raw_audio_data):
        result = self.__model.transcribe(raw_audio_data, fp16=False)
        self.__out_writer.write(f"* {result["text"]}")
