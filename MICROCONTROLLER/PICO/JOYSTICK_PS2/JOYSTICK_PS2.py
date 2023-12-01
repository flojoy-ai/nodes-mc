from typing import Literal, Optional, cast
from flojoy import DataContainer, JobResultBuilder, OrderedTriple, flojoy, OrderedPair

@flojoy
def JOYSTICK_PS2(
    default: Optional[DataContainer] = None,
    ADC_x_axis_pin: Literal[26, 27, 28] = 27, # TODO Have an array passed into literal instead, apparently only 3.11 and above
    ADC_y_axis_pin: Literal[26, 27, 28] = 26,
    is_pressed_pin: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                    18, 19, 20, 21, 22, 26, 27, 28] = 16
) -> OrderedTriple:
    """The Joystick PS2 node allows to read from a PS2 joystick.

    Parameters
    ----------
    ADC_x_axis_pin: specifies the pin to read the x axis from
    ADC_y_axis_pin: specifies the pin to read the y axis from
    is_pressed_pin: specifies the pin to read the button press from
    """
    from machine import Pin, ADC  # type: ignore

    read_x_axis = ADC(Pin(int(ADC_x_axis_pin))).read_u16()
    read_y_axis = ADC(Pin(int(ADC_y_axis_pin))).read_u16()
    read_button = Pin(int(is_pressed_pin), Pin.IN, Pin.PULL_UP).value()

    print(read_x_axis)

    return OrderedTriple(x=read_x_axis, y=read_y_axis, z=read_button)


    