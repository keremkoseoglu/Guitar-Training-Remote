"""IRealPro stuff"""

from pathlib import Path
import random
import re
from typing import List, Protocol

from pyRealParser import Tune

from config import get_configuration

##############################
# Domain model
##############################


class SongArray:
    """SongArray"""

    def __init__(self, songs: List[str]):
        self.songs = songs

    def get_random(self) -> str:
        """Returns a random song"""
        if not self.songs or len(self.songs) == 0:
            return ""
        random_song = random.choice(self.songs)
        return random_song


class SongArrayRepository(Protocol):
    """SongArrayRepository"""

    def get_name(self) -> str:
        """Returns the name of the repository"""

    def get_song_array(self) -> SongArray:
        """Returns a SongArray"""


##############################
# iReal Pro
##############################
class IRealBackup:
    """IRealBackup, implements SongArrayRepository"""

    def __init__(self, file_name: str, tunes: List[Tune]):
        self._file_name = file_name
        self._tunes = tunes
        self._song_array_cache = None

    def get_name(self) -> str:
        """Returns the name of the repository"""
        return self._file_name

    def get_song_array(self) -> SongArray:
        """Returns a SongArray"""
        if self._song_array_cache is None:
            song_names = [tune.title for tune in self._tunes]
            self._song_array_cache = SongArray(song_names)
        return self._song_array_cache


class IRealBackupCache:
    """IRealBackupCache, implements SongArrayRepository"""

    def __init__(self, file_name: str, songs: List[str]):
        self._file_name = file_name
        self._songs = songs
        self._song_array_cache = None

    def get_name(self) -> str:
        """Returns the name of the repository"""
        return self._file_name

    def get_song_array(self) -> SongArray:
        """Returns a SongArray"""
        if self._song_array_cache is None:
            self._song_array_cache = SongArray(self._songs)
        return self._song_array_cache


##############################
# Infrastructure
##############################


class FileSystem:
    """User's file system"""

    def obtain_latest_backup_songs(self) -> SongArray:
        """Returns the songs from the latest backup file in the config folder"""
        latest_backup_name = self.get_latest_backup_name_in_config_folder()

        if latest_backup_name is None:
            return None

        latest_cache_name = self.get_latest_cache_name_in_config_folder()

        if latest_cache_name is None or latest_cache_name != latest_backup_name:
            latest_backup = self.get_latest_backup_in_config_folder()
            songs = latest_backup.get_song_array().songs
            self.save_cache(latest_backup.get_name(), songs)

        latest_cache = self.get_latest_cache_in_config_folder()
        return latest_cache.get_song_array()

    ##############################
    # iReal CACHE
    ##############################

    def get_latest_cache_in_folder(self, cache_folder: str) -> SongArrayRepository:
        """Returns the latest backup file"""
        latest_txt_path = self._get_latest_txt_path(cache_folder)

        if latest_txt_path is None:
            return None

        cache_songs = self._file_to_list(latest_txt_path)
        latest_txt_file = Path(latest_txt_path).stem
        return IRealBackupCache(latest_txt_file, cache_songs)

    def get_latest_cache_in_config_folder(self) -> SongArrayRepository:
        """Returns the latest cache file in the config folder"""
        config = get_configuration()
        cache_folder = config["ireal_cache_folder"]
        return self.get_latest_cache_in_folder(cache_folder)

    def get_latest_cache_name_in_folder(self, cache_folder: str) -> str:
        """Returns the name of the latest cache file in the given folder"""
        latest_txt_path = self._get_latest_txt_path(cache_folder)
        if latest_txt_path is None:
            return None
        return Path(latest_txt_path).stem

    def get_latest_cache_name_in_config_folder(self) -> str:
        """Returns the name of the latest cache file in the config folder"""
        config = get_configuration()
        cache_folder = config["ireal"]["cache_folder"]
        return self.get_latest_cache_name_in_folder(cache_folder)

    def save_cache(self, name: str, songs: List[str]):
        """Saves the cache to a file in the config folder"""
        config = get_configuration()
        cache_folder = config["ireal"]["cache_folder"]
        cache_path = Path(cache_folder) / (name + ".txt")
        with open(cache_path, "w", encoding="utf-8") as file:
            file.write("\n".join(songs))

    ##############################
    # iReal BACKUP
    ##############################

    def get_latest_backup_in_folder(self, backup_folder: str) -> SongArrayRepository:
        """Returns the latest backup file"""
        latest_html_path = self._get_latest_html_path(backup_folder)
        backup_tunes = self._get_backup_tunes(latest_html_path)
        latest_html_file = Path(latest_html_path).stem
        return IRealBackup(latest_html_file, backup_tunes)

    def get_latest_backup_in_config_folder(self) -> SongArrayRepository:
        """Returns the latest backup file in the config folder"""
        config = get_configuration()
        backup_folder = config["ireal"]["backup_folder"]
        return self.get_latest_backup_in_folder(backup_folder)

    def get_latest_backup_name_in_folder(self, backup_folder: str) -> str:
        """Returns the name of the latest backup file in the given folder"""
        latest_html_path = self._get_latest_html_path(backup_folder)
        if latest_html_path is None:
            return None
        return Path(latest_html_path).stem

    def get_latest_backup_name_in_config_folder(self) -> str:
        """Returns the name of the latest backup file in the config folder"""
        config = get_configuration()
        backup_folder = config["ireal"]["backup_folder"]
        return self.get_latest_backup_name_in_folder(backup_folder)

    ##############################
    # Utility
    ##############################

    def _get_backup_tunes(self, backup_path: str) -> List[Tune]:
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

    def _file_to_list(self, filepath: str) -> List[str]:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read().splitlines()

    def _get_latest_html_path(self, folder_path) -> str:
        """Returns the path of the latest .html file in the given folder"""
        return self._get_latest_extension_path(folder_path, "html")

    def _get_latest_txt_path(self, folder_path) -> str:
        """Returns the path of the latest .txt file in the given folder"""
        return self._get_latest_extension_path(folder_path, "txt")

    def _get_latest_extension_path(self, folder_path, extension) -> str:
        directory = Path(folder_path)

        # Find all .html files and get the one with the most recent modification time
        latest_path = max(
            directory.glob("*." + extension),
            key=lambda f: f.stat().st_mtime,
            default=None,
        )

        return latest_path
