import MaxPlus
import pymxs

from ._utils import to_pymxs


# ------------------------------------------------------------------------------
def add(element, name, property_type, value=None):

    # -- Attributes are better exposed in pymxs rather than
    # -- MaxPlus, so the internals of this function will work
    # -- in pymxs
    mx_element = to_pymxs(element)

    # -- If no block address is specified we automatically add one
    if '.' not in name:
        name = '%s.%s' % (
            name,
            name,
        )

    # -- Break out the block name and the attribute name
    block_name, attr_name = name.split('.')

    # -- If the block already exists then we need to get the definition
    # -- of that block, otherwise we need to create a new definition
    block = None
    existing_definition = None

    # -- Cycle over our attr defs on this object
    attr_defs = pymxs.runtime.custAttributes.getDefs(mx_element)
    if attr_defs:
        for attr_def in attr_defs:

            # -- We only care about blocks which share the block name
            if block_name == str(attr_def.name):
                # -- Get the source data for this attribute definition
                block = attr_def.source[:]
                existing_definition = attr_def
                break

    # -- If this is not a pre-existing block we create a new definition
    # -- otherwise we flag it as requiring redefinition
    block = block or _new_block_definition(block_name)

    # -- We now need to cycle over all the source and inject our new
    # -- attribute into it
    redefined_lines = list()
    lines = block.splitlines()

    # -- We now need to cycle over the definition source, and manipulate
    # -- it to add in our attribute
    idx = -1
    while True:

        # -- Increment our counter regardless of what happens
        idx += 1

        if idx >= len(lines):
            break

        # -- Get the current line
        line = lines[idx]

        # -- Check if we need to start wrangling a parameter. By default
        # -- we add new parameters to the top
        if line.strip().startswith('Parameters'):
            redefined_lines.append(line)
            redefined_lines.append(lines[idx + 1])
            redefined_lines.append(
                '\t\t%s type:#%s ui:%s' % (attr_name, property_type, attr_name))
            idx += 1
            continue

        # -- Check if we need to start wrangling the rollout of a
        # -- parameter
        elif line.strip().lower().startswith('rollout'):
            redefined_lines.append(line)
            redefined_lines.append(lines[idx + 1])
            redefined_lines.append('\t\tspinner %s "%s" type: #%s' % (
                attr_name, attr_name.title(), property_type))
            idx += 1
            continue

        else:
            redefined_lines.append(line)

    # -- We now stitch all the lines back together into a single string
    updated_block = '\n'.join(redefined_lines)

    # -- Finally, we either update the definition or add it depending
    # -- on whether its new or not
    if existing_definition:
        pymxs.runtime.custAttributes.redefine(
            existing_definition,
            updated_block,
        )

    else:
        pymxs.runtime.custAttributes.add(
            mx_element,
            pymxs.runtime.execute(updated_block),
        )

    # -- We now need to return the property as a MaxPlus parameter
    container = element.BaseObject.GetCustomAttributeContainer()

    for idx, block in enumerate(container):
        if block.GetName() == block_name:
            _b = block.GetParameterBlock()
            return _b.GetParamByName(attr_name)


# ------------------------------------------------------------------------------
def remove(element, name):
    # -- If no block address is specified we automatically add one
    if '.' not in name:
        name = '%s.%s' % (
            name,
            name,
        )

    # -- Break out the block name and the attribute name
    block_name, attr_name = name.split('.')

    # -- If the block already exists then we need to get the definition
    # -- of that block, otherwise we need to create a new definition
    block = None
    existing_definition = None

    # -- Pymxs has better support for properties, so utilise
    # -- that here
    mx_element = to_pymxs(element)

    # -- Cycle over our attr defs on this object
    attr_defs = pymxs.runtime.custAttributes.getDefs(mx_element)

    if not attr_defs:
        return

    for attr_def in attr_defs:

        # -- We only care about blocks which share the block name
        if block_name == str(attr_def.name):
            # -- Get the source data for this attribute definition
            block = attr_def.source[:]
            existing_definition = attr_def
            break

    if not block:
        return

    # -- We now need to cycle over all the source and inject our new
    # -- attribute into it
    redefined_lines = list()
    lines = block.splitlines()

    # -- We now need to cycle over the definition source, and manipulate
    # -- it to add in our attribute
    idx = -1
    while True:

        # -- Increment our counter regardless of what happens
        idx += 1

        if idx >= len(lines):
            break

        # -- Get the current line
        line = lines[idx]

        # -- Check if we need to start wrangling a parameter. By default
        # -- we add new parameters to the top
        test = line.strip().startswith('%s ' % attr_name)
        test = test or " '%s' " % attr_name in line
        test = test or ' "%s" ' % attr_name in line
        test = test or ' %s ' % attr_name in line
        if test:
            continue

        redefined_lines.append(line)

    # -- We now stitch all the lines back together into a single string
    updated_block = '\n'.join(redefined_lines)

    pymxs.runtime.custAttributes.redefine(
        existing_definition,
        updated_block,
    )

    # -- Check if we need to remove the block itself
    container = element.BaseObject.GetCustomAttributeContainer()

    for idx, block in enumerate(container):
        if block.GetName() == block_name and block.GetParameterBlock().Count() == 0:
            container.Remove(idx)

    return None


# ------------------------------------------------------------------------------
def get_value(element, property_name):

    try:
        value = pymxs.runtime.execute(
            """
            n_ = maxOps.getNodeByHandle %s
            n_.%s
            """ % (
                element.GetHandle(),
                property_name,
            )
        )
        return value

    except RuntimeError:
        if 'baseObject' not in property_name:
            return get_value(
                element,
                'baseObject.%s' % property_name,
            )

    return None


# ------------------------------------------------------------------------------
def set_value(element, property_name, value):

    if isinstance(value, str):
        value = '"%s"' % value

    else:
        value = str(value)

    try:
        exec_str = """
        n_ = maxOps.getNodeByHandle %s
        n_.%s = %s
        """ % (
            element.GetHandle(),
            property_name,
            value,
        )
        print(exec_str)
        pymxs.runtime.execute(exec_str)

    except RuntimeError:
        if 'baseObject' not in property_name:
            set_value(
                element,
                'baseObject.%s' % property_name,
                value,
            )


# ------------------------------------------------------------------------------
def link(source, destination):
    return None


# ------------------------------------------------------------------------------
def unlink(destination, source=None):
    return None


# ------------------------------------------------------------------------------
def _new_block_definition(block_name):
    """
    This will return a new block definition with the given block name

    :param block_name: Name of the block to define

    :return: str
    """
    return """
        myData = attributes "%s" version:1
        (
                                        -- Define the actual parameters
                                        Parameters main rollout:params
                                        (
                                        )

                                        -- Build the ui element
                                        rollout params "%s"
                                        (
                                        )
        )
        """ % (block_name, block_name)
