import paho.mqtt.client as mqtt

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider

from local_settings import broker_ip, device_mac

def calc_checksum(stream):
    checksum = 0
    for i in range(1, 14):
        checksum = checksum ^ stream[i]
    stream[14] = checksum & 0xFF
    return bytearray(stream)


def cmd_brightness(value):
    assert 0 <= value <= 10000
    payload = bytearray.fromhex("28 00 00 00 00 00 00 00 00 00 00 00 00 f0 00 29")
    payload[7] = value & 0xFF
    payload[8] = value >> 8
    return payload


class TechlifeControl(App):
    def build(self):
        self.prev_val = 0
        self.client = mqtt.Client()
        self.client.connect(broker_ip)

        layout = BoxLayout(orientation='vertical')
        s = self.slider = Slider(min=0, max=10000, value=3000)
        s.bind(on_touch_move=self.dim)
        btn_on = Button(text='On')
        btn_off = Button(text='Off')
        btn_on.bind(on_release=self.on)
        btn_off.bind(on_release=self.off)
        layout.add_widget(btn_on)
        layout.add_widget(btn_off)
        layout.add_widget(s)
        return layout

    def send(self, cmd):
        self.client.publish("dev_sub_" + device_mac, calc_checksum(cmd))  

    def dim(self, *args):
        v = int(10000 * self.slider.value_normalized)
        if abs(v - self.prev_val) > 50:
            self.prev_val = v
            print(v)
            self.send(cmd_brightness(v))

    def on(self, *args):
        self.send(bytearray.fromhex("fa 23 00 00 00 00 00 00 00 00 00 00 00 00 23 fb"))

    def off(self, *args):
        self.send(bytearray.fromhex("fa 24 00 00 00 00 00 00 00 00 00 00 00 00 24 fb"))


if __name__ == '__main__':
    TechlifeControl().run()

