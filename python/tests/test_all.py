import pytest
import imshrimp


def test_sum_as_string():
    assert imshrimp.sum_as_string(1, 1) == "2"
