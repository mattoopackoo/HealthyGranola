from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import time

class CheckScreen(Screen):
    pass

class CameraClickScreen(Screen):
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))


GUI = Builder.load_string("""

GridLayout:
    cols: 1
    ScreenManager:
        id: screen_manager
        CheckScreen:
            name: "check_screen"
            id: check_screen
        CameraClickScreen:
            name: "camera_click_screen"
            id: camera_click_screen




<CameraClickScreen>:
    orientation: 'vertical'
    GridLayout:
        cols: 1
        Camera:
            id: camera
            resolution: (640, 480)
            play: False
        ToggleButton:
            text: 'Play'
            on_press: camera.play = not camera.play
            size_hint_y: None
            height: '48dp'
        Button:
            text: 'Capture'
            size_hint_y: None
            height: '48dp'
            on_press:
                root.capture()
                app.root.ids['screen_manager'].transition.direction = 'left'
                app.root.ids['screen_manager'].current = 'check_screen'


<CheckScreen>:
    Button:
        font_size: 25
        on_press:
            app.root.ids['screen_manager'].transition.direction = 'left'
            app.root.ids['screen_manager'].current = 'camera_click_screen'
        Image:
            source: 'C:/Users/murzakjo/Downloads/photo_icon.png'
            center_x: self.parent.center_x
            center_y: self.parent.center_y

""")

class TestCamera(App):

    def build(self):
        return GUI


TestCamera().run()
