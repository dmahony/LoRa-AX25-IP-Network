LoRa-AX25-IP-Network

Utilising inexpensive wireless modules and open source software to form networks over long distances using AX25 and IP networking in the unlicensed ISM bands, without reliance on a centralised service provider.


This is ideal for:

    Privacy minded individuals

    People living under oppressive governments

    Remote communities
	
    Natural Disaster areas

    Testing low bandwidth applications eg, COAP ROHC
	
	

LoRa radios allow us to reach much further distances than standard Wifi but at heavily reduced data rates. The small amount of data can still provide us with chat and other basic text services.

Example: Encrypted Weechat

Features

AX25 and TCP/IP networking

Highly Extensible, add your own servers for whatever you like (bandwidth permitting)

IRC over LoRa radios to chat over long distances with encrypted messaging.

Versatile Connection methods, use as a separate modem or all in one device with a single board computer.

Fetch News, RSS feeds, Wikipedia Summaries from Clients with Internet Connection.

Internet Gateway. Provide internet to other devices.

Solar Powered nodes 

Versatile connection methods allow people of all skill levels to participate. Can’t solder? Just hook it up with breadboard wires 

Low cost, under $USD10 per modem





LoRa-Chat-coolum-peregian-test

Link to other Lora Range tests

Weechat-encrypted

LoRachat IRC encrypted
https://youtu.be/R3EcQO4Yrec
Wikipedia Summary Lookup - AX25 LoRa
https://youtu.be/0-O8Qfpu2O0
link: See my server setup running Mystic BBS, ax25 node, etc  







Computer:

This should work on any Linux device that allows connection to the radio via UART or USB.

I use a Raspberry Pi Zero W with the radio connected via UART pins

link to ‘My Hardware’ Page



The Raspberry Pi Zero W allows for many different connection methods.

    Run a WiFi hotspot for areas without an Internet/Network Connection

    Use it in Wireless client mode to connect to your existing network.

    If you connected the radio via UART the spare USB port could be used for the many of the Pi’s    OTG modes.

    Or use the USB port for a network adapter (RJ45 Network Connection etc)

    Bluetooth to Serial or Bluetooth PAN networking

    Many other possibilities using the Pi’s GPIO pins



Hardware

E32-915T30D Lora Long Range UART SX1276 915mhz 1W from CDEBYTE store on Aliexpress: https://www.aliexpress.com/item/2Pc-Lot-CDEBYTE-915MHz-8000m-Long-Range-SX1276-Wireless-Transmitter-rf-Module-E44-TTL-1W-UART/32802838747.html 
Great store on Aliexpress, worth having a look as they often have excellent deals.

Software

Raspbian (debian) Stretch Lite: 
https://downloads.raspberrypi.org/raspbian_lite_latest

Weechat crypt.py plugin
https://weechat.org/scripts/source/crypt.py.html/

Weechat IRC client
MiniIRCd IRC server

For more of the software used please see the installation instructions: https://github.com/dmahony/Lora-Chat-Device/wiki/Installation-Instructions
Deployment / Usage

Link to Installation Instructions: https://github.com/dmahony/Lora-Chat-Device/wiki/Installation-Instructions



Contributing


This project is completely open source, contributions are encouraged, see the TODO list.

Please contact me at danielwmahony@gmail.com 


TODO list:


Create installation script with prompts to set callsign, IP address, UART or USB radio connection etc.

Create a Printed Circuit Board that holds a cheap Arduino / esp32 and LoRa chip

Maybe a web interface? There is an excellent frontend for WeeChat called GlowingBear:
https://github.com/glowing-bear/glowing-bear
(May need modification to work offline)

Modify linux AXcall program to not require valid Amateur radio callsigns, current workaround is to use a valid callsign as the source address.

Create Minimal sized image for fast deployment

Modify Esp32 serial to wifi so it only uses 1 serial port and no bluetooth.

Better utilisation of E32 Modules, use the wake on receive feature to wake up an esp32 from deep sleep mode. 

Utilise Termux on Android as a client device. (Currently does not include AX25 related packages)

Look into mesh networking solutions that work with ipv4 (MTU to small for ipv6) 

ROHC, Robust Header Compression: Compress headers for smaller packet sizes

CoAP Constrained Application Protocol: 
https://matrix.org/blog/2019/03/12/breaking-the-100-bps-barrier-with-matrix-meshsim-coap-proxy/
