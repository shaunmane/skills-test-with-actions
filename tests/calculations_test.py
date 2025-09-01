# System Modules
import sys
import os
import pytest  # you'll need pytest for exception testing

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402


def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    radius = 1
    result = area_of_circle(radius)
    assert abs(result - 3.14159) < 1e-5


def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    radius = 0
    result = area_of_circle(radius)
    assert result == 0


def test_area_of_circle_negative_radius():
    """Test with a negative radius (should raise ValueError)."""
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        area_of_circle(-5)


def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    assert get_nth_fibonacci(0) == 0


def test_get_nth_fibonacci_one():
    """Test with n=1."""
    assert get_nth_fibonacci(1) == 1


def test_get_nth_fibonacci_two():
    """Test with n=2 (loop branch)."""
    assert get_nth_fibonacci(2) == 1


def test_get_nth_fibonacci_three():
    """Test with n=3 (loop branch)."""
    assert get_nth_fibonacci(3) == 2


def test_get_nth_fibonacci_ten():
    """Test with n=10."""
    assert get_nth_fibonacci(10) == 55


def test_get_nth_fibonacci_negative():
    """Test with negative n (should raise ValueError)."""
    with pytest.raises(ValueError, match="n cannot be negative"):
        get_nth_fibonacci(-1)


# Optional: Only add this if you extend the function to check types
# def test_get_nth_fibonacci_non_integer():
#     """Test with non-integer input."""
#     with pytest.raises(TypeError, match="n must be an integer"):
#         get_nth_fibonacci(3.5)
