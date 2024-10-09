from enum import Enum
from transcribers.transcriber import Transcriber
import whisper
from libs.io import Writer


class Models(Enum):
    BASE = "base"


class WhisperTranscriber(Transcriber):
    def __init__(self, writer_impl: Writer, model: str = Models.BASE.value) -> None:
        self.__out_writer = writer_impl
        self.__model = whisper.load_model(model)

    def transcribe(self, raw_audio_data):
        result = self.__model.transcribe(raw_audio_data, fp16=False)
        self.__out_writer.write(f"* {result["text"]}")
