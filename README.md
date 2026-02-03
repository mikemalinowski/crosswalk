Crosswalk
=========

Crosswalk is an experimentation into creatingn a single entry point
for utility functionality of similar applications, most notably Max, Maya
Motionbuilder and Modo.

## Current Application Support

* Blender
* Maya
* Motion Builder
* 3dsmax
* Standalone Python

## Usage
The example below can be run in any of the applications listed above without changing 
any code. This allows a developer to write cross application tools easily. 

```python
import crosswalk

# -- Create some items
item_a = crosswalk.items.create("foo")
item_b = crosswalk.items.create("bar", parent=item_a)

# -- Print the hierarchy
print(f"Parent of {item_b} is {crosswalk.items.get_parent(item_b)}")
print(f"{item_a} has the following children: {crosswalk.items.get_children(item_a)}")

# -- Add an attribute and store some information
crosswalk.attributes.add_string_attribute(item_a, attribute_name="my_attribute", value="foobar")

# -- Now get the value
print(f"{item_a}.my_attribute = {crosswalk.attributes.get_value(item_a, attribute_name='my_attribute')}")

# -- Select something in the scene
selected = crosswalk.selection.select([item_a, item_b])

for item in crosswalk.selection.selected():
    name = crosswalk.items.get_name(item)
    print(f"We have selected {name}")
```
