bl_info = {
    "name": "Apply Mesh Name",
    "author": "Mike Dizhur",
    "version": (0, 6),
    "blender": (5, 1, 3),
    "location": "View3D > Object > Apply",
    "description": "Rename mesh to object name.",
    "category": "Object",
}

import bpy
from bpy.types import Operator


def smart_rename(s: str, names: set) -> str:
    return s


class OBJECT_OT_applyname(Operator):
    bl_label = "Apply Mesh Name"
    bl_idname = "object.apply_mesh_name"
    bl_description = "Renames mesh to object name"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {'REGISTER', 'UNDO'}

    prefer_short: bpy.props.BoolProperty(
        name="Prioritize short names",
        default=False,
        description="If mesh is linked, chooses the shortest name.",
        )

    purge_data: bpy.props.BoolProperty(
        name="Purge unused data",
        default=False,
        description="Unused data may prevent the plugin from changing"
                    " the name, appending numeration."
                    " Only purges unused data blocks.",
        )

    def execute(self, context):
        if self.purge_data:
            bpy.ops.outliner.orphans_purge(do_local_ids=True,
                                           do_linked_ids=False,
                                           do_recursive=False)
        names = set()
        for obj in context.selected_objects:
            if obj.type == 'MESH':
                if (obj.data.name not in names
                        or (len(obj.data.name) > len(obj.name)) * self.prefer_short):
                    obj.data.name = obj.name
                    names.add(obj.data.name)
                else:
                    self.report({"WARNING"},
                                f"Skipping renaming {obj.name},"
                                " probably linked mesh.")
                    continue
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(OBJECT_OT_applyname.bl_idname)


def register():
    bpy.utils.register_class(OBJECT_OT_applyname)
    bpy.types.VIEW3D_MT_object_apply.append(menu_func)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_applyname)
    bpy.types.VIEW3D_MT_object_apply.remove(menu_func)


if __name__ == "__main__":
    register()
