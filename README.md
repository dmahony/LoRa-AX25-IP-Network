<h1>LoRa-AX25-IP-Network</h1>
<p>Utilising inexpensive wireless modules and open source software to form networks over long distances using AX25 and IP networking in the unlicensed ISM bands, without reliance on a centralised service provider.</p>
<p>This is ideal for:</p>
<ul>
<li>Privacy minded individuals</li>
<li>People living under oppressive governments</li>
<li>Remote communities</li>
<li>Natural Disaster areas</li>
<li>Testing low bandwidth applications eg, COAP ROHC</li>
</ul>
<p>LoRa radios allow us to reach much further distances than standard Wifi but at heavily reduced data rates. The small amount of data can still provide us with chat and other basic text services.</p>
<img src="https://i.imgur.com/3t4fcat.png" alt="Weechat-encrypted"> 
<h2>Features:</h2>
<ul>
<li>AX25 and TCP/IP networking</li>
<li>Highly Extensible, add your own servers for whatever you like (bandwidth permitting)</li>
<li>IRC over LoRa radios to chat over long distances with encrypted messaging.</li>
<li>Versatile Connection methods, use as a separate modem or all in one device with a single board computer.</li>
<li>Fetch News, RSS feeds, Wikipedia Summaries from Clients with Internet Connection.</li>
<li>Internet Gateway. Provide internet to other devices.</li>
<li>Solar Powered nodes</li>
<li>Versatile connection methods allow people of all skill levels to participate. Can&rsquo;t solder? Just hook it up with breadboard wires</li>
<li>Low cost, under $USD10 per modem</li>
</ul>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>LoRachat IRC encrypted <a href="https://youtu.be/R3EcQO4Yrec ">https://youtu.be/R3EcQO4Yrec </a></p>
<p>Wikipedia Summary Lookup - AX25 LoRa <a href="https://youtu.be/0-O8Qfpu2O0 ">https://youtu.be/0-O8Qfpu2O0 </a>&nbsp;</p>
<h2>&nbsp;</h2>
<h2>Hardware</h2>
<h3>Radio:</h3>
<p>E32-915T30D Lora Long Range UART SX1276 915mhz <strong>1W</strong> from CDEBYTE store on Aliexpress: <a href="https://www.aliexpress.com/item/2Pc-Lot-CDEBYTE-915MHz-8000m-Long-Range-SX1276-Wireless-Transmitter-rf-Module-E44-TTL-1W-UART/32802838747.html ">https://www.aliexpress.com/item/2Pc-Lot-CDEBYTE-915MHz-8000m-Long-Range-SX1276-Wireless-Transmitter-rf-Module-E44-TTL-1W-UART/32802838747.html </a></p>
<p>or</p>
<p>E32-915T20D Lora Long Range UART SX1276 915mhz <strong>100mW</strong></p>
<p><a href="https://www.aliexpress.com/item/2Pc-Lot-CDEBYTE-915MHz-3000m-Long-Range-SX1276-Wireless-Transmitter-rf-Module-E44-TTL-100-UART/32804955120.html">https://www.aliexpress.com/item/2Pc-Lot-CDEBYTE-915MHz-3000m-Long-Range-SX1276-Wireless-Transmitter-rf-Module-E44-TTL-100-UART/32804955120.html</a></p>
<p>Great store on Aliexpress, worth having a look as they often have excellent deals.</p>
<h3>Computer:</h3>
<p>This should work on any Linux device that allows connection to the radio via UART or USB UART adapter.</p>
<p>I use a Raspberry Pi Zero W with the radio connected via UART pins</p>
<p>The Raspberry Pi Zero W allows for many different connection methods:</p>
<ul>
<li>Run a WiFi hotspot for areas without an Internet/Network Connection</li>
<li>Use it in Wireless client mode to connect to your existing network.</li>
<li>If you connected the radio via UART the spare USB port could be used for the many of the Pi&rsquo;s OTG modes.</li>
<li>Or use the USB port for a network adapter (RJ45 Network Connection etc)</li>
<li>Bluetooth to Serial or Bluetooth PAN networking</li>
<li>Many other possibilities using the Pi&rsquo;s GPIO pins.</li>
</ul>
<h2>Software</h2>
<ul>
<li>Raspbian (debian) Stretch Lite: <a href="https://downloads.raspberrypi.org/raspbian_lite_latest ">https://downloads.raspberrypi.org/raspbian_lite_latest </a></li>
<li>Weechat IRC client</li>
<li>Weechat crypt.py plugin <a href="https://weechat.org/scripts/source/crypt.py.html/ ">https://weechat.org/scripts/source/crypt.py.html/ </a></li>
<li>Weechat Relay <a href="https://weechat.org/files/doc/stable/weechat_relay_protocol.en.html">https://weechat.org/files/doc/stable/weechat_relay_protocol.en.html</a></li>
<li>Glowing Bear Weechat frontend (modified for offline use): <a href="https://github.com/dmahony/glowing-bear">https://github.com/dmahony/glowing-bear</a></li>
<li>MiniIRCd IRC server</li>
<li>For more of the software used please see the installation instructions</li>
</ul>
<h2>Usage</h2>
<p>Link to Installation Instructions: <a href="https://github.com/dmahony/Lora-Chat-Device/wiki/Installation-Instructions ">https://github.com/dmahony/Lora-Chat-Device/wiki/Installation-Instructions </a></p>
<h2>Contributing</h2>
<p>This project is completely open source, contributions are encouraged, see the TODO list.</p>
<p>Please contact me at <a href="mailto:danielwmahony@gmail.com ">danielwmahony@gmail.com </a></p>
<p>&nbsp;</p>
<h2>TODO list</h2>
<ul>
<li>Create installation script with prompts to set callsign, IP address, UART or USB radio connection etc.</li>
<li>Maybe a web interface? There is an excellent frontend for WeeChat called GlowingBear: https://github.com/glowing-bear/glowing-bear (May need modification to work offline)</li>
<li>Modify linux AXcall program to not require valid Amateur radio callsigns, current workaround is to use a valid callsign as the source address.</li>
<li>Create Minimal sized image for fast deployment</li>
<li>Modify ESP32-Seriual-Bridge so it only uses 1 serial port and no bluetooth. <a href="https://github.com/AlphaLima/ESP32-Serial-Bridge">https://github.com/AlphaLima/ESP32-Serial-Bridge</a></li>
<li>Better utilisation of E32 Modules, use the wake on receive feature to wake up an esp32 from deep sleep mode.</li>
<li>Utilise Termux on Android as a client device. (Currently does not include AX25 related packages)</li>
<li>Look into mesh networking solutions that work with ipv4 (MTU too small for ipv6)</li>
<li>Create a Printed Circuit Board that holds a cheap Arduino / esp32 and LoRa chip</li>
<li>ROHC, Robust Header Compression: Compress headers for smaller packet sizes</li>
<li>CoAP Constrained Application Protocol:</li>
<li><a href="https://matrix.org/blog/2019/03/12/breaking-the-100-bps-barrier-with-matrix-meshsim-coap-proxy/">https://matrix.org/blog/2019/03/12/breaking-the-100-bps-barrier-with-matrix-meshsim-coap-proxy/</a></li>
</ul>
