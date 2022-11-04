# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from filecmp import cmp
import os

os.system('echo "" > data/test-query-1.bed') 
os.system('python src/query_bed.py data/large-sorted.bed data/query-1.txt -o data/output-query-1.bed')

def test_query_bed_1():
    result = cmp('data/output-query-1.bed', 'data/expected-1.txt') 
    assert result
