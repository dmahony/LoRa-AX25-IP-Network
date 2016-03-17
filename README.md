# Lora-Chat-Device (working title)

<p>Using cheap LoRa wireless modules to chat over long distances.

This is a work in progress project to create a cheap, long range chat device for private, decentralized communication. This project is completely open source and contributions are very welcome!

I'm only a begginer programmer but with a bit of help I think we can create something amazing.</p>

<b>How It Works:</b>
User connects to a Raspberry Pi hotspot that hosts an XMPP chat server that you can connect to using almost any XMPP client. Users can then send data over long distances without the use of telephone networks or the internet.

<p>I recently discovered the fantastic Arduino-Kiss software by Folkert van Heusden (Github user: flok99)
Arduino-kiss allows for an Arduino and HopeRF module to be used as a KISS TNC https://en.wikipedia.org/wiki/KISS_%28TNC%29
The AX25 protocol allows us to do so many things like Addressing, routing and we can even use TCP/IP.</p>
TCP/IP over LoRa Video: https://youtu.be/Z9LDWIDyYq8

This software uses the Radiohead Packet Library so any compatible wireless tranceiver should work (with a little bit of modification)
http://www.airspayce.com/mikem/arduino/RadioHead/

Although the Performance limitations of the Arduino ATMega328P limit what we can do, we still have enough processing power to send short encrypted messages using software by John Goerzen (GitHub: jgoerzen) called ax25xmpp that lets us send messages using any XMPP client, you can even use OTR encryption.

<img src="http://i.imgur.com/iDSmCiD.jpg" alt="XMPP-AX25-chat"> 


An Arduino with ATMega328P only has 2048 bytes of RAM and the Arduino-KISS software allocates 3 * maxPacketSize. so for LoRa devices that is 762 bytes of ram which means some better hardware should improve the performance, I'm currently waiting on a few Moteino Megas and Arduino Dues to see if I can get it running fast enough for a BBS or viewing web pages.

Example BBS:
<img src="https://defacto2.net/file/view/ab31a4" alt="example-bbs">


I also have a few Maple Mini clones that are supposedly compatible with the RadioHead Packet Library that Arduino-KISS uses but I havent been able to get it working, if you know anything about Radiohead+Maple Mini please get in touch!
Getting the Maple Mini working with this would make it so much cheaper than the other options, Maple Mini clones on AliExpress are extremely cheap and powerful, they use a STM32 F103RCBT6 32-bit ARM Cortex M3 microprocessor with 120 KB Flash and 20 KB SRAM!


<b>Range:</b>
People have claimed huge distances with LoRa modules, some say in the dozens of Kilometers others say over 100 Kilometers (High Altitude Balloons) I'll report back as soon as I've done my own range tests.

<b>My Tests:</b>
<br>
<img src="http://i.imgur.com/tjdWeO5.png" alt="LoRa-Chat-coolum-peregian-test"> 
<br>
8.35km Test. No dropped packets and a very good signal strength, I think it can go much further that this but it was getting late and I had to return home. Next test I'll try go closer to 20km.


<br>
<img src="http://i.imgur.com/tfc3tMf.jpg" alt="LoRa-Chat interface alpha"> 
<br>

<b>Hardware:</b>
-Raspberry Pi (any model)<br>
-Inair9b Module or HopeRF RFM95<br>
- Arduino UNO (awaiting testing on something more powerful
-USB Wifi adapter that supports Hotspot<br>
-Wires to connect module to Arduino / Pi<br>
-alternatively, instead of using the wifi adapter you could use an esp8266, Bluetooth module, UART or any other method you prefer<br>
<br>
<b>Current prototype software:</b>
<br>
-Arduino-KISS by  to interface the sx1276 with Raspberry Pi<br>
-Butterfly Terminal to use the chat program from a web interface<br> 
-Lighttpd to host the website<br>
-startbootrap.com bare template<br>
-hostapd to set up an access point on the Raspberry Pi<br>
-isc-dhcp-server for serving DHCP to Wifi hotspot<br>
-Xabber XMPP for Android

<b>Current prototype hardware:</b>

Inair9b (sx1276) connected to Arduino via SPI using <a href="https://github.com/flok99/arduino-kiss">Arduino-KISS </a>

<img src="http://i.imgur.com/9Gtv727.jpg" alt="pi2-lora-chat">
<br>(early Rpi2 protoype)</br>

HopeRF RFM95 connected to Pi Zero via SPI using <a href="https://github.com/mayeranalytics/pySX127x">pySX127x </a>

<b>Hopeful future features:</b>

-Send GPS coordinates and view on offline Open Street Map, measure distance etc

-Codec2/FreeDV voice chat<br>
https://github.com/freedv/codec2<br>
-Narrow Band Television Video chat<br>
https://en.wikipedia.org/wiki/Narrow-bandwidth_television<br>
https://www.youtube.com/watch?v=1ShYefsbnAE<br>

-send any file (sane limits apply)<br>
-Encrytion for every feature<br>
-TCP/IP<br>
<br>
<b>Inspirations:</b><br> 
<a href="http://ossmann.blogspot.com.au/2012/10/the-toorcon-14-badge.html">Toorcon 14 badge hacked into RF chat system in 2 days!</a><br>
<a href="https://github.com/hathcox/ToorChat">Toorchat github</a><br>
<a href="https://youtu.be/pkTlTCUeec0?t=622">Toorchat Hak5 demo with YARD stick one device</a><br>
<a href="http://www.gotenna.com/">GoTenna device, similar idea to what I want but uses the Multi Use Radio System (MURS) and is expensive.</a><br>

<b>Contact</b><br>
If anyone would like to contribute or ask any questions please don't hesitate to contact me on danielwmahony@gmail.com

<b>Possible Github repos to use</b><br> 
<a href="https://github.com/mayeranalytics/pySX127x">pySX127x </a><br>
<a href="https://github.com/PaulStoffregen/RadioHead">RadioHead Packet Library</a><br>
<a href="https://github.com/hathcox/ToorChat">Toorchat</a><br>
<a href="https://github.com/Lora-net">Lora-net</a><br>
<a href="https://github.com/PiInTheSky/lora-gateway">PiInTheSky Lora-gateway</a><br>
<a href="https://github.com/telecombretagne/LoRaFABIAN">LoRaFABIAN</a><br>
<a href="https://github.com/TheThingsNetwork/">TheThingsNetwork</a><br>

<b>Other Information</b><br>
<a href="http://www.instructables.com/id/Introducing-LoRa-/?ALLSTEPS">Introducing LoRa™, by manuka </a><br>
<a href="http://www.semtech.com/images/datasheet/sx1276_77_78_79.pdf">SX1276/7/8 Datasheet</a><br>
<a href="http://modtronix.com/inair9b.html">InAir9b product page</a><br>
<a href="http://www.airspayce.com/mikem/arduino/RadioHead/">RadioHead Packet Radio library for embedded microprocessors</a><br>
<a href="https://revspace.nl/DecodingLora">DecodingLora; using RTL-SDR/software radio to decode LoRa</a>
