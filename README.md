Crosswalk
=========

Crosswalk is an experimentation into creatingn a single entry point
for utility functionality of similar applications, most notably Max, Maya
Motionbuilder and Modo.

## Current Application Support

* Blender
* Maya
* Motion Builder
* Standalone Python

## Command Reference

### **Objects**
```
app.objects.create(name, parent)
app.objects.exists(object_name)
app.objects.get_name(object)
app.objects.get_object(object_name)
app.objects.get_parent(object)
app.objects.get_children(object)
app.objects.set_parent(object, parent)
app.objects.all_objects_with_attribute(attribute_name)
```

### **Attributes**
```
app.attributes.get_attribute(object, attribute_name)
app.attributes.has_attribute(object, attribute_name)
app.attributes.set_attribute(object, attribute_name, value)
app.attributes.add_float_attribute(object, attribute_name, value)
app.attributes.add_string_attribute(object, attribute_name, value)
```

### **Selection**
```
app.selection.select(object)
app.selection.selected()
```

## Usage Example
```python
from crosswalk import app

# -- Example of creating objects
a = app.objects.create("a")
b = app.objects.create("b")

# -- Manipulate the hierarchy
app.objects.set_parent(b, a)

for child in app.objects.get_children(a):
    print(app.objects.get_name(child))
    
# -- Work with attributes
app.attributes.add_string_attribute(a, "demo", "this is a demo")
value = app.attributes.get_attribute(a, "demo")
print(value)

# -- Interact with the selection
app.selection.select(a)
for item in app.selection.selected():
    print(app.objects.get_name(item))
```