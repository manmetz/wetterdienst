import pandas as pd
from pandas._testing import assert_series_equal

from wetterdienst.core.scalar.values import ScalarValuesCore


def test_coerce_strings():

    series = ScalarValuesCore._coerce_strings(pd.Series(["foobar"]))
    series_expected = pd.Series(["foobar"], dtype=pd.StringDtype())

    assert_series_equal(series, series_expected)


def test_coerce_integers():

    series = ScalarValuesCore._coerce_integers(pd.Series([42]))
    series_expected = pd.Series([42], dtype=pd.Int64Dtype())

    assert_series_equal(series, series_expected)


def test_coerce_floats():

    series = ScalarValuesCore._coerce_floats(pd.Series([42.42]))
    # TODO: Why doesn't this match `pd.Float64Dtype()`?
    series_expected = pd.Series([42.42], dtype="float64")

    assert_series_equal(series, series_expected)