#coding=utf-8

def traverse_view_tree(view_tree, call_back):
    if not is_view_valid(view_tree):
        return
    call_back(view_tree)
    if "children" in view_tree:
        for child in view_tree["children"]:
            traverse_view_tree(child, call_back)

def is_view_valid(view):
    visible_to_user = view["visible-to-user"]
    if not visible_to_user:
        return False

    bounds = view["bounds"]
    rel_bounds = view["rel-bounds"]

    if (bounds[0] >= bounds[2] or bounds[1] >= bounds[3] or \
        rel_bounds[0] >= rel_bounds[2] or rel_bounds[1] >= rel_bounds[3]):
        return False

    if ((rel_bounds[2] - rel_bounds[0]) < (bounds[2] - bounds[0]) or \
        (rel_bounds[3] - rel_bounds[1]) < (bounds[3] - bounds[1])):
        return False

    return True
