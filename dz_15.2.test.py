import pytest
from dz_14.py import Tree

@pytest.fixture
def tree():
    return Tree([4, 7, 3, 5, 6, 8, 9])

def test_insert(tree):
    tree.insert(2)
    assert tree.left.left.value == 2

def test_min(tree):
    assert tree.min() == 3

def test_max(tree):
    assert tree.max() == 9

def test_delete(tree):
    tree.delete(4)
    assert tree.value == 5



