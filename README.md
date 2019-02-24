<h1>Lora Chat AX25</h1>
<p align="left" style="margin-bottom: 0in; line-height: 0.2in"><font face="Liberation Serif, serif">Utilising
cheap wireless modules and open source software to communicate over
long distances using AX25 and IRC in the unlicensed ISM bands. </font>
</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<h1 class="western">Navigation</h1>
<p style="margin-bottom: 0in; line-height: 115%">-Summary&nbsp;</p>
<p style="margin-bottom: 0in; line-height: 115%">-Features&nbsp;</p>
<p style="margin-bottom: 0in; line-height: 115%">-Deployment/Usage&nbsp;</p>
<p style="margin-bottom: 0in; line-height: 115%">-Contributing&nbsp;</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<h1 class="western">Summary of project</h1>
<p style="margin-bottom: 0in; line-height: 115%">I created this
project to allow people to form their own networks that don’t rely
on a centralised service provider. 
</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 115%">This is ideal for:</p>
<ul>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Privacy
	minded individuals</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">People living
	under oppressive governments</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Remote
	communities 
	</p>
</ul>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 115%">Using the LoRa
radios allow us to reach much further than standard Wifi but at
heavily reduced data rates. 
</p>
<p style="margin-bottom: 0in; line-height: 115%">You won’t be able
to send large files like videos, however the reduced bandwidth of the
radios can send data over much further distances.</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<br>
<img src="http://i.imgur.com/tjdWeO5.png" alt="LoRa-Chat-coolum-peregian-test"> 
<br>
</p>
<p align="left" style="margin-bottom: 0in; line-height: 0.2in"><i>Link
to other Lora Range tests</i></p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 115%">The small amount of
data can still provide us with chat and other basic text services. 
</p>
<p align="left" style="margin-bottom: 0in; line-height: 0.2in"><br/>

</p>

<br>
<img src="https://i.imgur.com/3t4fcat.png" alt="Weechat-encrypted"> 
<br>
Wikipedia Summary Lookup - AX25 LoRa
https://youtu.be/0-O8Qfpu2O0<br>

</p>
<h1 class="western">Features</h1>
<p style="margin-bottom: 0in; line-height: 115%">Simple ncurses menu
to operate, no Linux knowledge required.</p>
<p style="margin-bottom: 0in; line-height: 115%">Internet Relay Chat
(IRC) over LoRa radios to chat over long distances&nbsp;</p>
<p style="margin-bottom: 0in; line-height: 115%">Encrypted IRC
Messages</p>
<p style="margin-bottom: 0in; line-height: 115%">Fetch News, RSS
feeds, Wikipedia Summaries from Clients with Internet Connection.</p>
<p style="margin-bottom: 0in; line-height: 115%">AX25 with TCP/IP
networking</p>
<p style="margin-bottom: 0in; line-height: 115%">Highly Extensible,
add your own servers for whatever you like (bandwidth permitting)</p>
<p align="left" style="margin-bottom: 0in; line-height: 0.2in"><i>link:
See my server setup running Mystic BBS, ax25 node, etc &nbsp;</i></p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<h1 class="western">Hardware</h1>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
<br/>

</p>
<p style="line-height: 115%"><b>Radio:</b></p>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
<span style="display: inline-block; border: none; padding: 0in"><font face="Liberation, serif"><font size="3" style="font-size: 12pt"><span style="background: #ffffff"><font color="#000000">RF95
connected via SPI to Arduino with ATmega328 </span></span></font></font></font>
</p>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
<span style="display: inline-block; border: none; padding: 0in"><font face="Liberation, serif"><font size="3" style="font-size: 12pt"><span style="background: #ffffff"><font color="#000000">I
prefer to use a module with the RF95 pre-soldered, this costs more
but the time saved is invaluable. </span></span></font></font></font>
</p>
<p style="line-height: 115%"><b>Premade Modules</b></p>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
<span style="display: inline-block; border: none; padding: 0in"><font face="Liberation, serif"><font size="3" style="font-size: 12pt"><span style="background: #ffffff"><font color="#000000">Moteino
Mega:</span></span></font></font></font></p>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
<span style="display: inline-block; border: none; padding: 0in"><font face="Liberation, serif"><font size="3" style="font-size: 12pt"><span style="background: #ffffff"><font color="#000000"><font color="#0000ff"><u><a href="https://lowpowerlab.com/shop/product/119">https://lowpowerlab.com/shop/product/119</a></u></font>
</span></span></font></font></font>
</p>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
<span style="display: inline-block; border: none; padding: 0in"><font face="Liberation, serif"><font size="3" style="font-size: 12pt"><span style="background: #ffffff"><font color="#000000">TTGO
Lora V2:</span></span></font></font></font></p>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
<span style="display: inline-block; border: none; padding: 0in"><font face="Liberation, serif"><font size="3" style="font-size: 12pt"><span style="background: #ffffff"><font color="#000000"><font color="#0000ff"><u><a href="https://www.aliexpress.com/item/TTGO-LORA32-V2-0-433-868-915Mhz-ESP32-LoRa-OLED-0-96-Inch-SD-Card-Blue/32846302183.html">https://www.aliexpress.com/item/TTGO-LORA32-V2-0-433-868-915Mhz-ESP32-LoRa-OLED-0-96-Inch-SD-Card-Blue/32846302183.html</a></u></font>
</span></span></font></font></font>
</p>
<p style="line-height: 115%"><b>Computer:</b></p>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
<span style="display: inline-block; border: none; padding: 0in"><font face="Liberation, serif"><font size="3" style="font-size: 12pt"><span style="background: #ffffff"><font color="#000000">This
should work on any Linux device that allows connection to the radio
via UART or USB.</span></span></font></font></font></p>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
<span style="display: inline-block; border: none; padding: 0in"><font face="Liberation, serif"><font size="3" style="font-size: 12pt"><span style="background: #ffffff"><font color="#000000">I
use a Raspberry Pi Zero W with the radio connected via UART</span></span></font></font></font></p>
<p style="line-height: 115%"><i>link to ‘My Hardware’ Page</i></p>
<p style="line-height: 115%"><br/>
<br/>

</p>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
<span style="display: inline-block; border: none; padding: 0in"><font face="Liberation, serif"><font size="3" style="font-size: 12pt"><span style="background: #ffffff"><font color="#000000">The
Raspberry Pi Zero W allows for many different connection methods.</span></span></font></font></font></p>
<ul>
	<li/>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
	<span style="display: inline-block; border: none; padding: 0in"><font face="Liberation, serif"><font size="3" style="font-size: 12pt"><span style="background: #ffffff"><font color="#000000">Run
	a WiFi hotspot for areas without an Internet/Network Connection</span></span></font></font></font></p>
	<li/>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
	<span style="display: inline-block; border: none; padding: 0in"><font face="Liberation, serif"><font size="3" style="font-size: 12pt"><span style="background: #ffffff"><font color="#000000">Use
	it in Wireless client mode to connect to your existing network. </span></span></font></font></font>
	</p>
	<li/>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
	<span style="display: inline-block; border: none; padding: 0in"><font face="Liberation, serif"><font size="3" style="font-size: 12pt"><span style="background: #ffffff"><font color="#000000">If
	you connected the radio via UART the spare USB port could be used
	for the many of the Pi’s OTG modes. </span></span></font></font></font>
	</p>
	<li/>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
	<span style="display: inline-block; border: none; padding: 0in"><font face="Liberation, serif"><font size="3" style="font-size: 12pt"><span style="background: #ffffff"><font color="#000000">Or
	use the USB port for a network adapter (RJ45 Network Connection etc)</span></span></font></font></font></p>
	<li/>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
	<span style="display: inline-block; border: none; padding: 0in"><font face="Liberation, serif"><font size="3" style="font-size: 12pt"><span style="background: #ffffff"><font color="#000000">Bluetooth
	to Serial or Bluetooth PAN networking</span></span></font></font></font></p>
	<li/>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
	<span style="display: inline-block; border: none; padding: 0in"><font face="Liberation, serif"><font size="3" style="font-size: 12pt"><span style="background: #ffffff"><font color="#000000">Many
	other possibilities using the Pi’s GPIO pins</span></span></font></font></font></p>
</ul>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
<br/>

</p>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
<br/>

</p>
<h1 class="western">Software</h1>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
<span style="display: inline-block; border: none; padding: 0in"><font face="Liberation, serif"><font size="3" style="font-size: 12pt"><span style="background: #ffffff"><font color="#000000">Raspbian
(debian) Stretch Lite:&nbsp;</span></span></font></font></font></p>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
<span style="display: inline-block; border: none; padding: 0in"><font face="Liberation, serif"><font size="3" style="font-size: 12pt"><span style="background: #ffffff"><font color="#000000"><font color="#0000ff"><u><a href="https://downloads.raspberrypi.org/raspbian_lite_latest">https://downloads.raspberrypi.org/raspbian_lite_latest</a></u></font>
</span></span></font></font></font>
</p>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
<span style="display: inline-block; border: none; padding: 0in"><font face="Liberation, serif"><font size="3" style="font-size: 12pt"><span style="background: #ffffff"><font color="#000000">Arduino-Kiss
by Folkert van Heusden:</span></span></font></font></font></p>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
<span style="display: inline-block; border: none; padding: 0in"><font face="Liberation, serif"><font size="3" style="font-size: 12pt"><span style="background: #ffffff"><font color="#000000"><font color="#0000ff"><u><a href="https://github.com/flok99/arduino-kiss">https://github.com/flok99/arduino-kiss</a></u></font>
</span></span></font></font></font>
</p>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
<span style="display: inline-block; border: none; padding: 0in"><font face="Liberation, serif"><font size="3" style="font-size: 12pt"><span style="background: #ffffff"><font color="#000000">or
instead of Arduino-Kiss by Folkert van Heusden you can try a modified
version by Josef Matondang (github: josefmtd) which cleans up the
code and makes it more efficient (no CRC etc):&nbsp;</span></span></font></font></font></p>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
<span style="display: inline-block; border: none; padding: 0in"><font face="Liberation, serif"><font size="3" style="font-size: 12pt"><span style="background: #ffffff"><font color="#000000"><font color="#0000ff"><u><a href="https://github.com/josefmtd/ax25-packet-network">https://github.com/josefmtd/ax25-packet-network</a></u></font>
</span></span></font></font></font>
</p>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
<br/>
Weechat crypt.py plugin<br>
https://weechat.org/scripts/source/crypt.py.html/<br>
	<br>
</p>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
<span style="display: inline-block; border: none; padding: 0in"><font face="Liberation, serif"><font size="3" style="font-size: 12pt"><span style="background: #ffffff"><font color="#000000">Weechat
IRC client</span></span></font></font></font></p>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
<span style="display: inline-block; border: none; padding: 0in"><font face="Liberation, serif"><font size="3" style="font-size: 12pt"><span style="background: #ffffff"><font color="#000000">MiniIRCd
IRC server</span></span></font></font></font></p>
<p style="margin-bottom: 0in; font-variant: normal; letter-spacing: normal; font-style: normal; line-height: 115%">
<span style="display: inline-block; border: none; padding: 0in"><font face="Liberation, serif"><font size="3" style="font-size: 12pt"><span style="background: #ffffff"><font color="#000000">For
more of the software used please see the installation instructions: https://github.com/dmahony/Lora-Chat-Device/wiki/Installation-Instructions</span></span></font></font></font></p>
<h1 class="western">Deployment / Usage</h1>
<p align="left" style="margin-bottom: 0in; line-height: 0.2in"><i>Link
to Installation Instructions: https://github.com/dmahony/Lora-Chat-Device/wiki/Installation-Instructions</i></p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<h1 class="western">Contributing</h1>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 115%">This project is
completely open source, contributions are encouraged.</p>
<p style="margin-bottom: 0in; line-height: 115%">Please contact me at
<font color="#0000ff"><u>danielwmahony@gmail.com</u></font>&nbsp;</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p align="left" style="margin-bottom: 0in; line-height: 0.2in"><b>TODO
list:</b></p>
<p align="left" style="margin-bottom: 0in; line-height: 0.2in"><br/>

</p>
<ul>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Create
	installation script with prompts to set callsign, IP address, &nbsp;UART
	or USB radio connection etc.</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%"></p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Create a
	Printed Circuit Board that holds a cheap Arduino / esp32 and LoRa
	chip</p>
</ul>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<ul>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Maybe a web
	interface? There is an excellent frontend for WeeChat called
	GlowingBear:&nbsp;</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%"><font color="#0000ff"><u><a href="https://github.com/glowing-bear/glowing-bear">https://github.com/glowing-bear/glowing-bear</a></u></font>
	&nbsp;</p>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">(May need
	modification to work offline)&nbsp;</p>
</ul>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<ul>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Modify linux
	AXcall &nbsp;program to not require valid Amateur radio callsigns,
	current workaround is to use a valid callsign as the source
	address.&nbsp;</p>
</ul>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<ul>
	<li/>
<p style="margin-bottom: 0in; line-height: 115%">Create
	Minimal sized image for fast deployment</p>
</ul>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
<p style="margin-bottom: 0in; line-height: 115%"><br/>

</p>
</body>
</html>
