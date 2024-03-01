# MenuTitle: 森破图样与乱数假文
# Glyphs Version: 3.1.2 (3151)
# Python Version: 3
# Developer: DrayZ
# -*- coding: utf-8 -*-

import random
import re
from vanilla import Window, List, Button, EditText, CheckBox, TextBox

class TitleAndRandomTextGenerator:
    def __init__(self, text_file_path=None):
        self.text_file_path = text_file_path
        self.titles = self.extract_titles()
        
        self.text_size = 100
        self.add_punctuation = True
        self.desired_glyphs = "万三上下不业东两个中为主乐九也习书了二云五些交京亮人什今从他以们会但住作你做儿元先光全八公六共关兴册再军农冬几出刀分别到前力办加动包北医十千午半卫厂去又双反发口只叫可台叶吃合同后向听吵和哥哭四回因国土在地坐声外多大天太头奇女奶她好妈妹姐子字学孩家对小少就尺山岁工己巾市师干平年广床开当很心快成我手才打找把放文方日早时明星春是晚更月有朋木本机条来林果树校样桌正每比毛民气水江河洗海火灯点然爷爸片牙牛狗猫王玩现班瓜生用田电画白百的皮目直看真着知石票秋穿窗立站竹笑米红经给网羊美羽老耳胖脸自舌花草虫行衣被西要见让话语说课谁豆贝走起跑跳身车边过还这进道那都里金长门问阳阴雨雪青面音页风飞饭饱马高鱼鸟一七次没船"
        self.punctuation_list = "，。、：；！？"
        self.get_han_letter_characters = [glyph.string for glyph in Glyphs.font.glyphs if glyph.script == "han" and glyph.category == "Letter"]
        self.exist_desired_glyphs = [t for t in self.desired_glyphs if t in self.get_han_letter_characters]

        self.w = Window((400, 300), "Sample Text and Random Text Generator")
        self.setup_ui()

    def setup_ui(self):
        self.w.titleList = List((10, 10, -10, 100), self.titles, allowsMultipleSelection=False)
        self.w.extractButton = Button((10, 120, -10, 30), "Use Selected Text", callback=self.extract_title)
        
        self.w.text_size_input = EditText((10, 170, 80, 22), placeholder="Enter text size", callback=self.update_parameters)
        self.w.AutomaticAlignmentText = TextBox((100, 172, -10, 20), "⬅️ Enter text size", sizeStyle="regular", selectable=True,)
        self.w.text_size_input.set("100")  # Set a default value
        self.w.add_punctuation_checkbox = CheckBox((10, 200, -10, 20), "Add Punctuation", value=True, callback=self.update_parameters)
        self.w.generate_button = Button((10, 230, -10, 30), "Generate Random Text", callback=self.generate_and_show_random_text)
        
        self.w.open()

    def extract_titles(self):
        try:
            with open(self.text_file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            titles = re.findall(r'##(.*?)##', text)
            return titles
        except FileNotFoundError:
            return ["File not found"]
        except Exception as e:
            return [f"Error: {str(e)}"]

    def extract_title(self, sender):
        selected_title = self.w.titleList.getSelection()
        if selected_title:
            title_to_extract = self.titles[selected_title[0]]
            pattern = r'##{}##(.*?)%%'.format(re.escape(title_to_extract))
            text = self.read_file_content()
            matches = re.findall(pattern, text, re.DOTALL)
            if matches:
                Glyphs.font.currentTab.text = matches[0]
                print("Title extracted successfully!")
            else:
                print(f'Title "{title_to_extract}" not found in the text file.')  # Print an error message
        else:
            print("Please select a title.")  # Print a message when no title is selected

    def update_parameters(self, sender):
        self.text_size = int(self.w.text_size_input.get()) if self.w.text_size_input.get() else 10
        self.add_punctuation = self.w.add_punctuation_checkbox.get()

    def generate_and_show_random_text(self, sender=None):
        random_text = self.get_plain_characters()
        self.show_in_current_tab(random_text)

    def show_in_current_tab(self, text):
        font = Glyphs.font
        if font and font.currentTab:
            # Set the text of the current tab
            font.currentTab.text = text
        else:
            print("Font or current tab not available")

    def get_random_character(self):
        if self.exist_desired_glyphs and random.random() < 0.75:
            return random.choice(self.exist_desired_glyphs)
        else:
            return random.choice(self.get_han_letter_characters)

    def get_random_punctuation(self):
        return random.choice(self.punctuation_list)

    def get_plain_characters(self):
        characters = [self.get_random_character() for _ in range(self.text_size)]
        
        # Optionally add punctuation
        if self.add_punctuation:
            characters_with_punctuation = []
            for char in characters:
                characters_with_punctuation.append(char)
                # Add punctuation randomly after each character
                if random.random() < 0.08:  # Adjust the probability as needed
                    characters_with_punctuation.append(self.get_random_punctuation())
            characters_with_punctuation.append("。")
            return ''.join(characters_with_punctuation)
        else:
            return ''.join(characters)

    def read_file_content(self):
        try:
            with open(self.text_file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return "File not found"
        except Exception as e:
            return f"Error: {str(e)}"


if __name__ == "__main__":
    text_file_path = 'SampleTextDataset/SampleText.txt'
    app = TitleAndRandomTextGenerator(text_file_path)
