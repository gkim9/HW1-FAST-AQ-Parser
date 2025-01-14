# write tests for parsers
# '''
# I had to look up how to make the seqparser module load when I test this locally.
# (It seems like I'm using python 3.12 whereas it was intended to be written in python 3.9?)
# It probably doesn't matter for github actions
# '''
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """

    '''
    iterating over FastaParser(filename) should give (seq#, DNA_sequence) for all the sequences in the fasta file
    -> 
    '''

    test_fasta = FastaParser('data/test.fa')
    assert test_fasta.filename == "data/test.fa", "Incorrect file name"

    seqs = [seq for seq in test_fasta]
    first_line = seqs[0]

    assert type(first_line) == tuple, "Incorrect data type after fasta file parsed"

    assert first_line == ('seq0', 'TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA'), "test failed"

    # When running the bad/blank fasta file, ValueError must be raised in order for the FastaParser to be working correctly
    with pytest.raises(ValueError):
        next(iter(FastaParser('tests/bad.fa')))

    with pytest.raises(ValueError):
        next(iter(FastaParser('tests/blank.fa')))

    pass


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    assert None not in next(iter(FastaParser('data/test.fa')), None), "Seems like a fastq file"

    pass


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    seqs = [seq for seq in FastqParser('data/test.fq')]
    assert len(seqs[0]) == 3
    assert type(seqs[0]) == tuple
    pass

seq = [seq for seq in FastqParser('data/test.fq')]
print(seq)
print("\n")
print(test_FastqParser())

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    assert None not in next(iter(FastqParser('data/test.fq')), None), "Seems like a fasta file"

    pass