""" Bass accompany module """
from practice.abstract_url_list import AbstractUrlList


class BassAccompany(AbstractUrlList):
    """ Online lesson class """

    @property
    def _title(self) -> str:
        return "Bass accompany"

    @property
    def _subtitle(self) -> str:
        return "Play along"

    @property
    def _config_section(self) -> str:
        return "bass_accompany"

    def _is_guitar_eligible(self, guitar: dict) -> bool:
        return guitar["type"] == "Bass"
