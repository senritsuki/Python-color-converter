# Python Color Converter
Color converter for Python 3.x. Supported formats: RGB, HSL, XYZ, L\*a\*b\*, L\*C\*h.

## Install

1. Install Python 3.x
2. Install numpy
3. Download color_converter.py

## How to use

```python
import color_converter as cc

cc.rgbhex_to_rgb255('#0080ff')
# -> [0, 128, 255]

cc.rgb255_to_rgbhex((0, 128, 255))
# -> '#0080ff'
```

## Functions

|Function name|Argument value|Return value|
|-|-|-|
|hsl_to_rgb01|HSL array<br/>(0.0, 0.0, 0.0) .. (360.0, 1.0, 1.0)|RGB array<br/>(0.0, 0.0, 0.0) .. (1.0, 1.0, 1.0)|
|hsl_to_rgb255|HSL array<br/>(0.0, 0.0, 0.0) .. (360.0, 1.0, 1.0)|RGB array<br/>(0, 0, 0) .. (255, 255, 255)|
|hsl_to_rgbhex|HSL array<br/>(0.0, 0.0, 0.0) .. (360.0, 1.0, 1.0)|RGB string<br/>'#000000' .. '#ffffff'|
|lab_to_lch|D50 CIE L\*a\*b\* array<br/>(0.0, \*.\*, \*.\*) .. (100.0, \*.\*, \*.\*)|D50 CIE L\*C\*h array<br/>(0.0, 0.0, 0.0) .. (100.0, \*.\*, 360.0)|
|lab_to_rgb01|D50 CIE L\*a\*b\* array<br/>(0.0, \*.\*, \*.\*) .. (100.0, \*.\*, \*.\*)|RGB array<br/>(0.0, 0.0, 0.0) .. (1.0, 1.0, 1.0)|
|lab_to_rgb255|D50 CIE L\*a\*b\* array<br/>(0.0, \*.\*, \*.\*) .. (100.0, \*.\*, \*.\*)|RGB array<br/>(0, 0, 0) .. (255, 255, 255)|
|lab_to_rgbhex|D50 CIE L\*a\*b\* array<br/>(0.0, \*.\*, \*.\*) .. (100.0, \*.\*, \*.\*)|RGB string<br/>'#000000' .. '#ffffff'|
|lab_to_xyz|D50 CIE L\*a\*b\* array<br/>(0.0, \*.\*, \*.\*) .. (100.0, \*.\*, \*.\*)|D50 CIE XYZ array<br/>(\*.\*, \*.\*, \*.\*) .. (\*.\*, \*.\*, \*.\*)|
|lch_to_lab|D50 CIE L\*C\*h array<br/>(0.0, 0.0, 0.0) .. (100.0, \*.\*, 360.0)|D50 CIE L\*a\*b\* array<br/>(0.0, \*.\*, \*.\*) .. (100.0, \*.\*, \*.\*)|
|lch_to_rgb255|D50 CIE L\*C\*h array<br/>(0.0, 0.0, 0.0) .. (100.0, \*.\*, 360.0)|RGB array<br/>(0, 0, 0) .. (255, 255, 255)|
|lch_to_rgbhex|D50 CIE L\*C\*h array<br/>(0.0, 0.0, 0.0) .. (100.0, \*.\*, 360.0)|RGB string<br/>'#000000' .. '#ffffff'|
|lrgb_to_srgb|D65 linear sRGB array<br/>(0.0, 0.0, 0.0) .. (1.0, 1.0, 1.0)|D65 non linear sRGB array<br/>(0.0, 0.0, 0.0) .. (1.0, 1.0, 1.0)|
|lrgb_to_xyz|D65 linear sRGB array<br/>(0.0, 0.0, 0.0) .. (1.0, 1.0, 1.0)|D50 CIE XYZ array<br/>(\*.\*, \*.\*, \*.\*) .. (\*.\*, \*.\*, \*.\*)|
|rgb01_to_hsl|RGB array<br/>(0.0, 0.0, 0.0) .. (1.0, 1.0, 1.0)|HSL array<br/>(0.0, 0.0, 0.0) .. (360.0, 1.0, 1.0)|
|rgb01_to_lab|RGB array<br/>(0.0, 0.0, 0.0) .. (1.0, 1.0, 1.0)|D50 CIE L\*a\*b\* array<br/>(0.0, \*.\*, \*.\*) .. (100.0, \*.\*, \*.\*)|
|rgb01_to_rgb255|RGB array<br/>(0.0, 0.0, 0.0) .. (1.0, 1.0, 1.0)|RGB array<br/>(0, 0, 0) .. (255, 255, 255)|
|rgb01_to_rgbhex|RGB array<br/>(0.0, 0.0, 0.0) .. (1.0, 1.0, 1.0)|RGB string<br/>'#000000' .. '#ffffff'|
|rgb255_to_hsl|RGB array<br/>(0, 0, 0) .. (255, 255, 255)|HSL array<br/>(0.0, 0.0, 0.0) .. (360.0, 1.0, 1.0)|
|rgb255_to_lab|RGB array<br/>(0, 0, 0) .. (255, 255, 255)|D50 CIE L\*a\*b\* array<br/>(0.0, \*.\*, \*.\*) .. (100.0, \*.\*, \*.\*)|
|rgb255_to_lch|RGB array<br/>(0, 0, 0) .. (255, 255, 255)|D50 CIE L\*C\*h array<br/>(0.0, 0.0, 0.0) .. (100.0, \*.\*, 360.0)|
|rgb255_to_rgb01|RGB array<br/>(0, 0, 0) .. (255, 255, 255)|RGB array<br/>(0.0, 0.0, 0.0) .. (1.0, 1.0, 1.0)|
|rgb255_to_rgbhex|RGB array<br/>(0, 0, 0) .. (255, 255, 255)|RGB string<br/>'#000000' .. '#ffffff'|
|rgbhex_to_hsl|RGB string<br/>'#000000' .. '#ffffff'|HSL array<br/>(0.0, 0.0, 0.0) .. (360.0, 1.0, 1.0)|
|rgbhex_to_lab|RGB string<br/>'#000000' .. '#ffffff'|D50 CIE L\*a\*b\* array<br/>(0.0, \*.\*, \*.\*) .. (100.0, \*.\*, \*.\*)|
|rgbhex_to_lch|RGB string<br/>'#000000' .. '#ffffff'|D50 CIE L\*C\*h array<br/>(0.0, 0.0, 0.0) .. (100.0, \*.\*, 360.0)|
|rgbhex_to_rgb01|RGB string<br/>'#000000' .. '#ffffff'|RGB array<br/>(0.0, 0.0, 0.0) .. (1.0, 1.0, 1.0)|
|rgbhex_to_rgb255|RGB string<br/>'#000000' .. '#ffffff'|RGB array<br/>(0, 0, 0) .. (255, 255, 255)|
|srgb_to_lrgb|D65 non linear sRGB array<br/>(0.0, 0.0, 0.0) .. (1.0, 1.0, 1.0)|D65 linear sRGB array<br/>(0.0, 0.0, 0.0) .. (1.0, 1.0, 1.0)|
|xyz_to_lab|D50 CIE XYZ array<br/>(\*.\*, \*.\*, \*.\*) .. (\*.\*, \*.\*, \*.\*)|D50 CIE L\*a\*b\* array<br/>(0.0, \*.\*, \*.\*) .. (100.0, \*.\*, \*.\*)|
|xyz_to_lrgb|D50 CIE XYZ array<br/>(\*.\*, \*.\*, \*.\*) .. (\*.\*, \*.\*, \*.\*)|D65 linear sRGB array<br/>(0.0, 0.0, 0.0) .. (1.0, 1.0, 1.0)|
