# MenuTitle: 永结同心
# Glyphs Version: 3.1.2 (3151)
# Python Version: 3
# Developer: DrayZ
# 计算字符的平均几何中心

SumCx = 0
SumCy = 0
count = 0

for layer in Font.selectedLayers:
	Ox,Oy = layer.bounds.origin.x, layer.bounds.origin.y
	Ow,Oh = layer.bounds.size.width, layer.bounds.size.height
	Cx,Cy = Ox + 0.5*Ow, Oy + 0.5*Oh
	SumCx += Cx
	SumCy += Cy
	count += 1

AvrCx = SumCx/count
AvrCy = SumCy/count
print(AvrCx,AvrCy)