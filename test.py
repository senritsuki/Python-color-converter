
import color_converter as cc

print("cc.rgbhex_to_rgb255('#0080ff')")
print(cc.rgbhex_to_rgb255('#0080ff'))

print("cc.rgb255_to_rgbhex((0, 128, 255))")
print(cc.rgb255_to_rgbhex((0, 128, 255)))

print("cc.lab_to_lch((80, 10, 17.32))")
print(cc.lab_to_lch((80, 10, 17.32)))

print("cc.lch_to_lab((80, 20, 60))")
print(cc.lch_to_lab((80, 20, 60)))

print("cc.hsl_to_rgbhex((210, 0.4, 0.7))")
print(cc.hsl_to_rgbhex((210, 0.4, 0.7)))

print("cc.lch_to_rgbhex((70, 40, 210))")
print(cc.lch_to_rgbhex((70, 40, 210)))

# test with Adobe Photoshop CS6

print("cc.lab_to_rgb255((0, 0, 0)) -> [0, 0, 0]")
print(cc.lab_to_rgb255((0, 0, 0)))

print("cc.lab_to_rgb255((50, 0, 0)) -> [119, 119, 119]")
print(cc.lab_to_rgb255((50, 0, 0)))

print("cc.lab_to_rgb255((100, 0, 0)) -> [255, 255, 255]")
print(cc.lab_to_rgb255((100, 0, 0)))

print("cc.lab_to_rgb255((50, 50, 0)) -> [193, 78, 121]")
print(cc.lab_to_rgb255((50, 50, 0)))

print("cc.lab_to_rgb255((50, 0, 50)) -> [136, 118, 22]")
print(cc.lab_to_rgb255((50, 0, 50)))

print("cc.lab_to_rgb255((50, -50, 0)) -> [0, 140, 117]")
print(cc.lab_to_rgb255((50, -50, 0)))

print("cc.lab_to_rgb255((50, 0, -50)) -> [54, 122, 205]")
print(cc.lab_to_rgb255((50, 0, -50)))

