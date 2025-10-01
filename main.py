import numpy as np
import matplotlib.pyplot as plt

def plot() -> None:
    """Create and display a 3D surface plot."""
    # create a 2D grid of points
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    # make a 3d plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    plt.show()

# example functions with type annotations and numpydoc-style docstrings
def add(a: int, b: int) -> int:
    """Add two integers and return the result.
    Args:
        a (int): The first integer.
        b (int): The second integer.
    Returns:
        int: The sum of the two integers.
    """
    return a + b

class Calculator:
    """A simple calculator class."""

    def multiply(self, a: int, b: int) -> int:
        """Multiply two integers and return the result.
        Args:
            a (int): The first integer.
            b (int): The second integer.
        Returns:
            int: The product of the two integers.
        """
        return a * b


if __name__ == "__main__":
    # simple usage examples
    the_sum = add(3, 5)
    print(f"3 + 5 = {the_sum}")
    
    # create an instance of Calculator and use it
    calc = Calculator()
    the_product = calc.multiply(4, 6)
    print(f"4 * 6 = {the_product}")
    
    plot()
