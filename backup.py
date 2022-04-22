from datetime import datetime
from pathlib import Path
import zipfile

def backthisup(OBJECT_TO_BACKUP, BACKUP_DIRECTORY):
    MAX_BACKUP_AMOUNT = 5

    object_to_backup_path = Path(OBJECT_TO_BACKUP)
    backup_directory_path = Path(BACKUP_DIRECTORY)
    assert object_to_backup_path.exists()

    backup_directory_path.mkdir(parents=True, exist_ok=True)

    existing_backups = [
        x for x in backup_directory_path.iterdir()
        if x.is_file() and x.suffix == '.zip' and x.name.startswith('backup-')
    ]

    oldest_to_newest_backup_by_name = list(sorted(existing_backups, key=lambda f: f.name))
    while len(oldest_to_newest_backup_by_name) >= MAX_BACKUP_AMOUNT:
        backup_to_delete = oldest_to_newest_backup_by_name.pop(0)
        backup_to_delete.unlink()

    backup_file_name = f'backup-{datetime.now().strftime("%Y%m%d%H%M%S")}-{object_to_backup_path.name}.zip'
    zip_file = zipfile.ZipFile(str(backup_directory_path / backup_file_name), mode='w')
    if object_to_backup_path.is_file():
        zip_file.write(
            object_to_backup_path.absolute(),
            arcname=object_to_backup_path.name,
            compress_type=zipfile.ZIP_DEFLATED
        )
    elif object_to_backup_path.is_dir():
        for file in object_to_backup_path.glob('**/*'):
            if file.is_file():
                zip_file.write(
                    file.absolute(),
                    arcname=str(file.relative_to(object_to_backup_path)),
                    compress_type=zipfile.ZIP_DEFLATED
                )
    zip_file.close()