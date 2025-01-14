# write tests for transcribe functions
# # the lines below are what's needed to test locally-- probably not needed with github actions so will comment out
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from seqparser import (
        transcribe,
        reverse_transcribe)
import pytest

def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    seq_input = 'TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA'
    seq_output = 'ACUAACUUAGAAAACUCCCAGUGCCGGGCCUUCGGUCUUAAAGCCCCAGGAGACACCUAUAAUUAGCUCGGGUGUGCCACACUCAAGUCGCCGGGGGCGU'
    assert transcribe(seq_input) == seq_output

    with pytest.raises(ValueError):
        transcribe('TGATXT') # testing if ValueError is raised if non-nucleotide in sequence

    pass


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    seq_input = 'TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA'
    seq_output = 'UGCGGGGGCCGCUGAACUCACACCGUGUGGGCUCGAUUAAUAUCCACAGAGGACCCCGAAAUUCUGGCUUCCGGGCCGUGACCCUCAAAAGAUUCAAUCA'

    assert reverse_transcribe(seq_input) == seq_output

    with pytest.raises(ValueError):
        reverse_transcribe('TGATXT') # testing if ValueError is raised if non-nucleotide in sequence

    pass