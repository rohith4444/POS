from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.cache import Cache
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
from kivy.graphics.texture import Texture
from PIL import Image as IMAGE
from IPython.display import display
from IPython.display import Image as iImage
import time
import numpy
from io import BytesIO

class SigninWindow(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        cameraOrImageLayout = self.ids.camera_or_image
        camera = self.ids['camera']
        captured = False
        # texture = camera.texture
        # size=texture.size
        # pixels = texture.pixels
        # pil_image=IMAGE.frombytes(mode='RGBA', size=size,data=pixels)
        # numpypicture=numpy.array(pil_image)
        # print(numpypicture)
        image = camera.export_to_png("IMG_1.png")
        print("Captured")
        captured = True
        time.sleep(1)
        cameraButtonsLayout = self.ids.camera_button_layout

        if (captured):
            print("captured")
            cameraButtonsLayout.clear_widgets()
            button = Button(text='Re-Capture', on_press=self.recapture)
            button2 = Button(text="Ok")
            cameraButtonsLayout.add_widget(button)
            cameraButtonsLayout.add_widget(button2)

            # buf = pil_image.tostring()
            # image_texture = Texture.create(size=(image.shape[1], image.shape[0]), colorfmt='rgb')
            # image_texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')
            Cache.remove('kv.image')
            Cache.remove('kv.texture')
            cameraOrImageLayout.clear_widgets()
            imageWidget = Image(source = "IMG_1.png")
            cameraOrImageLayout.add_widget(imageWidget)



    def recapture(self, arg):
        cameraOrImage = self.ids.camera_or_image
        cameraOrImage.clear_widgets()
        camera = Camera(resolution=(640, 480), play=True)
        cameraOrImage.add_widget(camera)

        cameraButtonsLayout = self.ids.camera_button_layout
        cameraButtonsLayout.clear_widgets()
        print("recapturing")


class SigninApp(App):
    def build(self):
        return SigninWindow()


if __name__ == "__main__":
    sa = SigninApp()
    sa.run()