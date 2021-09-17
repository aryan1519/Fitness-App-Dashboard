from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
import pandas as pd
import numpy as np


Window.size = (370,670)

hr = 0
o2 = 0
kcal = 0
steps = 0

class DemoApp(MDApp):

    def refresh(self,obj):

        df = pd.read_csv('dataset.csv')

        l = np.array(df. iloc[-1:].values).tolist()[0]

        hr = l[0]
        o2 = l[1]
        kcal = l[2]
        steps = l[3]

        # label1.text = str(hr)+" bpm"
        # label2.text = str(o2)+" %"

        return hr,o2,kcal,steps


    def build(self):

        img1 = Image(source ='heart.png',size_hint_x = 0.3,size_hint_y = 0.3,pos = (10, 470))
        label1 = MDLabel(text = str(hr)+" bpm",
                         pos_hint={'center_x': 1, 'center_y': 0.88},
                         font_style = 'H4',
                         theme_text_color = 'Custom',
                         text_color = (244/255.0, 212/255.0, 124/255.0,1))


        img2 = Image(source ='oxy.png',size_hint_x = 0.3,size_hint_y = 0.23,pos = (10, 350))
        label2 = MDLabel(text = str(o2)+" %",
                         pos_hint={'center_x': 1, 'center_y': 0.65},
                         font_style = 'H4',
                         theme_text_color = 'Custom',
                         text_color = (244/255.0, 212/255.0, 124/255.0,1))


        img3 = Image(source ='kcal.png',size_hint_x = 0.35,size_hint_y = 0.35,pos = (10, 180))
        label3 = MDLabel(text = str(kcal)+" kcal",
                         pos_hint={'center_x': 1, 'center_y': 0.47},
                         font_style = 'H4',
                         theme_text_color = 'Custom',
                         text_color = (244/255.0, 212/255.0, 124/255.0,1))

        img4 = Image(source ='steps.png',size_hint_x = 0.35,size_hint_y = 0.35,pos = (10, 50))
        label4 = MDLabel(text = str(steps)+" steps",
                         pos_hint={'center_x': 1, 'center_y': 0.27},
                         font_style = 'H4',
                         theme_text_color = 'Custom',
                         text_color = (244/255.0, 212/255.0, 124/255.0,1))        

        def refresh():

            df = pd.read_csv('dataset.csv')

            l = np.array(df. iloc[-1:].values).tolist()[0]

            hr = l[0]
            o2 = l[1]
            kcal = l[2]
            steps = l[3]

            label1.text = str(hr)+" bpm"
            label2.text = str(o2)+" %"
            label3.text = str(kcal)+" kcal"
            label4.text = str(steps)+" steps" 

            # return hr,o2


        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.theme_style = "Dark"

        screen = Screen()

        btn_flat = MDRectangleFlatButton(text='Refresh',
                                         pos_hint={'center_x': 0.5, 'center_y': 0.1},
                                         on_press = lambda x:refresh())



        screen.add_widget(img1)
       
        screen.add_widget(label1)


        screen.add_widget(img2)
       
        screen.add_widget(label2)


        screen.add_widget(img3)
       
        screen.add_widget(label3)


        screen.add_widget(img4)
       
        screen.add_widget(label4)



        screen.add_widget(btn_flat)


        return screen


DemoApp().run()