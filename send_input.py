#!/usr/bin/env python

""" A simple beacon transmitter class to send a 1-byte message (0x0f) in regular time intervals. """

# Copyright 2015 Mayer Analytics Ltd.
#
# This file is part of pySX127x.
#
# pySX127x is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# pySX127x is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more
# details.
#
# You can be released from the requirements of the license by obtaining a commercial license. Such a license is
# mandatory as soon as you develop commercial activities involving pySX127x without disclosing the source code of your
# own applications, or shipping pySX127x with a closed source product.
#
# You should have received a copy of the GNU General Public License along with pySX127.  If not, see
# <http://www.gnu.org/licenses/>.


import sys
import hexdump
import array
from time import sleep
from SX127x.LoRa import *
from SX127x.LoRaArgumentParser import LoRaArgumentParser
from SX127x.board_config import BOARD

BOARD.setup()

parser = LoRaArgumentParser("A simple LoRa beacon")
parser.add_argument('--single', '-S', dest='single', default=False, action="store_true", help="Single transmission")
parser.add_argument('--wait', '-w', dest='wait', default=1, action="store", type=float, help="Waiting time between transmissions (default is 0s)")


class LoRaBeacon(LoRa):

    def __init__(self, verbose=False):
        super(LoRaBeacon, self).__init__(verbose)
        self.set_mode(MODE.SLEEP)
        self.set_dio_mapping([1,0,0,0,0,0])

    def on_rx_done(self):
        print("\nRxDone")
        print(self.get_irq_flags())
        print(map(hex, self.read_payload(nocheck=True)))
        self.set_mode(MODE.SLEEP)
        self.reset_ptr_rx()
        self.set_mode(MODE.RXCONT)

    def on_tx_done(self):
        global args
        self.set_mode(MODE.STDBY)
        self.clear_irq_flags()
        sys.stdout.flush()
        if args.single:
            print
            sys.exit(0)
        BOARD.led_off()
        sleep(args.wait)
#        self.write_payload([0x0f])
        BOARD.led_on()
        self.set_mode(MODE.TX)

    def on_cad_done(self):
        print("\non_CadDone")
        print(self.get_irq_flags())

    def on_rx_timeout(self):
        print("\non_RxTimeout")
        print(self.get_irq_flags())

    def on_valid_header(self):
        print("\non_ValidHeader")
        print(self.get_irq_flags())

    def on_payload_crc_error(self):
        print("\non_PayloadCrcError")
        print(self.get_irq_flags())

    def on_fhss_change_channel(self):
        print("\non_FhssChangeChannel")
        print(self.get_irq_flags())

    def handle_input(input):
        ary = array.array('B', input)
	print[(hexdump.dump(ary, sep=" , 0x"))]
	
    def start(self):
        global args
        sys.stdout.write("\rstart")
#	self.set_payload_length(10)        
#	self.write_payload[(hexdump.dump(ary, sep=" , 0x"))]
#	self.set_mode(MODE.TX)

    while True:
        try:
#        input=raw_input('Enter a message >>\n')
#        handle_input(input)

            input=raw_input('Enter a message >>\n')
            handle_input(input)
#	    print[(hexdump.dump(ary, sep=" , 0x"))]

        except EOFError:
            break    
#	handle_input(input)
#	self.write_payload[(hexdump.dump(ary, sep=" , 0x"))]
#	self.write_payload([48 , 0x65 , 0x6c , 0x6c , 0x6f , 0x20 , 0x57 , 0x6f , 0x72 , 0x6c , 0x64 , 0x21])
#        self.set_mode(MODE.TX)

lora = LoRaBeacon(verbose=False)
args = parser.parse_args(lora)

lora.set_pa_config(pa_select=1)
lora.set_rx_crc(True)
lora.set_agc_auto_on(True)
lora.set_lna_gain(GAIN.NOT_USED)
lora.set_coding_rate(CODING_RATE.CR4_6)
lora.set_implicit_header_mode(False)
lora.set_pa_config(max_power=15, output_power=15)
lora.set_pa_config(max_power=15, output_power=15)
lora.set_low_data_rate_optim(True)
lora.set_pa_ramp(PA_RAMP.RAMP_50_us)


print(lora)
#assert(lora.get_lna()['lna_gain'] == GAIN.NOT_USED)
assert(lora.get_agc_auto_on() == 1)

print("Beacon config:")
print("  Wait %f s" % args.wait)
print("  Single tx = %s" % args.single)
print("")
try: input("Press enter to start...")
except: pass

try:
    lora.start()
    self.set_payload_length(10)         
    self.write_payload[(hexdump.dump(ary, sep=" , 0x"))]
#    self.write_payload[('hexdump.dump(ary, sep=" , 0x"))]
    self.set_mode(MODE.TX)
    print(txdone)

except KeyboardInterrupt:
    sys.stdout.flush()
    print("")
    sys.stderr.write("KeyboardInterrupt\n")
finally:
    sys.stdout.flush()
    print("")
    lora.set_mode(MODE.SLEEP)
    print(lora)
    BOARD.teardown()
