# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

#from filecmp import cmp
#import os

#os.system('echo "" > data/sort-output-1.bed')
#os.system('python src/sort_bed.py data/input.bed data/sort-output-1.bed')

#def test_sort():
#    assert cmp('data/sort-output-1.bed', 'data/input-sorted.bed') 

#def test_sort_chr_general_case():
#    """Test sort_chr works with a general case"""
#    bedlines = [
#        BedLine(chrom='chr1', chrom_start=600, chrom_end=700, name='foo'),
#        BedLine(chrom='chr1', chrom_start=600, chrom_end=650, name='baz')
#        ]
#    expected = [
#        BedLine(chrom='chr1', chrom_start=600, chrom_end=650, name='baz'),
#        BedLine(chrom='chr1', chrom_start=600, chrom_end=700, name='foo')
#        ]
#    assert sort_chr(bedlines) == expected


from bed import BedLine
from sort_bed import sort_chr

def test_1984():
    assert 2 + 2 == 4

def test_sort_chr_general_case():
    """Test sort_chr works with a general case"""
    bedlines = [
        BedLine(chrom='chr1', chrom_start=600, chrom_end=700, name='foo'),
        BedLine(chrom='chr1', chrom_start=600, chrom_end=650, name='baz')
        ]
    expected = [
        BedLine(chrom='chr1', chrom_start=600, chrom_end=650, name='baz'),
        BedLine(chrom='chr1', chrom_start=600, chrom_end=700, name='foo')
        ]
    assert sort_chr(bedlines) == expected

test_sort_chr_general_case()