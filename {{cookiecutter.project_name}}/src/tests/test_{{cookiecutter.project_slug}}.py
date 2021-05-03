#!/usr/bin/env python

# Example Tests

{% if cookiecutter.use_pytest == 'y' -%}

import pytest


def capital_case(x):
    return x.capitalize()


def test_capital_case():
    assert capital_case("semaphore") == "Semaphore"

{% else %}
# TO-DO
{%- endif %}