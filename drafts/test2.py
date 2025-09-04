from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.popup import Popup
import webbrowser
from kivy.core.window import Window
from kivy.uix.widget import Widget as Spacer

from kivy.properties import StringProperty
#from kivy.properties import ListProperty


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        #data = ListProperty([])
        self.config = []

        # Создаем интерфейс экрана
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        layout2 = BoxLayout(orientation='horizontal', padding=10, spacing=10)

        self.textinput = TextInput(hint_text="Ввод конфигурации по одному символу")

        lbl = Label(text="Ввод конфигурации по одному символу", font_size='30sp', color=[0, 1, 0, 1])

        self.lbl2 = Label(text=f"конфигурация: {self.config}", font_size='30sp', color=[0, 1, 0, 1])

        btn1 = Button(text="Ввод", font_size='20sp', background_color=[0, 1, 0, 1], height=100)
        btn1.bind(on_press=self.inputtext)

        btn2 = Button(text="Конец ввода", font_size='20sp', background_color=[0, 1, 0, 1], height=100)
        btn2.bind(on_press=self.go_to_screen2)

        layout.add_widget(lbl)
        layout.add_widget(self.lbl2)
        layout.add_widget(self.textinput)
        layout2.add_widget(btn1)
        layout2.add_widget(btn2)
        layout.add_widget(layout2)

        self.add_widget(layout)

    def check_config(self):
        if "q1" not in self.config:
            print("в конфигурации нет q1")
            return False
        else:
            return True

    def inputtext(self, instance):
        text = self.textinput.text
        self.textinput.text = ""
        if text == "0" or text == "1" or text == "q1":
            self.config.append(text)
        else:
            print("Введите другое")

        self.lbl2.text = f"конфигурация: {self.config}"
        print(self.config)

    def go_to_screen2(self, instance):
        #self.data = self.config
        if self.check_config():
            self.manager.get_screen("screen2").config = list(self.config)
            self.manager.get_screen("screen2").lbl3.text = f"Текущая конфигурация: {self.config}"
            self.manager.current = 'screen2'
        else:
            self.manager.current = 'screen2'
            self.manager.current = 'screen1'


class Screen2(Screen):
    def __init__(self, **kwargs):
        super(Screen2, self).__init__(**kwargs)
        self.config = []

        self.rule = []

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        layout2 = BoxLayout(orientation='horizontal', padding=10, spacing=10)

        self.textinput = TextInput(hint_text="Ввод правила по одному символу")

        lbl = Label(text="Ввод правила по одному символу", font_size='30sp', color=[0, 1, 0, 1])
        lbl2 = Label(text="текущий формат: δ(q, a) = (b, D, p)\nдопустимые значения: δ(q¹, 0/1) = (0/1, R/L, q¹/q⁰)",
                     font_size='30sp', color=[0, 1, 0, 1])
        self.lbl3 = Label(text=f"Текущая конфигурация: {self.config}\n", font_size='30sp', color=[0, 1, 0, 1])
        self.lblN = Label(text=f"Новая конфигурация: *её нет*", font_size='30sp', color=[0, 1, 0, 1])
        self.lbl4 = Label(text=f"Текущее правило: {self.rule}", font_size='30sp', color=[0, 1, 0, 1])
        self.lbl5 = Label(text="введите, где стоит xxx: δ(q1, xxx) = (*, *, *): ", font_size='30sp', color=[0, 1, 0, 1])

        btn1 = Button(text="Ввод", font_size='20sp', background_color=[0, 1, 0, 1], height=100)
        btn1.bind(on_press=self.enter_rule)

        btn2 = Button(text="Применить правило", font_size='20sp', background_color=[0, 1, 0, 1], height=100)
        btn2.bind(on_press=self.apply_rule)

        layout.add_widget(lbl)
        layout.add_widget(lbl2)
        layout.add_widget(self.lbl3)
        layout.add_widget(self.lblN)
        layout.add_widget(self.lbl4)
        layout.add_widget(self.lbl5)
        layout.add_widget(self.textinput)
        layout2.add_widget(btn1)
        layout2.add_widget(btn2)
        layout.add_widget(layout2)
        self.add_widget(layout)

    def enter_rule(self, instance):
        text = self.textinput.text.lower()
        print('начали запись правила')

        if len(self.rule) == 0 and text in ('0', '1'):
            self.rule.append(text)
            print('записали 1')
            self.lbl5.text = f"введите, где стоит xxx: δ(q1, {self.rule[0]}) = (xxx, *, *): "
        elif len(self.rule) == 1 and text in ('0', '1'):
            self.rule.append(text)
            print('записали 2')
            self.lbl5.text = f"введите, где стоит xxx: δ(q1, {self.rule[0]}) = ({self.rule[1]}, xxx, *): "
        elif len(self.rule) == 2 and text in ('r', 'l'):
            self.rule.append(text)
            print('записали 3')
            self.lbl5.text = f"введите, где стоит xxx: δ(q1, {self.rule[0]}) = ({self.rule[1]}, {self.rule[2]}, xxx): "
        elif len(self.rule) == 3 and text in ('q1', 'q0'):
            self.rule.append(text)
            print('записали 4')
            self.lbl5.text = f"получено правило: δ(q1, {self.rule[0]}) = ({self.rule[1]}, {self.rule[2]}, {self.rule[3]}): "
        print(self.rule)
        self.textinput.text = ''

    def check_rule(self):
        cfg = self.config
        rule = self.rule
        q1_index = cfg.index("q1")
        if q1_index + 1 >= len(cfg):
            print("нет символа справа от q1")
            return False
        if cfg[q1_index + 1] != rule[0]:
            print("справа от q1: ", cfg[q1_index + 1])
            print("значение w1: ", rule[0])
            print("символ справа не соответствует 'a'")
            return False
        else:
         return True

    def apply_rule(self, instance):
        print("мы на этом месте")
        if self.check_rule():
            cfg = self.config
            rule = self.rule
            q1_index = cfg.index("q1")
            cfg[q1_index + 1] = rule[1]
            if rule[2] == "r":
                cfg[q1_index], cfg[q1_index + 1] = cfg[q1_index + 1], cfg[q1_index]
                if rule[3] == "q0":
                    q1_index = cfg.index("q1")
                    cfg[q1_index] = 'q0'
            elif rule[2] == "l":
                cfg[q1_index], cfg[q1_index - 1] = cfg[q1_index - 1], cfg[q1_index]
                if rule[3] == "q0":
                    q1_index = cfg.index("q1")
                    cfg[q1_index] = 'q0'
            self.lblN.text = f'Новая конфигурация: {cfg}'
        else:
            print("проверка провалилась")
            return 0






    # def inputtext(self, instance):
    #     print("Переданный список из 1 класса",self.config)
    #     t1 = self.textinput.text
    #     print(t1)
    #     if t1 == "0" or t1 == "1":
    #         self.lbl5.text = f"введите, где стоит xxx: δ(q1, {t1}) = (xxx, *, *): "
    #         t2 = self.textinput.text
    #     if t2 == "0" or t2 == "1":
    #         self.lbl5.text = "введите, где стоит xxx: δ(q1, {t1}) = ({t2}, xxx, *): "
    #         t3 = self.textinput.text.lower()
    #     if t3 == "r" or t3 == "l":
    #         self.lbl5.text = "введите, где стоит xxx: δ(q1, {t1}) = ({t2}, {t3}, xxx): "
    #         t4 = self.textinput.text
    #     if t4 == "q1" or t4 == "q0":
    #         print(f"δ(q¹, {t1}) = ({t2}, {t3}, {t4})")
    #     return t1, t2, t3, t4

    #def inputtext(self, instance):
    #    t1 = self.textinput.text
    #    if t1 == "0" or t1 == "1":
    #        self.lbl5.text = f"введите, где стоит xxx: δ(q1, {t1}) = (xxx, *, *): "
    #        t2 = self.textinput.text
    #        if t2 == "0" or t2 == "1":
    #            self.lbl5.text ="введите, где стоит xxx: δ(q1, {t1}) = ({t2}, xxx, *): "
    #            t3 = self.textinput.text.lower()
    #            if t3 == "r" or t3 == "l":
    #                self.lbl5.text ="введите, где стоит xxx: δ(q1, {t1}) = ({t2}, {t3}, xxx): "
    #                t4 = self.textinput.text
    #                if t4 == "q1" or t4 == "q0":
    #                    print(f"δ(q¹, {t1}) = ({t2}, {t3}, {t4})")
    #                    return t1, t2, t3, t4

    #self.textinput.text = ""
    #if text == "0" or text == "1" or text == "q1":
    #    self.rule.append(text)
    #else:
    #    print("Введите другое")

    #self.lbl4.text = f"правило: {self.rule}"
    #print(self.rule)


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(Screen2(name='screen2'))
        return sm


if __name__ == '__main__':
    MyApp().run()
