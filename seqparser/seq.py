# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    transcribed_seq = ''

    if reverse:
        return reverse_transcribe(seq)

    for nucleotide in seq:
        if nucleotide not in ALLOWED_NUC:
            raise ValueError(f"Invalid nucleotide in sequence: {nucleotide}")
        transcribed_seq += TRANSCRIPTION_MAPPING[nucleotide]

    return transcribed_seq
    pass

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    # Hey this is my comment
    # Again!
    return transcribe(seq[::-1])