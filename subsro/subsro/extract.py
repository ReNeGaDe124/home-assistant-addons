import os
import zipfile
import rarfile
import py7zr
import tempfile
import shutil

def extract_srt(archive_bytes, target_srt_path):
    tmp_dir = tempfile.mkdtemp()

    archive_path = os.path.join(tmp_dir, "sub")
    with open(archive_path, "wb") as f:
        f.write(archive_bytes)

    extracted = False

    try:
        if zipfile.is_zipfile(archive_path):
            with zipfile.ZipFile(archive_path) as z:
                z.extractall(tmp_dir)

        elif rarfile.is_rarfile(archive_path):
            with rarfile.RarFile(archive_path) as r:
                r.extractall(tmp_dir)

        else:
            with py7zr.SevenZipFile(archive_path, mode="r") as z:
                z.extractall(tmp_dir)

        for root, _, files in os.walk(tmp_dir):
            for file in files:
                if file.lower().endswith(".srt"):
                    shutil.move(
                        os.path.join(root, file),
                        target_srt_path
                    )
                    extracted = True
                    break
    finally:
        shutil.rmtree(tmp_dir)

    return extracted
