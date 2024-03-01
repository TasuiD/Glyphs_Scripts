# MenuTitle: 看看你的
# Glyphs Version: 3.1.2 (3151)
# Python Version: 3
# Developer: DrayZ
# 看宽度数据

import statistics

glyph_array = []
for l in Font.selectedLayers:
    glyph_array.append(l.width)


def calculate_statistics(arr):
    mean = statistics.mean(arr)
    mode = statistics.mode(arr)
    median = statistics.median(arr)
    return mean, mode, median

mean_value, mode_value, median_value = calculate_statistics(glyph_array)

print("Result:")
print(f"Mean: {mean_value}")
print(f"Mode: {mode_value}")
print(f"Median: {median_value}")
