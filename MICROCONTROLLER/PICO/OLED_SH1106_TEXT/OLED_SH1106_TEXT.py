import time
from typing import Literal, Optional, cast
from flojoy import DataContainer, JobResultBuilder, flojoy, TextBlob, Scalar, OrderedTriple

@flojoy
def OLED_SH1106_TEXT(
    text: TextBlob | Scalar | OrderedTriple,
    oled_width: int = 128,
    oled_height: int = 64,
    i2c_clock_pin: Literal["1", "3", "5", "7", "9", "11", "13", "15", "17", "19", "21", "27"] = "1", # TODO Have an array passed into literal instead, apparently only 3.11 and above
    i2c_data_pin: Literal["0", "2", "4", "6", "8", "10", "12", "14", "16", "18", "20", "26"] = "0",
) -> DataContainer:
    """The OLED_SH1106 node allows to output text to an OLED display 
    compatible with an SH1106 driver. 

    Parameters
    ----------
    oled_width: the pixel width of the OLED display
    oled_height: the pixel height of the OLED display
    i2c_clock_pin: the pin that will be used for the clock
    i2c_data_pin: the pin that will be used for the data
    """

    if isinstance(text, OrderedTriple):
        text_inp = str(text.x) + ',' + str(text.y) + ',' + str(text.z)
    else:
        text_inp = text.text_blob if isinstance(text, TextBlob) else str(text.c)

    from machine import Pin, SoftI2C  # type: ignore
    from .sh1106 import SH1106_I2C

    i2c = SoftI2C(scl=Pin(int(i2c_clock_pin)), sda=Pin(int(i2c_data_pin)))
    print("init oled")
    oled = SH1106_I2C(oled_width, oled_height, i2c)
    print("init done")
    oled.fill(0)
    print("text_inp: ", text_inp)
    oled.text(text_inp, 0, 0)
    print("ran text")
    oled.show()


    result = cast(
        DataContainer,
        JobResultBuilder().from_inputs([text] if text else []).build(),
    )

    return result
