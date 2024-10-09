import abc


class AudioRecorder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def start(self, callback):
        pass

    @abc.abstractmethod
    def stop(self):
        pass
