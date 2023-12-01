from typing import Literal, Optional, cast
from flojoy import DataContainer, JobResultBuilder, flojoy

@flojoy
def OLED_SH1106(
    default: Optional[DataContainer] = None,
    oled_width: int = 128,
    oled_height: int = 64,
    i2c_clock_pin: Literal["1", "3", "5", "7", "9", "11", "13", "15", "17", "19", "21", "27"] = "1",
    i2c_data_pin: Literal["0", "2", "4", "6", "8", "10", "12", "14", "16", "18", "20", "26"] = "0",
) -> DataContainer:
    """The OLED_SH1106 node allows to output to an OLED display 
    compatible with an SH1106 driver. 

    Parameters
    ----------
    oled_width: the pixel width of the OLED display
    oled_height: the pixel height of the OLED display
    i2c_clock_pin: the pin that will be used for the clock
    i2c_data_pin: the pin that will be used for the data
    """
    from machine import Pin, SoftI2C  # type: ignore
    from .sh1106 import SH1106_I2C
    i2c = SoftI2C(scl=Pin(int(i2c_clock_pin)), sda=Pin(int(i2c_data_pin)))
    oled = SH1106_I2C(oled_width, oled_height, i2c)
    oled.fill(0)
    oled.text("Hello World!", 0, 10)
    oled.show()

    result = cast(
        DataContainer,
        JobResultBuilder().from_inputs([default] if default else []).build(),
    )
    return result
