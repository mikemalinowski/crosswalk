import os
import pymel.core as pm


# ------------------------------------------------------------------------------
def version():
	return pm.about(version=True)


# ------------------------------------------------------------------------------
def refresh():
	pm.refresh()


# ------------------------------------------------------------------------------
def load(filename, operation='open', force=False):
	imported_nodes = list()

	if operation == 'open':
		pm.mel.file(
			filename,
			open=True,
			force=force,
		)

	elif operation == 'import':
		imported_nodes = pm.mel.file(
			filename,
			i=True,
			ignoreVersion=True,
			returnNewNodes=True,
		)

	elif operation == 'reference':
		imported_nodes = pm.mel.file(
			filename,
			reference=True,
			ignoreVersion=True,
			gl=True,
			mergeNamespacesOnClash=False,
			namespace=os.path.basename(filename).split('.')[0],
			options='v=0;',
			returnNewNodes=True,
		)

	return imported_nodes


# ------------------------------------------------------------------------------
def new(force=False):
	pm.newFile(force=force)


# ------------------------------------------------------------------------------
def save(filename=None):
	if filename:
		pm.saveAs(filename)

	else:
		pm.saveFile()


# ------------------------------------------------------------------------------
def filepath():
	return pm.sceneName()


# ------------------------------------------------------------------------------
def is_silent():
	return pm.about(batch=True)


# ------------------------------------------------------------------------------
def undo():
	pm.undo()


# ------------------------------------------------------------------------------
def redo():
	pm.redo()

