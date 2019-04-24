import logging
import os
import shutil
from pathlib import Path


def file_backup_same_dir(src_file_path: [Path, str], max_backups: int = 5):
    src_file_path = Path(src_file_path)
    backup_paths = [Path(src_file_path.with_suffix(f'.bak{idx}')) for idx in range(max_backups)]
    for file in backup_paths:
        if not file.exists():
            logging.debug("Copying file from %s to %s", src_file_path, file)
            shutil.copy(src_file_path, file)
            return
    backup_paths.sort(key=lambda x: os.lstat(x).st_ctime)
    dest_path = backup_paths[0]
    logging.debug("Removing backup file: %s", dest_path)
    os.remove(dest_path)
    logging.debug("Copying file from %s to %s", src_file_path, dest_path)
    shutil.copy(src_file_path, dest_path)


if __name__ == '__main__':
    file_backup_same_dir(Path(r"M:\Python\Projects\CharacterSheet\utils\file_operation.py"))
