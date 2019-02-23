# Lora-Chat-Device (working title)

<p>Using cheap wireless modules to chat over long distances using AX25 and IRC in the unlicenced ISM bands.<br>
<br>
Raspberry Pi - Arduino - LoRa - AX25 - IRC <br><br>
This is a work in progress project to create a cheap, long range chat device for private, decentralized communication. This project is completely open source and contributions are very welcome!</p>
<br>
<b>How It Works:</b><br>
 
Users can then send data over long distances without the use of telephone networks or the internet via cheap RF modules.<br>

<p>Arduino-Kiss software by Folkert van Heusden (Github user: flok99) allows for an Arduino and HopeRF module to be used as a <a href="https://en.wikipedia.org/wiki/KISS_%28TNC%29">KISS TNC </a>

<br>The AX25 protocol allows us to do so many things like Addressing, routing and we can even use TCP/IP.</p>
[![AX25-TCPIP](http://img.youtube.com/vi/Z9LDWIDyYq8/0.jpg)](http://www.youtube.com/watch?v=Z9LDWIDyYq8 "AX25 TCP/IP over LoRa ")
<br>
<p>This software uses the Radiohead Packet Library so any compatible wireless tranceiver should work (with a little bit of modification)<br></p>
http://www.airspayce.com/mikem/arduino/RadioHead/
<br>

<b>Range:</b>
People have claimed huge distances with LoRa modules, some say in the dozens of Kilometres others say over 100 Kilometres (High Altitude Balloons) I'll report back as soon as I've done my own range tests.

<b>My Tests:</b>
<br>
<img src="http://i.imgur.com/tjdWeO5.png" alt="LoRa-Chat-coolum-peregian-test"> 
<br>
8.35km Test. No dropped packets and a very good signal strength, I think it can go much further that this but it was getting late and I had to return home. Next test I'll try go closer to 20km.
<br>
<br>
<b>Hardware:</b><br>
-Raspberry Pi (any model)<br>
-Inair9b Module or HopeRF RFM95<br>
-Arduino UNO (awaiting testing on something more powerful<br>
-USB Wifi adapter that supports Hotspot<br>
-Wires to connect module to Arduino / Pi<br>
-alternatively, instead of using the wifi adapter you could use an esp8266, Bluetooth module, UART or any other method you prefer<br>
<br>
<b>Current prototype software:</b> <br>
<a href="https://github.com/flok99/arduino-kiss"> Arduino-KISS by Folkert van Heusden (flok99)</a><br>

<br>


<b>Hopeful future features:</b>

-Fully working BBS<br>
-Send GPS coordinates and view on offline Open Street Map, measure distance etc<br>
-Codec2/FreeDV voice chat<br>
https://github.com/freedv/codec2<br>
-Narrow Band Television Video chat<br>
https://en.wikipedia.org/wiki/Narrow-bandwidth_television<br>
https://www.youtube.com/watch?v=1ShYefsbnAE<br>

-send small files, maybe create a simple web page based Image/Sound/whatever converter<br>
-Encrytion for every feature<br>
<br>


<b>Installation Instructions:</b><br>
https://github.com/dmahony/Lora-Chat-Device/wiki/Installation-Instructions<br>


For the Hardware:<br>
EASIEST/ PREMADE: <a href="https://lowpowerlab.com/shop/moteinomega">Moteino with built in RFM95 </a>
<br>OR MAKE YOUR OWN: Inair9b (sx1276) or HopeRF RFM95 connected to Arduino via SPI<br>
I'll eventually release a Raspberry Pi prebuilt image to make it easier for those not comfortable with Linux!
<br>
<b>Contact</b><br>
If anyone would like to contribute or ask any questions please contact me on danielwmahony@gmail.com


<b>Other Information</b><br>
<a href="http://www.instructables.com/id/Introducing-LoRa-/?ALLSTEPS">Introducing LoRa™, by manuka </a><br>
<a href="http://www.semtech.com/images/datasheet/sx1276_77_78_79.pdf">SX1276/7/8 Datasheet</a><br>
<a href="http://modtronix.com/inair9b.html">InAir9b product page</a><br>
<a href="http://www.airspayce.com/mikem/arduino/RadioHead/">RadioHead Packet Radio library for embedded microprocessors</a><br>
<a href="https://revspace.nl/DecodingLora">DecodingLora; using RTL-SDR/software radio to decode LoRa</a>
