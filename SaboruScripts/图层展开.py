# MenuTitle: ShowAllLayers
# Glyphs Version: 3.1.2 (3151)
# Python Version: 3
# Developer: DrayZ

for currentlayer in Font.selectedLayers:
	Layers = []
	current_glyph = currentlayer.parent
	for layer in current_glyph.layers:
		Layers.append(layer)
		if len(Layers) == 10:
			Layers.append(GSControlLayer(10))
	NewTab = Font.newTab("/"+current_glyph.name)
	NewTab.layers = Layers

