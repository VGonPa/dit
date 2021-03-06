"""
Tests for dit.multivariate.gk_common_information.
"""

from __future__ import division

from nose.tools import assert_almost_equal

from dit import Distribution
from dit.multivariate import gk_common_information as K

def test_K1():
    """ Test K for dependent events """
    outcomes = ['00', '11']
    pmf = [1/2, 1/2]
    d = Distribution(outcomes, pmf)
    assert_almost_equal(K(d), 1.0)
    assert_almost_equal(K(d, [[0], [1]]), 1.0)
    d.set_rv_names("XY")
    assert_almost_equal(K(d, [['X'], ['Y']]), 1.0)

def test_K2():
    """ Test conditional K for dependent events """
    outcomes = ['00', '11']
    pmf = [1/2, 1/2]
    d = Distribution(outcomes, pmf)
    assert_almost_equal(K(d, [[0], [1]], [0]), 0.0)
    assert_almost_equal(K(d, [[0], [1]], [1]), 0.0)
    d.set_rv_names("XY")
    assert_almost_equal(K(d, [['X'], ['Y']], ['X']), 0.0)
    assert_almost_equal(K(d, [['X'], ['Y']], ['Y']), 0.0)

def test_K3():
    """ Test K for mixed events """
    outcomes = ['00', '01', '11']
    pmf = [1/3, 1/3, 1/3]
    d = Distribution(outcomes, pmf)
    assert_almost_equal(K(d), 0.0)
    assert_almost_equal(K(d, [[0], [1]]), 0.0)
    d.set_rv_names("XY")
    assert_almost_equal(K(d, [['X'], ['Y']]), 0.0)

def test_K4():
    """ Test K in a canonical example """
    outcomes = ['00', '01', '10', '11', '22', '33']
    pmf = [1/8, 1/8, 1/8, 1/8, 1/4, 1/4]
    d = Distribution(outcomes, pmf)
    assert_almost_equal(K(d), 1.5)
    assert_almost_equal(K(d, [[0], [1]]), 1.5)
    d.set_rv_names("XY")
    assert_almost_equal(K(d, [['X'], ['Y']]), 1.5)

def test_K5():
    """ Test K on subvariables and conditionals """
    outcomes = ['000', '010', '100', '110', '221', '331']
    pmf = [1/8, 1/8, 1/8, 1/8, 1/4, 1/4]
    d = Distribution(outcomes, pmf)
    assert_almost_equal(K(d, [[0], [1]]), 1.5)
    assert_almost_equal(K(d), 1.0)
    assert_almost_equal(K(d, [[0], [1], [2]]), 1.0)
    d.set_rv_names("XYZ")
    assert_almost_equal(K(d, [['X'], ['Y']]), 1.5)
    assert_almost_equal(K(d, [['X'], ['Y'], ['Z']]), 1.0)
    assert_almost_equal(K(d, ['X', 'Y'], ['Z']), 0.5)
    assert_almost_equal(K(d, ['XY', 'YZ']), 2.0)
