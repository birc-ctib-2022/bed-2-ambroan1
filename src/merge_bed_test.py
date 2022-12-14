# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from filecmp import cmp
import os

os.system('python src/merge_bed.py data/input-sorted.bed data/input-sorted.bed -o data/merge-output-1.bed')

def test_merge_1():
    assert  cmp('data/merge-output-1.bed', 'data/input-merged.bed')
    