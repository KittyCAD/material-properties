<div>
  <img src="/images/header.svg" style="width: 100%;" alt="Click to see the source">
</div>

<p align="center">Here you can find properties for common materials used in mechanical design. This page is a work in progress :hammer:</p>

<p align="center">
  <img src="https://media.giphy.com/media/4EFt4pA9U27Gau23IZ/giphy.gif" alt="machine gif" />
</p>

## 🛠️ Units Directory 🛠️
When using our material library, reference the units directory below to know what units you are currently using.
*(All units are currently in English units, we will create an SI version in the future :gear:, or feel free to open a pr in the meantime :wink:)*

<table align="center" style="text-align: center">
  <tr>
    <th>Property</th>
    <th>JSON Key</th>
    <th>Units</th>
  </tr>
  <tr>
    <td>Density</td>
    <td>den</td>
    <td>lb/in^3</td>
  </tr>
  <tr>
    <td>Yield Strength</td>
    <td>yield_str</td>
    <td>psi</td>
  </tr>
  <tr>
    <td>Ultimate Strength</td>
    <td>ult_str</td>
    <td>psi</td>
  </tr>
  <tr>
    <td>Elongation</td>
    <td>elongation</td>
    <td>% (unitless)</td>
  </tr>
  <tr>
    <td>Modulus of Elasticity</td>
    <td>moe</td>
    <td>psi</td>
  </tr>
  <tr>
    <td>Poisson's Ratio</td>
    <td>pr</td>
    <td>% (unitless)</td>
  </tr>
  <tr>
    <td>Maximum Service Temperature</td>
    <td>max_service_temp</td>
    <td>&degF</td>
  </tr>
  <tr>
    <td>Coefficient of Thermal Expansion</td>
    <td>coef_thermal_exp</td>
    <td>&#956in/in</td>
  </tr>
  <tr>
    <td>Minimum Extruder Temperature</td>
    <td>min_extrude_temp</td>
    <td>&degF</td>
  </tr>
  <tr>
    <td>Maximum Extruder Temperature</td>
    <td>max_extrude_temp</td>
    <td>&degF</td>
  </tr>
  <tr>
    <td>Minimum Bed Temperature</td>
    <td>min_bed_temp</td>
    <td>&degF</td>
  </tr>
  <tr>
    <td>Maximum Bed Temperature</td>
    <td>max_bed_temp</td>
    <td>&degF</td>
  </tr>
</table>

### 🛠️ Code Example 🛠️
Below is a Python example of how to use the library.

```
import json

with open('material-properties/carbonsteel.json') as aluminum_properties:
    aluminum = json.load(aluminum_properties)

AISI_1020_den = aluminum['AISI_1020']['hot']['den']
```

### 👷 Honorary Engineers (Contributors) 👷

A huge thank you to all our contributing engineers! <br><br> 
<a href="https://github.com/kittyCAD/material-properties/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=kittyCAD/material-properties" />
</a>

### 👷 How to Contribute 👷

If you would like to make a change, open up a PR and we will review promptly. If you would like to add or edit a value within the database, please provide a reference with your requested change. 

#### References
[1]: Beer, F. P., Johnston, E. R., DeWolf, J. T., & Mazurek, D. F. (2012). Mechanics of Materials (Sixth). MaGraw-Hill. <br>
[2] Filament Properties Table. Simplify3D. (n.d.). Retrieved February 24, 2023, from https://www.simplify3d.com/resources/materials-guide/properties-table/ 