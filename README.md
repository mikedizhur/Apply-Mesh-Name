# Apply-Mesh-Name

Blender addon adding a function to rename mesh names to the object name.

## Usage

Simply use `Ctrl + A` shortcut to bring up the Apply menu
(unless you changed the binding) or go to
`Object > Apply` menu in 3D Viewport and select "Apply Mesh Name"

### Options

Prioritize short names:

- With the option set, the addon will use the shortest name found when renaming meshes.
- Only useful for objects with linked mesh data.
- By default Blender does not sort objects in selection by name,
so if you renamed Object to Object.002 and Object.001 to Object,
both of which use the same mesh data,
the name will **probably** be set to Object.001 by default.

Purge unused data:

- Purges unused data, which might prevent you from renaming mesh data.
- Let's say you have Object and you duplicate it to Object.001.
You then modify Object.001 and delete Object. You rename Object.001 to Object
and try to Apply Mesh Name. You check and see that the mesh is now named Object.002.
Unused data from Object is using mesh name Object, which doesn't let the addon
rename the mesh to the same name.
- This option purges the unused data, allowing you to successfully rename the mesh.
Equivalent to `File > Clean Up > Purge Unused Data [+] Local Data-blocks`.
