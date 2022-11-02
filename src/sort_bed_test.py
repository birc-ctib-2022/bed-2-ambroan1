# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from filecmp import cmp
import os

os.system('echo "" > data/sort-output-1.bed')
os.system('python src/sort_bed.py data/input.bed data/sort-output-1.bed')

def test_sort():
    assert cmp('data/sort-output-1.bed', 'data/input-sorted.bed') 
