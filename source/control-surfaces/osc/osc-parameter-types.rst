.. _osc_parameter_types:

Parameter types
===============

An OSC message is laid out in this form:

``/path/of/command type parameter``

The type is there to indicate what the parameter is. This gives the idea
that parameter types are quite strict and if the command requires an
Integer *"i"* then the controller had better send it. However, the
checking of the parameter type is left to the receiving software.

What this means in practical terms is that the surface can get away with
sending the wrong type of parameter. There are some places where that
just doesn't make sense. For example, a parameter that is specified as a
Float with a range of ``0`` to ``1``, could be sent as an Integer, but
would only have full scale and minimum value with nothing in between.
This is not much use for a fader, though OK for a button.

There are a number of OSC controllers based on iOS and Android tablets
that only send or receive parameters as floats or text. These
controllers should have no problem sending bool or int values as floats.
Ardour will interpret the values as required.