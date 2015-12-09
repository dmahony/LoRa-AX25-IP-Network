# Lora-Chat-Device
Using cheap LoRa wireless modules to chat over long distances.

This is a work in progress project to try and get LoRa wireless modules to chat to each other.

Here is an example of how I would like it to work:

LoRa device connects to either a Raspberry Pi or OpenWRT router and users can connect to webpage to send and recieve text messages with encryption. Perhaps sending different types of files could be viable by converting the files to text and prepending them with a certain flag so the receiver knows how to decode it.

Eg: 
upload image to webpage > webpage converts to hex and breaks it into max payload length chunks and adds flag to indicate file type > sends data via LoRa > other LoRa recieves text with flag telling to convert hex to image > displays in chat box

<b>Current prototypes are using:</b>

Inair9b (sx1276) connected to Raspberry Pi via SPI using <a href="https://github.com/mayeranalytics/pySX127x">pySX127x </a>

<img src="http://i.imgur.com/SBA0ONi.jpg" alt="Inair9b-arduino-nano">
<br>(sketchy Rpi2 protoype w/ PoE)</br>
<br>will probably move on to using the Raspberry Pi zero once they become available.

Previous prototype:
Inair9b (sx1276) with an Arduino Nano via SPI and connects to A5-V11 OpenWRT router via usb serial adapter using  <a href="https://github.com/PaulStoffregen/RadioHead">RadioHead Packet Library</a>

<img src="http://imgur.com/o91j5aj.jpg" alt="Inair9b-arduino-nano">
<br>(no OpenWRT router attached in picture)</br>






<b>Settings to use</b>

 <img src="http://i.imgur.com/bcRODsF.png" alt="LoRa-Speed-Settings"><br>
To get maximum range I would use: Bandwidth 10.4kHz Spreading Factor 12 Coding rate 4/5 Frequency Reference TCXO which would give me a bandwidth of 24bps.It would be too low for anything other than text. Testing pending.


<b>Inspirations:</b><br> 
<a href="http://ossmann.blogspot.com.au/2012/10/the-toorcon-14-badge.html">Toorcon 14 badge hacked into RF chat system in 2 days!</a><br>
Toorchat <a href="https://github.com/hathcox/ToorChat">Toorchat github</a><br>

<a href="https://youtu.be/pkTlTCUeec0?t=622">Toorchat Hak5 demo with YARD stick one device</a><br>

<a href="http://www.gotenna.com/">GoTenna device, similar idea to what I want but uses the Multi Use Radio System (MURS) and is expensive.</a><br>

Contact.<br>
If anyone would like to contribute or ask any questions please don't hesitate to contact me on danielwmahony@gmail.com

<b>Possible Github repos to use</b><br> 
<a href="https://github.com/mayeranalytics/pySX127x">pySX127x </a><br>
<a href="https://github.com/PaulStoffregen/RadioHead">RadioHead Packet Library</a><br>
<a href="https://github.com/hathcox/ToorChat">Toorchat</a><br>
<a href="https://github.com/Lora-net">Lora-net</a><br>
<a href="https://github.com/PiInTheSky/lora-gateway">PiInTheSky Lora-gateway</a><br>
<a href="https://github.com/telecombretagne/LoRaFABIAN">LoRaFABIAN</a><br>
<a href="https://github.com/TheThingsNetwork/">TheThingsNetwork</a><br>

Other Information.<br>
LoRa Introduction <a href="http://www.instructables.com/id/Introducing-LoRa-/">LoRa Introduction</a><br>
SX1276/7/8 Datasheet <a href="http://www.semtech.com/images/datasheet/sx1276_77_78_79.pdf">Datasheet</a><br>
