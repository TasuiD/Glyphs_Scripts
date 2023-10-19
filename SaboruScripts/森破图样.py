#MenuTitle: 森破图样
# Glyphs Version: 3.1.2 (3151)
# Python Version: 3
# Developer: DrayZ
# -*- coding: utf-8 -*-

import re
from vanilla import Window, List, Button, TextBox

class TitleExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.titles = self.extract_titles()
        
        self.w = Window((300, 200), "Sample Text Box")
        self.w.titleList = List((10, 10, -10, -70), self.titles, allowsMultipleSelection=False)
        self.w.extractButton = Button((10, -50, -10, 30), "Use Selected Text", callback=self.extract_title)
        
        self.w.open()

    def extract_titles(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            titles = re.findall(r'##(.*?)##', text)
            return titles
        except FileNotFoundError:
            return ["File not found"]
        except Exception as e:
            return [f"Error: {str(e)}"]

    def extract_title(self, sender):
        selected_title = self.w.titleList.getSelection()
        with open(self.file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        if selected_title:
            title_to_extract = self.titles[selected_title[0]]
            pattern = r'##{}##(.*?)%%'.format(re.escape(title_to_extract))
            matches = re.findall(pattern, text, re.DOTALL)
            if matches:
                Font.currentTab.text = matches[0]
                print("!!!")
            else:
                print(f'Title "{title_to_extract}" not found in the text file.')  # Print an error message
        else:
            print("Please select a title.")  # Print a message when no title is selected

file_path = 'SampleTextDataset/SampleText.txt'
app = TitleExtractor(file_path)
