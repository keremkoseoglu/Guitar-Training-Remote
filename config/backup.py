""" Backup module """
from datetime import datetime
from os import makedirs, scandir, path
from shutil import copyfile, rmtree
from config import get_dir_path, get_data_dir_path

class Backup:
    """ Backup class """
    _BACKUP_DIR = "backup"
    _MAX_BACKUPS = 5

    def run(self):
        """ Runs a new backup operation """
        try:
            self.remove_old_backups()
        except Exception:
            pass

        try:
            self.create_new_backup()
        except Exception:
            pass

    def remove_old_backups(self):
        """ Removes old backups """
        backup_paths = []
        backup_dir = get_dir_path(Backup._BACKUP_DIR)

        for backup_path in scandir(backup_dir):
            if backup_path.is_file():
                continue
            backup_paths.append(backup_path.path)

        backup_paths.sort()
        while len(backup_paths) >= Backup._MAX_BACKUPS:
            removable_path = backup_paths.pop(0)
            rmtree(removable_path)

    def create_new_backup(self):
        """ Creates a new backup """
        # Target directory
        now = datetime.now()
        year = str(now.year)
        month = Backup._get_2_digit_number(now.month)
        day = Backup._get_2_digit_number(now.day)
        hrs = Backup._get_2_digit_number(now.hour)
        mins = Backup._get_2_digit_number(now.minute)
        secs = Backup._get_2_digit_number(now.second)
        subdir = f"{year}{month}{day}{hrs}{mins}{secs}"
        target_dir = get_dir_path(Backup._BACKUP_DIR)
        target_dir = path.join(target_dir, subdir)
        makedirs(target_dir)

        # Copy files
        data_dir = get_data_dir_path()

        for data_path in scandir(data_dir):
            if not data_path.is_file():
                continue
            target_path = path.join(target_dir, data_path.name)
            copyfile(data_path, target_path)

    @staticmethod
    def _get_2_digit_number(number) -> str:
        result = str(number)
        while len(result) < 2:
            result = f"0{result}"
        return result
