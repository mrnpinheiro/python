import pytest

from harmonic import (
    harmonic_maior,
    harmonic_menor
)


@pytest.fixture
def random_numbers():
    return [number for number in range(1, 6)]


def test_harmonic(random_numbers):
    result_harmonic_maior = harmonic_maior(random_numbers[-1])
    result_harmonic_menor = harmonic_menor(random_numbers[-1])
    expected_result_harmonic = sum([
        1 / number
        for number in random_numbers
    ])
    assert result_harmonic_maior == round(expected_result_harmonic, 2)
    assert result_harmonic_maior == result_harmonic_menor
