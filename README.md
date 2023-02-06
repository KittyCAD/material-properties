# Material Properties Database

Here you can find properties for common materials used in mechanical design. This page is a work in progress :hammer:

<p align="center">
  <img src="https://media.giphy.com/media/4EFt4pA9U27Gau23IZ/giphy.gif" alt="machine gif" />
</p>

## Units Directory
When using our material library, reference the units directory below to know what units you are currently using.
*(All units are currently in English units, we will create an SI version in the future :gear:, or feel free to open a pr in the meantime :wink:)*

| Property              | JSON Key      | Units        |
| --------------------- | ------------- | ------------ |
| Density               | `den`         | lb/in^3      |
| Yield Strength        | `yield_str`   | psi          |
| Ultimate Strength     | `ult_str`     | psi          |
| Elongation            | `elongation`  | % (unitless) |
| Modulus of Elasticity | `moe`         | psi          |
| Poisson's Ratio       | `pr`          | % (unitless) |

### Code Example
Below is a Python example of how to use the library.

<p align="center">
  <img src="/images/python_example.png" alt="Python Example">
</p>

### Want to add more?
This library is open to all! If you want to add your own materials to the library, feel free to open a pull request and we will review
