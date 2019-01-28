Crosswalk
=========

__Note: This is currently pre-release__

Crosswalk is an experimentation to develop an approach of exposing a
standardised/common API to interact with from within different
environments - inspired largely by conversations with Lee Dunham (a 
fantastic Tech Artist and keen driver in this area).

The general idea is that an API is exposed at the crosswalk level,
where each function which is expected to be implemented is then
decorated with a ```@reroute``` decorator. This decorator dynamically
redirects the function call to an implementation which is usable from
within the current host environment.

An example of this might be defining a common API for applications
such as Modo, Houdini and Maya. Each one requires the use of an internal
API which is only accessible from within its own embedded python
interpreter. The use of crosswalk would allow for a 'minimum' common
api be defined, then each implementation 'fills in the gaps'.

 In such a situation you'd have a folder structure along the lines
 of :

 **crosswalk/constraints.py -> def parentConstraint(..)**

This function would be decorated with ```@reroute``` as its not
an implementation, its just declaring the expectation of the function
being implemented.

Each implementation would then look like:

**crosswalk/hosts/modo/constraints.py -> def transformConstraint(..)**

**crosswalk/hosts/houdini/constraints.py -> def transformConstraint(..)**

In this example - providing crosswalk is on the PythonPath - we could
take the following code and run it seamlesslys in both Modo and
Houdini without any alteration.

```
import crosswalk

crosswalk.constraints.transformConstraint(obj_a, obj_b)
```

When calling the code you do not need to call the direct modo/houdini
implementation as all the rerouting is dynamic.

Specified Host
==============

The default mechanism for Crosswalk is to always utilise the first 
host which is importable. In the context of Modo and Houdini, this 
means that you'll always get the Modo utils when in Modo and the 
Houdini utils when in houdini (because each rely on their own applications
api, and are therefore not importable within each others embedded
interpreters).

This works well until you implement multiple hosts for the same
application. An example of this might be Maya, where some developers
utilise OpenMaya, others develop using maya.cmds and others also 
utilise PyMel. In this scenario we could have three different host
implementations, and all are immediately importable - and therefore
valid. 

To help solve this we have a special keyword argument which can be
passed to any function exposed through crosswalk. That kwarg is ```xpa='host_name'```.
By passing this argument, and specifying the host you want to utilise
you can direct the re-routing operation to a specific host. An
example might be:

Using PyMel
```
import crosswalk
import pymel.core as pm

cns = crosswalk.constraints.transformConstraint(pm.selected()[0], xapi='pymel')
print(type(cns)) # -- pm.nt.parentConstraint
```

Using Maya.cmds
```
import crosswalk
import maya.cmds

cns = crosswalk.constraints.transformConstraint(maya.cmds.ls(sl=True), xapi='cmds')
print(type(cns)) # -- str
```

Over-Implementing
=================

When taking the example of a common Application API its probable that
the base API will stay relatively generic, but you may still want to
utilise more bespoke functionality within the implementation. This has
the downside of limiting how much can be shared, but it does mean you do
not need to incorporate multiple libraries to do the same thing.

To do this with crosswalk you can simply add further functions within
your implementation that are not exposed at the base level (therefore
they never exist with a ```@reroute``` decorator.

Under the hood, crosswalk will take any unresolvable call and attempt
to dynamically re-route it blindly. Therefore you could have a specific
function for modo, such as:

 **crosswalk/hosts/modo/constraints.py -> fusionConstraints(..)**

 This does not exist in ```crosswalk.constraints``` but rather than
 failing it will still dynamically re-route where possible. Where it
 is not possible you will recieve a *NotImpemented Error*.


Benefits
========

One of the biggest benefits of this approach is the utilisation of
shared functionality at the base API level. For instance, taking
an example of a time module such as:

```
crosswalk.time.start() # -- Returns the start time
crosswalk.time.end() # -- Returns the end time
crosswalk.time.range() # -- Returns the current time range
```

With these three functions we only actually need two of them to be
implemented within each host, the *start*(* and *end()* functions -
as the *range()* function can be inferred by calling ```end() - start()```
In this way we can start to limit the cost of implementing a new host
as not all functions always need re-implementing.

Alternatives
============

The concept presented here was first inspired by looking at Cross3d - an
interesting cross-application API developed by Blur Studios. They utilise
many of these concepts in a slightly different way. The main difference
is that the Cross3d base API is object based, and therefore enforces
a coding structure whilst crosswalk is entirely function based, and is
therefore considered a utility library rather than a wholesome API in
its own right.


Performance
===========

Performance is always going to be factor - and for every layer of
abstraction we pay a cost. Therefore, we gain the benefit of a sharable
utility library where code can easibly be re-utilised within multiple
environments along with a low implementation cost - but we do pay
a runtime cost for this dynamic redirection.

As much of the process is cached on the fly to minimise this cost. For
instance, the looking up of available hosts is only ever done once. Also
once a function has been mapped to the relevant host its mapping is
cached and the process does not need to be performed again.

We will always pay a decoration cost - as that is the primary mechanism
we utilise to redirect. Within **crosswalk** is a *_timings.py* module
which can be executed to get an idea of what this cost might be within
your desired host.


Contribute
==========

If you would like to contribute thoughts, ideas, fixes or features please get in touch! mike@twisted.space
