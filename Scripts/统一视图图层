# MenuTitle: Show Glyphs in Current Layer
# Glyphs Version: 3.1.2 (3151)
# Python Version: 3
# Developer: DrayZ


def extract_string(input_string):
    result = []
    i = 0
    while i < len(input_string):
        if input_string[i:i+2] == '//':
            # 规则3：提取两个/
            result.append('/')
            i += 2
        elif input_string[i] == '/':
            # 规则2：提取/和/之后的字符（包括/）
            j = i + 1
            while j < len(input_string) and (input_string[j] != ' ' or input_string[j-1] == '/'):
                j += 1
            result.append(input_string[i:j])
            i = j
        else:
            # 规则1：提取单个字符
            result.append(input_string[i])
            i += 1
    return result

for layer in Font.selectedLayers:
    current_layer_name = layer.name
    glyph = layer.parent

layers = []
text = Font.currentTab.text

# 测试示例
result = extract_string(text)
print(result)

Layers = []
for i in result:
    if len(i) > 1 and i[0] == "/":
        for g in Font.glyphs:
            if g.name == i[1:]:
                for l in g.layers:
                    if l.name == current_layer_name:
                        Layers.append(l)
    else:
        uni=hex(ord(i))
        if len(uni)==4:
            uni_new=uni.replace("0x","00")
        else:
            uni_new=uni.replace("0x","")
        UNI_new=uni_new.swapcase()
        for g in Font.glyphs:
            if g.unicode == UNI_new:
                for l in g.layers:
                    if l.name == current_layer_name:
                        Layers.append(l)
print(Layers)
Font.currentTab.layers = Layers
