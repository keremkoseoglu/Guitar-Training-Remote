""" Guitar accompany module """
from practice.abstract_url_list import AbstractUrlList


class GuitarAccompany(AbstractUrlList):
    """ Online lesson class """

    @property
    def _title(self) -> str:
        return "Guitar accompany"

    @property
    def _subtitle(self) -> str:
        return "Play along"

    @property
    def _config_section(self) -> str:
        return "guitar_accompany"

    @staticmethod
    def _is_guitar_eligible(guitar: dict) -> bool:
        return guitar["type"] == "Guitar"
