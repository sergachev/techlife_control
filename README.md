## A simple Python app to control TechLife Wi-Fi bulbs

Thanks to [Kivy](https://kivy.org/) runs on various platforms - tested on Linux and Android.
Based on research from [here](https://community.openhab.org/t/hacking-techlife-pro-bulbs/85940/45).


Bulbs use MQTT and by default use an insecure broker at cloud.qh-tek.com. 
It is possible to use your own one either with help of DNS redirection, 
or modifying bulb's configuration sending it a special packet.

Initial configuration (connecting the bulb to your Wi-Fi network) can be done with 
[this](https://gist.github.com/csabavirag/334d9fa4028c17a69e3af4ea22838381#file-techlifepro_setup-py) script;
a packet to change the broker IP can be generated with [this](https://community.openhab.org/t/hacking-techlife-pro-bulbs/85940/25) script
and should be sent to the current broker (cloud.qh-tek.com out of the box).
