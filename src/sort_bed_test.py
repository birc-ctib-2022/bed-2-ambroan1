# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from bed import BedLine
from sort_bed import sort_chr


os.system('python src/sort_bed.py data/input.bed data/sorted-output.bed' )

def test_sort_1():
    result = cmp('data/sorted-output.bed', 'data/input-sorted.bed') 
    assert result