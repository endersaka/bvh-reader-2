class BVHReader2:
    """
    Dummy class, for future implementation...
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.joint_hierarchy = {}
        self.motion_data = []
        self.frame_time = 0.0

    def read(self):
        """
        Bla
        """
        with open(self.file_path, 'r') as file:
            lines = file.readlines()

        self._parse_hierarchy(lines)
        self._parse_motion(lines)

    def _parse_hierarchy(self, lines):
        # Implementation for parsing the joint hierarchy from the BVH file
        pass

    def _parse_motion(self, lines):
        # Implementation for parsing the motion data from the BVH file
        pass

    def get_joint_hierarchy(self):
        return self.joint_hierarchy

    def get_motion_data(self):
        return self.motion_data

    def get_frame_time(self):
        return self.frame_time