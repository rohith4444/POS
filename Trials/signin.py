from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from PIL import Image
import time
import numpy

class SigninWindow(BoxLayout):
    def on_start(self, **kwargs):
        cameraOrImage = self.ids.camera_or_image
        camera = Camera(resolution=(320, 240), play=True, id="camera")
        camera.play = True
        cameraOrImage.add_widget(camera)


    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        captured = False
        # camera = self.ids['camera']
        # texture = camera.texture
        # size=texture.size
        # pixels = texture.pixels
        # pil_image=Image.frombytes(mode='RGBA', size=size,data=pixels)
        # numpypicture=numpy.array(pil_image)
        # print(numpypicture)
        # timestr = time.strftime("%Y%m%d_%H%M%S")
        # image = camera.export_to_png("IMG_1.png".format(timestr))
        # print("Captured")
        captured = True

        cameraButtonsLayout = self.ids.camera_button_layout

        if (captured):
            print("captured")
            button = Button(text='Re-Capture', on_press= self.recapture())
            cameraButtonsLayout.add_widget(button)

    def recapture(self):
        cameraOrImage = self.ids.camera_or_image
        camera = Camera(resolution=(320, 240), play=True)
        camera.play = True
        cameraOrImage.add_widget(camera)
        print("recapturing")


class SigninApp(App):
    def build(self):
        return SigninWindow()


if __name__ == "__main__":
    sa = SigninApp()
    sa.run()