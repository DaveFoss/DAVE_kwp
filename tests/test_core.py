import pandas as pd

from dave_kwp import compute
from dave_kwp import get_kwp


def test_compute():
    assert compute([b"a", b"bc", b"abc"]) == b"abc"


def test_kwp():
    pd.testing.assert_series_equal(
        get_kwp("building"), pd.Series([1, 2, 3, 4])
    )
