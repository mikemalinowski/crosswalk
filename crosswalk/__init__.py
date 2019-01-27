"""
crosswalk is an experiment into function re-routing when you might
want to define a standardised API to a piece of functionality which
may require different implementations in different environments (such
as environments with embedded interpreters).

The idea is that the a standard API would be defined by the addition of
sub modules, where functions within them would be decorated with the 
reroute decorator. Any function decorated as such should be re-implemented
within the sub module implementations. Any function not decorated would
not be required to re-implement.

There is also an UndefinedRouting mechanism which allows for a host 
implementation of 'over implement'. This ultimately means that a host
implementation adds a function which is not defined in the Standard API. 
In this situation, when calling that function through crosswalk, rather
than fail it will attempt to dynamically add the function on the fly
to allow the re-routing to occur.

As with any abstract layer there is a cost of implementation. 
"""
from ._core import reroute
from ._core import UndefinedRouting

# -- These are functions used to help generate
# -- hosts
from ._generate import generate

# -- This is the list of modules exposed as part
# -- of the stanard api
from . import example
