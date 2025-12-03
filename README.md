# MyMath: A Comprehensive Python Math Package

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Table of Contents

- [About The Project](#about-the-project)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Operations](#basic-operations)
  - [Statistical Operations](#statistical-operations)
  - [Geometric Operations](#geometric-operations)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About The Project

`MyMath` is a versatile Python package designed to simplify common mathematical, statistical, and geometric calculations. Whether you're a student, a data analyst, or a developer, `MyMath` provides a straightforward and efficient way to perform essential computations without needing to implement them from scratch.

This package aims to offer a clean, well-documented, and easy-to-use API for everyday mathematical tasks, making your coding experience smoother and more productive.

## Features

`MyMath` is structured into three main modules, each dedicated to a specific area of mathematics:

- **Basic Operations (`mymath.basic`)**

  - `square(number)`: Returns the square of a given number.
  - `double(number)`: Returns twice the value of a given number.
  - `add(a, b)`: Returns the sum of two given numbers.

- **Statistical Operations (`mymath.stats`)**

  - `mean(numbers)`: Calculates the mean (average) of a list of numbers.
  - `median(numbers)`: Calculates the median of a list of numbers.

- **Geometric Operations (`mymath.geometry`)**
  - `area_of_rectangle(length, breadth)`: Calculates the area of a rectangle.
  - `area_of_circle(radius)`: Calculates the area of a circle.

## Installation

To install `MyMath`, you can clone the repository and install it manually, or if it were a published package, you would use pip.

```bash
git clone https://github.com/rafael-a-g-n/Create-Python-Package.git
cd Create-Python-Package
pip install .
```

Alternatively, you can just place the `mymath` directory into your Python project.

## Usage

Here are some examples of how to use the `MyMath` package:

### Basic Operations

```python
from mymath import basic

print(basic.square(5))    # Output: 25
print(basic.double(10))   # Output: 20
print(basic.add(7, 3))    # Output: 10
```

### Statistical Operations

```python
from mymath import stats

numbers = [1, 2, 3, 4, 5]
print(stats.mean(numbers))    # Output: 3.0
print(stats.median(numbers))  # Output: 3

numbers_even = [1, 2, 3, 4, 5, 6]
print(stats.median(numbers_even)) # Output: 3.5
```

### Geometric Operations

```python
from mymath import geometry

print(geometry.area_of_rectangle(4, 5)) # Output: 20
print(geometry.area_of_circle(3))      # Output: 28.274333882308138
```

## Technologies Used

- Python 3.x

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information. (Note: A `LICENSE` file does not currently exist in this project. It is good practice to include one.)

## Contact

Rafael Nogueira
Project Link: [https://github.com/rafael-a-g-n/Create-Python-Package](https://github.com/rafael-a-g-n/Create-Python-Package)
