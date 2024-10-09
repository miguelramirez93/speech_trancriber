import abc


class Transcriber(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def transcribe(self, raw_audio_data):
        pass
