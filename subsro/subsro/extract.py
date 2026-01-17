import os
import tempfile
import shutil
import subprocess
import re
import charset_normalizer

def ensure_utf8(file_path):
    try:
        with open(file_path, "rb") as f:
            chunk = f.read(4096)

        if not chunk:
            return 'error'

        if chunk.startswith(b'\xef\xbb\xbf'):
            return 'already_utf8'

        try:
            chunk.decode("utf-8")
            return 'already_utf8'
        except UnicodeDecodeError as e:
            if e.start >= len(chunk) - 4:
                return 'already_utf8'
            
            pass
        
        with open(file_path, "rb") as f:
            full_data = f.read()

        results = charset_normalizer.from_bytes(full_data)
        best_match = results.best()
        
        if not best_match:
            return 'error'
            
        content = str(best_match)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
            
        return 'converted'

    except Exception:
        return 'error'


def extract_srt(archive_bytes, target_path):
    filename = os.path.basename(target_path).upper()
    v_match = re.search(r'S(\d+).*E(\d+)|(\d+)X(\d+)', filename)
    is_episode = bool(v_match)
    
    with tempfile.TemporaryDirectory() as tmp_dir:
        archive_path = os.path.join(tmp_dir, "subs.rar")
        with open(archive_path, "wb") as f:
            f.write(archive_bytes)
        
        try:
            subprocess.run(["7z", "x", archive_path, f"-o{tmp_dir}", "-y"], check=True, capture_output=True)
            
            all_srt_files = []
            for root, _, files in os.walk(tmp_dir):
                if "__MACOSX" in root: continue
                for file in files:
                    if file.lower().endswith(".srt"):
                        all_srt_files.append(os.path.join(root, file))
            
            if not all_srt_files: return False

            chosen_srt = None
            if is_episode:
                target_s = int(v_match.group(1) or v_match.group(3))
                target_e = int(v_match.group(2) or v_match.group(4))
                for srt_path in all_srt_files:
                    srt_name = os.path.basename(srt_path).upper()
                    s_match = re.search(r'S(\d+).*E(\d+)|(\d+)X(\d+)', srt_name)
                    if s_match:
                        found_s = int(s_match.group(1) or s_match.group(3))
                        found_e = int(s_match.group(2) or s_match.group(4))
                        if found_s == target_s and found_e == target_e:
                            chosen_srt = srt_path
                            break
            else:
                all_srt_files.sort(key=lambda x: os.path.getsize(x), reverse=True)
                chosen_srt = all_srt_files[0]

            if chosen_srt:
                ensure_utf8(chosen_srt)
                shutil.move(chosen_srt, target_path)
                return True
            
            return False

        except Exception:
            return False