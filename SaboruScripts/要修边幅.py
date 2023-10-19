# MenuTitle: 要修边幅
# Glyphs Version: 3.1.2 (3151)
# Python Version: 3
# Developer: DrayZ

def is_inside_boundary_box(node):
    x, y = node.x, node.y
    if a <= x <= b and c <= y <= d:
        return False
    else:
        return True

for i in Font.selectedLayers:
    indices_to_delete = []
    left, right = i.bounds.origin.x, i.bounds.origin.x + i.bounds.size.width
    top, bottom = i.bounds.origin.y + i.bounds.size.height, i.bounds.origin.y
    offset = 100
    a,b,c,d = left + offset, right - offset, bottom + offset, top - offset
    for shape in i.shapes:
        if all(is_inside_boundary_box(node) for node in shape.nodes):
            indices_to_delete.append(shape)
    for n in reversed(indices_to_delete):
        i.shapes.remove(n)

        