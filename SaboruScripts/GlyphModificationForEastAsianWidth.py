#MenuTitle: GlyphModificationForEastAsianWidth
# Glyphs Version: 3.1.2 (3151)
# Python Version: 3
# Developer: DrayZ
# Some code from The mekkablue Glyphs-Scripts Project: https://github.com/mekkablue/Glyphs-Scripts
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals

import vanilla
import GlyphsApp
import math
from AppKit import NSAffineTransform, NSAffineTransformStruct

class ModifyGlyphManager(object):
    def __init__(self):
        # Create a vanilla window
        self.w = vanilla.FloatingWindow(
            (290, 256), "Glyph Modification", minSize=(290, 256), maxSize=(290, 256)
        )

        linePos, inset, lineHeight = 12, 15, 22

        # Checkbox to include all glyphs
        self.w.includeAllGlyphs = vanilla.CheckBox(
            (inset, linePos - 1, -inset, 24),
            "⚠️ Apply to ALL glyphs, ignore glyph selection",
            sizeStyle="small",
            value=False,
        )        
        linePos += lineHeight + 10

        self.w.AutomaticAlignmentText = vanilla.TextBox(
            (inset, linePos - 1, -inset, 20),
            "⬇️ Automatic alignment:",
            sizeStyle="regular",
            selectable=True,
        )
        linePos += lineHeight

        # Button to disable alignment
        self.w.disableAlignmentButton = vanilla.Button(
            (inset, linePos - 1, 80, 20),
            "🚫 Disable",
            sizeStyle="regular",
            callback=self.disableAlignment,
        )

        # Button to enable alignment
        self.w.enableAlignmentButton = vanilla.Button(
            (inset + 100, linePos - 1, 80, 20),
            "✅ Enable",
            sizeStyle="regular",
            callback=self.enableAlignment,
        )
        linePos += lineHeight + 20

        self.w.ModifyWidthText = vanilla.TextBox(
            (inset, linePos - 1, -inset, 20),
            "⬇️ Modify Glyph Width:",
            sizeStyle="regular",
            selectable=True,
        )
        linePos += lineHeight

        # Radio buttons for width options
        self.w.widthOptions = vanilla.RadioGroup(
            (inset, linePos-1, 180, 24),
            ["500", "1000", "Custom"],
            callback=self.widthOptionSelected,
            sizeStyle="small",
            isVertical=False,
        )
        self.w.widthOptions.set(0)  # Default to 500

        # Input field for custom width
        self.w.customWidthInput = vanilla.EditText(
            (inset + 200, linePos, -inset, 22),
            "",
            placeholder="",
            callback=self.customWidthEntered,
        )
        self.w.customWidthInput.enable(False)  # Disable initially
        linePos += lineHeight+5

        # Button to modify width
        self.w.modifyWidthButton = vanilla.Button(
            (inset, linePos - 1, 80, 20),
            "🏃 Run",
            sizeStyle="regular",
            callback=self.modifyGlyphWidth,
        )

        linePos += lineHeight + 20

        self.w.centerGlyphsText = vanilla.TextBox(
            (inset, linePos - 1, -inset, 20),
            "⬇️ Center Glyphs:",
            sizeStyle="regular",
            selectable=True,
        )
        linePos += lineHeight

        # Button to center glyphs
        self.w.centerGlyphsButton = vanilla.Button(
            (inset, linePos - 1, 80, 20),
            "🎯Center",
            sizeStyle="regular",
            callback=self.centerGlyphs,
        )

        # Open the window
        self.w.open()

    def widthOptionSelected(self, sender):
        # Enable or disable the custom width input field based on the selected radio button
        custom_width_enabled = sender.get() == 2  # Custom option selected
        self.w.customWidthInput.enable(custom_width_enabled)

    def customWidthEntered(self, sender):
        # You can add validation or processing here if needed
        pass

    def modifyGlyphWidth(self, sender):
        try:
            thisFont = Glyphs.font

            # Get the selected width based on the radio button
            selected_width_option = self.w.widthOptions.get()
            if selected_width_option == 0:
                new_width = 500
            elif selected_width_option == 1:
                new_width = 1000
            else:
                # Custom width input
                custom_width_str = self.w.customWidthInput.get()
                new_width = float(custom_width_str) if custom_width_str else None

            if new_width is None:
                print("Invalid width input. Please enter a valid number.")
                return

            # Get the selected glyphs or all glyphs if includeAllGlyphs is checked
            if self.w.includeAllGlyphs.get():
                selectedGlyphs = thisFont.glyphs
            else:
                selectedGlyphs = [l.parent for l in thisFont.selectedLayers]

            # Loop through selected glyphs and set the width
            for thisGlyph in selectedGlyphs:
                for thisLayer in thisGlyph.layers:
                    if thisLayer.isMasterLayer or thisLayer.isSpecialLayer:
                        thisLayer.width = new_width
                        print(f"Modified width of {thisGlyph.name} to {new_width}")

        except Exception as e:
            # Display error message in Glyphs macro window
            Glyphs.showMacroWindow()
            print(f"Modify Width Error: {e}")

    def disableAlignment(self, sender):
        try:
            thisFont = Glyphs.font

            # Get the selected glyphs or all glyphs if includeAllGlyphs is checked
            if self.w.includeAllGlyphs.get():
                selectedGlyphs = thisFont.glyphs
            else:
                selectedGlyphs = [l.parent for l in thisFont.selectedLayers]

            # Loop through selected glyphs and layers to disable alignment
            for thisGlyph in selectedGlyphs:
                for thisLayer in thisGlyph.layers:
                    if thisLayer.isMasterLayer or thisLayer.isSpecialLayer:
                        for thisComponent in thisLayer.components:
                            thisComponent.setDisableAlignment_(True)
                        print(f"Disabled alignment in {thisGlyph.name} - {thisLayer.name}")

        except Exception as e:
            # Display error message in Glyphs macro window
            Glyphs.showMacroWindow()
            print(f"Disable Alignment Error: {e}")

    def enableAlignment(self, sender):
        try:
            thisFont = Glyphs.font

            # Get the selected glyphs or all glyphs if includeAllGlyphs is checked
            if self.w.includeAllGlyphs.get():
                selectedGlyphs = thisFont.glyphs
            else:
                selectedGlyphs = [l.parent for l in thisFont.selectedLayers]

            # Loop through selected glyphs and layers to enable alignment
            for thisGlyph in selectedGlyphs:
                for thisLayer in thisGlyph.layers:
                    if thisLayer.isMasterLayer or thisLayer.isSpecialLayer:
                        for thisComponent in thisLayer.components:
                            thisComponent.setDisableAlignment_(False)
                        print(f"Enabled alignment in {thisGlyph.name} - {thisLayer.name}")

        except Exception as e:
            # Display error message in Glyphs macro window
            Glyphs.showMacroWindow()
            print(f"Enable Alignment Error: {e}")

    def centerGlyphs(self, sender):
        try:
            thisFont = Glyphs.font
            selectedLayers = thisFont.selectedLayers

            if len(selectedLayers) == 1 and selectedLayers[0].selection:
                currentLayer = selectedLayers[0]
                selectionOrigin = currentLayer.selectionBounds.origin.x
                selectionWidth = currentLayer.selectionBounds.size.width
                shift = self.shiftMatrix((currentLayer.width - selectionWidth) * 0.5 - selectionOrigin)
                for item in currentLayer.selection:
                    try:
                        if type(item) == GSNode:
                            item.x += shift.tX
                        else:
                            item.applyTransform(shift)
                    except Exception as e:
                        print(e)
            else:
                for thisLayer in selectedLayers:
                    shift = self.shiftMatrix((thisLayer.LSB - thisLayer.RSB) * -0.5)
                    thisLayer.applyTransform(shift)

            print("✅ Centered: %s" % (", ".join([l.parent.name for l in selectedLayers])))

        except Exception as e:
            # Display error message in Glyphs macro window
            Glyphs.showMacroWindow()
            print("\n⚠️ 'Center Glyphs' Script Error:\n")
            import traceback
            print(traceback.format_exc())
            print()
            raise e

    def shiftMatrix(self, xShift):
        transform = NSAffineTransform.transform()
        transform.translateXBy_yBy_(xShift, 0)
        return transform.transformStruct()

# Create an instance of the ModifyGlyphManager
ModifyGlyphManager()
