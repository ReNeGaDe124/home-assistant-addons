import pysubs2
from charset_normalizer import from_bytes

def validate_and_fix(content: bytes) -> str:
    text = from_bytes(content).best().output().decode("utf-8", errors="ignore")
    subs = pysubs2.SSAFile.from_string(text)
    return subs.to_string("srt")
