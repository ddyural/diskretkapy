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

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.config = []

        # Создаем интерфейс экрана
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        layout2 = BoxLayout(orientation='horizontal', padding=10, spacing=10)

        self.textinput = TextInput(hint_text="Ввод конфигурации по одному символу")

        lbl = Label(text="Ввод конфигурации по одному символу", font_size='30sp', color=[0, 1, 0, 1])

        self.lbl2 = Label(text=f"конфигурация: {self.config}", font_size='30sp', color=[0, 1, 0, 1])

        btn1 = Button(text="Ввод", font_size='20sp', background_color=[0, 1, 0, 1],  height=100)
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
        self.manager.current = 'screen2'


class Screen2(Screen):
    def __init__(self, **kwargs):
        super(Screen2, self).__init__(**kwargs)

        self.config = []
        self.rule = []

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        layout2 = BoxLayout(orientation='horizontal', padding=10, spacing=10)

        self.textinput = TextInput(hint_text="Ввод правила по одному символу")

        lbl = Label(text="Ввод правила по одному символу", font_size='30sp', color=[0, 1, 0, 1])
        lbl2 = Label(text="текущий формат: δ(q, a) = (b, D, p)\nдопустимые значения: δ(q¹, 0/1) = (0/1, R/L, q¹/q⁰)", font_size='30sp', color=[0, 1, 0, 1])
        lbl3 = Label(text=f"Текущая конфигурация: {self.config}", font_size='30sp', color=[0, 1, 0, 1])
        self.lbl4 = Label(text=f"Текущее правило: {self.rule}", font_size='30sp', color=[0, 1, 0, 1])
        self.lbl5 = Label(text="введите, где стоит xxx: δ(q1, xxx) = (*, *, *): ", font_size='30sp', color=[0, 1, 0, 1])


        btn1 = Button(text="Ввод", font_size='20sp', background_color=[0, 1, 0, 1], height=100)
        btn1.bind(on_press=self.inputtext)

        btn2 = Button(text="Конец ввода", font_size='20sp', background_color=[0, 1, 0, 1], height=100)

        layout.add_widget(lbl)
        layout.add_widget(lbl2)
        layout.add_widget(lbl3)
        layout.add_widget(self.lbl4)
        layout.add_widget(self.lbl5)
        layout.add_widget(self.textinput)
        layout2.add_widget(btn1)
        layout2.add_widget(btn2)
        layout.add_widget(layout2)
        self.add_widget(layout)

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


