import pytest
from pytest import fixture
from maxibon import KarumiHQs, ConsoleChat, Developer

from hypothesis import given, settings, Verbosity
from hypothesis import strategies as st

@fixture()
def office():
    return KarumiHQs(ConsoleChat())

@settings(verbosity=Verbosity.verbose)
def test_the_office_starts_with_10_maxibon(office):
    assert office.maxibon_left == 10
