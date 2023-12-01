from typing import Literal, Optional, cast
from flojoy import DataContainer, JobResultBuilder, flojoy, Scalar

@flojoy
def GPIO_IN(
    default: Optional[DataContainer] = None,
    pin: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                    18, 19, 20, 21, 22, 26, 27, 28] = 1, # TODO Have an array passed into literal instead, apparently only 3.11 and above
    mode: Literal["Pull Down", "Pull Up"] = "Pull Down",
) -> Scalar:
    """The GPIO_IN node tracks input from the specified pin \
        on a Rasbperry Pico. This is a GPIO (General Purpose Input/Output).

    Parameters
    ----------
    pin: specifies the pin as input
    mode: specifies the mode of the LED,
    - Pull Down: uses the pull down resistor (no input -> at 0V)
    - Pull Up: attaches to 3.3V power source (no input -> at 3.3V)
    """
    from machine import Pin  # type: ignore

    read_from = Pin(int(pin), Pin.IN, Pin.PULL_DOWN) if mode == "Pull Down" else Pin(int(pin), Pin.IN, Pin.PULL_UP)

    cur_value = read_from.value()    
    print("GPIO IN:" + str(cur_value))
    return Scalar(c=cur_value)
