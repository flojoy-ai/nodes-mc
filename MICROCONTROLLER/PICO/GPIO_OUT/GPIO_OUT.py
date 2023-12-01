from typing import Literal, Optional, cast
from flojoy import DataContainer, JobResultBuilder, flojoy

@flojoy
def GPIO_OUT(
    default: Optional[DataContainer] = None,
    pin: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                    18, 19, 20, 21, 22, 26, 27, 28] = 1, # TODO Have an array passed into literal instead, apparently only 3.11 and above
    mode: Literal["Toggle", "On", "Off"] = "Toggle",
) -> DataContainer:
    """The PIN_OUT node specifies voltage output through the specified PIN \
        on a Rasbperry Pico. This is a GPIO (General Purpose Input/Output).

    Parameters
    ----------
    pin: specifies the pin to send out voltage
    mode: specifies the mode of the LED,
    - on: turns the LED on
    - off: turns the LED off
    - toggle: toggles the LED (on -> off, off -> on)
    """
    from machine import Pin  # type: ignore

    selected = Pin(int(pin), Pin.OUT)

    if mode == "On":
        selected.value(1)
    elif mode == "Off":
        selected.value(0)
    elif mode == "Toggle":
        selected.toggle()

    result = cast(
        DataContainer,
        JobResultBuilder().from_inputs([default] if default else []).build(),
    )

    return result
