""" Online lesson module """
from practice.abstract_url_list import AbstractUrlList


class OnlineLesson(AbstractUrlList):
    """ Online lesson class """

    @property
    def _title(self) -> str:
        return "Online lesson"

    @property
    def _subtitle(self) -> str:
        return "Take an online lesson"

    @property
    def _config_section(self) -> str:
        return "online_lessons"
