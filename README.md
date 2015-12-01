# Lora-Chat-device
Using cheap LoRa wireless modules to chat over long distances.

This is a work in progress project to try and get LoRa wireless modules to chat to each other.

here is an example of how I would like it to work:

LoRa device connects to either a Raspberry Pi or OpenWRT router and users can connect to webpage to send and recieve text messages with encryption. Perhaps sending different types of files could be viable by converting the files to text and prepending them with a certain flag so the receiver knows how to decode it.

Eg: 
upload image to webpage > webpage converts to base64 and breaks it into max payload length chunks and adds flag to indicate file type > sends data via LoRa > other LoRa recieves text with flag telling to convert base64 to image > displays in chat box

Current prototypes are using:
Inair9b (sx1276) with an Arduino Nano via SPI and connects to A5-V11 OpenWRT router via usb serial adapter using RadioHead Packet Library https://github.com/PaulStoffregen/RadioHead



Inair9b (sx1276) connected to Raspberry Pi via SPI using pySX127x https://github.com/mayeranalytics/pySX127x

Future Prototypes
Both of these modules communicate via UART so I'm guessing it would be much easier to send data
HopeRF HM-TRP connected via UART to either Raspberry Pi or OpenWRT (cons; not LoRa! significantly less range)
http://www.anarduino.com/details.jsp?pid=139
HopeRF HM-TRLR-S connected via UART to either Raspberry Pi or OpenWRT (cons; Expensive!)
http://www.hoperf.com/rf/data_link_module/HM-TRLR-S.htm

<a href="http://www.hoperf.com/rf/data_link_module/HM-TRLR-S.htm">HopeRF HM-TRLR-S</a>


Any of previously mentioned modules connected to the cheap Raspberry Pi Zero via either SPI or UART


