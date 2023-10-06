from typing import Literal, Optional, cast
from flojoy import DataContainer, JobResultBuilder, flojoy


@flojoy
def LED(
    default: Optional[DataContainer] = None,
    mode: Literal["Toggle", "On", "Off", "Mock"] = "Toggle",
) -> DataContainer:
    """The LED node toggles the LED on a Rasbperry Pico"

    Parameters
    ----------
    mode: specifies the mode of the LED,
    - on: turns the LED on
    - off: turns the LED off
    - toggle: toggles the LED (on -> off, off -> on)
    """
    print("RUNNING LED NODE!")
    if mode != "Mock":
        from machine import Pin  # type: ignore

        led = Pin("LED", Pin.OUT)

        if mode == "On":
            led.value(1)
        elif mode == "Off":
            led.value(0)
        elif mode == "Toggle":
            led.toggle()
    else:
        print("LED ACTIVATED")

    result = cast(
        DataContainer,
        JobResultBuilder().from_inputs([default] if default else []).build(),
    )

    return result
