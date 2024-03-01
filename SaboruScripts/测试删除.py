# MenuTitle: 测试删除
# Glyphs Version: 3.1.2 (3151)
# Python Version: 3
# Developer: Georg Seifert


from CoreText import CTFontManagerCopyAvailableFontURLs, CTFontManagerUnregisterFontsForURL, kCTFontManagerScopeSession
tempPath = GSGlyphsInfo.applicationSupportPath()
for url in CTFontManagerCopyAvailableFontURLs():
	if url.path().hasPrefix_(tempPath):
		print(url)
		CTFontManagerUnregisterFontsForURL(url, kCTFontManagerScopeSession, None)