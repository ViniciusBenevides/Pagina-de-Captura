import os

source_file = r'c:\Users\vsben_332kka0\Desktop\Projects\portfolio-vinicius\src\components\WorldMap.astro'
dest_file = r'c:\Users\vsben_332kka0\Desktop\Projects\portfolio-vinicius\src\components\worldmap.svg'

with open(source_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Filter out the div wrapper from the start and end
svg_lines = []
for i, line in enumerate(lines):
    if i == 0 and '<div class="worldmap">' in line:
        continue
    if i == len(lines)-1 and '</div>' in line:
        continue
    svg_lines.append(line)

with open(dest_file, 'w', encoding='utf-8') as f:
    f.writelines(svg_lines)

print("SVG extracted successfully.")
