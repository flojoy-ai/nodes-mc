from typing import Any, Literal, TypedDict

from flojoy import JobResultBuilder, Scalar, flojoy


class ConditionalOutput(TypedDict):
    true: Any
    false: Any


@flojoy
def CONDITIONAL(
    x: Scalar,
    y: Scalar,
    operator_type: Literal["<=", ">", "<", ">=", "!=", "=="] = ">=",
) -> ConditionalOutput:
    """The CONDITIONAL node is a specialized node that compares two given Scalar inputs.
    We are planning to add support for more DataContainer types in the future.


    It then enqueues nodes connected with a "true" or "false" output based on the comparison result.

    Parameters
    ----------
    operator_type : select
        Specifies the type of comparison to be performed between the two inputs. The default value is ">=".
    """

    bool_ = compare_values(x.c[0], y.c[0], operator_type)
    print(bool_)

    data = None
    if bool_:
        data = x
    else:
        data = y

    next_direction = str(bool_).lower()

    return ConditionalOutput(
        true=JobResultBuilder().from_data(data).flow_to_directions(
            [next_direction]).build(),
        false=JobResultBuilder().from_data(data).flow_to_directions(
            [next_direction]).build(),
    )


def compare_values(first_value: Any, second_value: Any, operator: str):
    if operator == "<=":
        return first_value <= second_value
    elif operator == ">":
        return first_value > second_value
    elif operator == "<":
        return first_value < second_value
    elif operator == ">=":
        return first_value >= second_value
    elif operator == "!=":
        return first_value != second_value
    else:
        return first_value == second_value
