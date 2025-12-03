Functions that could easily be promoted to APIs

* `pose_bones()`
* `get_pose_bone_by_name()`
* `get_active_armature()`
* `get_active_object()`

Plus the constant `REST_POSE`.

Though, as mentioned in [Future Plan](https://github.com/endersaka/bvh-reader-2/wiki/Future-Plan) line [326](https://github.com/endersaka/bvh-reader-2/blob/068df0e8aa07dc042bfca1302ec01e2c982c54c6/blender/script/goofy_importer.py#L326) ([305](https://github.com/endersaka/bvh-reader-2/blob/1f9fc27b604e4df12575fdb3a88fdfea4b51289c/blender/script/goofy_importer.py#L305) in `main` branch) can be replaced by something like:

```python
bone_rest_pose_data = armature_data.bones.get(segment_name)
```

Removing the need to use `REST_POSE` at all.
