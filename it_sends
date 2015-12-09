
from SX127x.LoRa import *
from SX127x.board_config import BOARD
import array
import hexdump


def handle_input(input):
    ary = array.array('B', input)
#    print[(hexdump.dump(ary, sep=" , 0x"))]
    lora.write_payload(ary.tolist())

BOARD.setup()

lora = LoRa()
lora.set_mode(MODE.STDBY)
lora.set_payload_length(100)
input=raw_input('Enter a message >>\n')
handle_input(input)
lora.set_mode(MODE.TX)

BOARD.teardown()
