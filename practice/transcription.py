""" Transcription module """
from practice.abstract_url_list import AbstractUrlList


class Transcription(AbstractUrlList):
    """ Transacription class """

    @property
    def _title(self) -> str:
        return "Transcription"

    @property
    def _subtitle(self) -> str:
        return "Transcribe:"

    @property
    def _config_section(self) -> str:
        return "transcriptions"
