import os
from . import _core


# -- Get the location of the crosswalk module
_ROOT = os.path.dirname(__file__)


# ------------------------------------------------------------------------------
def generate(host_name):
    """
    This will generate a new host layout which will auto fill the
    functions required to implement a minimum of the base API.

    :param host_name:
    :return:
    """
    # -- Check that the given host name is not already
    # -- in existence
    if host_name in _core.hosts():
        raise Exception('Host already exists (%s)' % host_name)

    # -- Collate a list of the files we need to read and
    # -- generate
    signatures = dict()

    for filename in os.listdir(_ROOT):

        # -- Join the path and the filename together to
        # -- get an absolute path
        filepath = os.path.join(
            _ROOT,
            filename,
        )

        # -- If this is not a file we ignore it
        if not os.path.isfile(filepath):
            continue

        # -- Finally we only look at python files and ignore
        # -- any files which start with an underscore.
        if filename.startswith('_') or not filename.endswith('.py'):
            continue

        # -- Store the file name (excluding the suffix) against
        # -- the filepath.
        module_name = filename.split('.')[0]
        signatures[module_name] = list()

        with open(filepath, 'r') as f:
            lines = f.readlines()

        for line_idx in range(len(lines)):
            if lines[line_idx].startswith('@reroute'):
                signatures[module_name].append(lines[line_idx+1])

    # -- We can now iterate the files we need to generate
    # -- in the host location - so lets start by making the
    # -- directory.
    new_dir = os.path.join(
        _core.HOST_DIR,
        host_name,
    )

    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    # -- We now need to build up the file and add all the functions
    # -- which require re-implementing
    for module_name in signatures:

        # -- Define the absolute path of the file we need to
        # -- create
        filepath = os.path.join(
            new_dir,
            module_name + '.py',
        )

        with open(filepath, 'w') as f:

            # -- Add the import line once
            f.write('import crosswalk\n\n')

            # -- Write out all the signatures
            for signature in signatures[module_name]:
                f.write('\n' + signature)

                if 'class' in signature:
                    f.write('\tpass')
                else:
                    f.write('\treturn None\n\n')

    return True
