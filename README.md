# Lora-Chat-Device
Using cheap LoRa wireless modules to chat over long distances.

This is a work in progress project to try and get LoRa wireless modules to chat to each other.

here is an example of how I would like it to work:

LoRa device connects to either a Raspberry Pi or OpenWRT router and users can connect to webpage to send and recieve text messages with encryption. Perhaps sending different types of files could be viable by converting the files to text and prepending them with a certain flag so the receiver knows how to decode it.

Eg: 
upload image to webpage > webpage converts to base64 and breaks it into max payload length chunks and adds flag to indicate file type > sends data via LoRa > other LoRa recieves text with flag telling to convert base64 to image > displays in chat box

<b>Current prototypes are using:</b>

Inair9b (sx1276) with an Arduino Nano via SPI and connects to A5-V11 OpenWRT router via usb serial adapter using  <a href="https://github.com/PaulStoffregen/RadioHead">RadioHead Packet Library</a>

<img src="http://imgur.com/o91j5aj.jpg" alt="Inair9b-arduino-nano">
<br>(no OpenWRT router attached in picture)</br>

Inair9b (sx1276) connected to Raspberry Pi via SPI using <a href="https://github.com/mayeranalytics/pySX127x">pySX127x </a>




<b>Future Prototypes</b>

Both of these modules communicate via UART so I'm guessing it would be much easier to send data.

<a href="http://www.anarduino.com/details.jsp?pid=139">HopeRF HM-TRP</a> connected via UART to either Raspberry Pi or OpenWRT (cons; not LoRa! significantly less range)

 <img src="http://www.anarduino.com/images/hm-trp100.png" alt="HM-TRP" align="left"> 
<br>
<br>
<a href="http://www.hoperf.com/rf/data_link_module/HM-TRLR-S.htm">HopeRF HM-TRLR-S</a> connected via UART to either Raspberry Pi or OpenWRT (cons; Expensive!)<br><br>
 <img src="http://www.hoperf.com/upload/rf/HM-TRLR-HFS.jpg" alt="HM-TRLR-S" align="left"> 





Any of previously mentioned modules connected to the cheap Raspberry Pi Zero via either SPI or UART


Inspirations:<br> 
<a href="http://ossmann.blogspot.com.au/2012/10/the-toorcon-14-badge.html">Toorcon 14 badge hacked into RF chat system in 2 days!</a><br>

<a href="http://www.gotenna.com/">GoTenna device, similar idea to what I want but uses the Multi Use Radio System (MURS) and is expensive.</a><br>

Contact.<br>
If anyone would like to contribute or ask any questions please don't hesitate to contact me on danielwmahony@gmail.com


