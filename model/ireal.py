"""IRealPro stuff"""

from pathlib import Path
import random
import re
from typing import List

from pyRealParser import Tune

from config import get_configuration


class IRealBackup:
    """IRealBackup"""

    def __init__(self, tunes: List[Tune]):
        self.tunes = tunes

    def get_random_tune(self) -> Tune:
        """Returns a random tune from the backup file"""
        if not self.tunes or len(self.tunes) == 0:
            return None
        random_tune = random.choice(self.tunes)
        return random_tune

    def get_random_song_name(self) -> str:
        """Returns a random song name from the backup file"""
        random_tune = self.get_random_tune()
        if random_tune is None:
            return ""
        return random_tune.title


class Factory:
    """IRealBackup factory"""

    @staticmethod
    def get_latest_backup_in_config_folder() -> IRealBackup:
        """Returns the latest backup file in the config folder"""
        config = get_configuration()
        backup_folder = config["ireal_backup_folder"]
        return Factory.get_latest_backup_in_folder(backup_folder)

    @staticmethod
    def get_latest_backup_in_folder(backup_folder: str) -> IRealBackup:
        """Returns the latest backup file"""
        latest_html_file = Factory._get_latest_html_file(backup_folder)
        backup_tunes = Factory._get_backup_tunes(latest_html_file)
        return IRealBackup(backup_tunes)

    @staticmethod
    def _get_backup_tunes(backup_path: str) -> List[Tune]:
        """Returns the tunes from the backup file"""
        with open(backup_path, "r", encoding="utf-8") as file:
            content = file.read()

            match = re.search(
                r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>BACKUP</a>', content
            )

            if match:
                ireal_content = match.group(1)
                return Tune.parse_ireal_url(ireal_content)

        return None

    @staticmethod
    def _get_latest_html_file(folder_path):
        directory = Path(folder_path)

        # Find all .html files and get the one with the most recent modification time
        latest_file = max(
            directory.glob("*.html"), key=lambda f: f.stat().st_mtime, default=None
        )

        return latest_file
