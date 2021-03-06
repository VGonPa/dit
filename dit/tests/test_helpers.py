"""
Tests for dit.helpers.
"""

from __future__ import division

from nose.tools import assert_equal, assert_raises

from dit import Distribution
from dit.exceptions import ditException, InvalidDistribution, InvalidOutcome
from dit.helpers import construct_alphabets, get_product_func, parse_rvs, \
                        reorder

def test_construct_alphabets1():
    outcomes = ['00', '01', '10', '11']
    alphas = construct_alphabets(outcomes)
    assert_equal(alphas, (('0', '1'), ('0', '1')))

def test_construct_alphabets2():
    outcomes = 3
    assert_raises(TypeError, construct_alphabets, outcomes)

def test_construct_alphabets3():
    outcomes = [0, 1, 2]
    assert_raises(ditException, construct_alphabets, outcomes)

def test_construct_alphabets4():
    outcomes = ['0', '1', '01']
    assert_raises(ditException, construct_alphabets, outcomes)

def test_parse_rvs1():
    outcomes = ['00', '11']
    pmf = [1/2]*2
    d = Distribution(outcomes, pmf)
    assert_raises(ditException, parse_rvs, d, [0, 0, 1])

def test_parse_rvs2():
    outcomes = ['00', '11']
    pmf = [1/2]*2
    d = Distribution(outcomes, pmf)
    d.set_rv_names('XY')
    assert_raises(ditException, parse_rvs, d, ['X', 'Y', 'Z'])

def test_parse_rvs3():
    outcomes = ['00', '11']
    pmf = [1/2]*2
    d = Distribution(outcomes, pmf)
    assert_raises(ditException, parse_rvs, d, [0, 1, 2])

def test_reorder1():
    outcomes = ['00', '11', '01']
    pmf = [1/3]*3
    sample_space = ('00', '01', '10', '11')
    new = reorder(outcomes, pmf, sample_space)
    assert_equal(new[0], ['00', '01', '11'])

def test_reorder2():
    outcomes = ['00', '11', '22']
    pmf = [1/3]*3
    sample_space = ('00', '01', '10', '11')
    assert_raises(InvalidOutcome, reorder, outcomes, pmf, sample_space)
