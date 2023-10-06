import numpy as np
from flojoy import flojoy, OrderedPair, Scalar, Vector
from ..utils.arithmetic_utils import get_val, reduce


@flojoy
def DIVIDE(
        a: OrderedPair | Scalar | Vector,
        b: list[OrderedPair | Scalar | Vector]
) -> OrderedPair | Scalar | Vector:
    """The DIVIDE node divides two or more numeric arrays, matrices, dataframes, or constants element-wise.

    When a constant is divided into an array or matrix, each element in the array or matrix will be divided by the constant value.

    Inputs
    ------
    a : OrderedPair|Scalar|Vector
        The input that will be divide by b.
    b : OrderedPair|Scalar|Vector
        The input that will divide a.

    Returns
    -------
    OrderedPair|Scalar|Vector
        OrderedPair if a is an OrderedPair.
        x: the x-axis of input a.
        y: the result of the division of input a by input b.

        Scalar if a is a Scalar.
        c: the result of the division of input a by input b.

        Vector if a is a Vector.
        v: the result of the division of input a by input b.
    """

    initial = get_val(a)
    seq = map(lambda dc: get_val(dc), b)
    y = reduce(lambda u, v: u / v, seq, initial)

    if isinstance(a, OrderedPair):
        return OrderedPair(x=a.x, y=y)
    elif isinstance(a, Vector):
        return Vector(v=y)
    elif isinstance(a, Scalar):
        return Scalar(c=y)
