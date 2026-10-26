try:
    from netbox.object_actions import (
        AddObject,
        BulkDelete,
        BulkEdit,
        BulkExport,
        BulkImport,
        ObjectAction,
    )
except ImportError:
    class ObjectAction:
        name = ''
        permissions_required = set()
        multi = False

    class AddObject(ObjectAction):
        name = 'add'
        permissions_required = {'add'}

    class BulkDelete(ObjectAction):
        name = 'bulk_delete'
        permissions_required = {'delete'}
        multi = True

    class BulkEdit(ObjectAction):
        name = 'bulk_edit'
        permissions_required = {'change'}
        multi = True

    class BulkExport(ObjectAction):
        name = 'export'
        permissions_required = {'view'}
        multi = True

    class BulkImport(ObjectAction):
        name = 'bulk_import'
        permissions_required = {'add'}


try:
    from netbox.object_actions import ObjectAction as NetBoxObjectAction
except ImportError:
    NetBoxObjectAction = None


def actions(*action_classes):
    if NetBoxObjectAction is not None:
        return action_classes
    return {
        action.name: action.permissions_required
        for action in action_classes
    }


class PermissionOnlyBulkAction(ObjectAction):
    multi = True

    if NetBoxObjectAction is not None:
        @classmethod
        def render(cls, context, obj, **kwargs):
            return ''


class BulkRemoveTenant(PermissionOnlyBulkAction):
    name = 'bulk_remove_tenant'
    permissions_required = {'change'}
