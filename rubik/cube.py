
# NOTES:
#    __init__(self [,...])          instance = MyClass(arg1, arg2)    called on instance creation
#    __getitem__(self, key)         self[key]                         accessing an item using an index
#    __setitem__(self, key, val)    self[key] = val                   assigning to an item using an index
#    __str__(self)                  str()                             produce human readable output 
#    __repr__(self)                 repr()                            produce machine readable output
#
#    a leading underscore is used to indicate a private method/attribute
#    unused loop variables can be replaced with an underscore
#    : str is a parameter annotation
#    -> is a return value annotation

FACE_NAMES = ('front', 'right', 'back', 'left', 'up', 'down')
OPERATIONS = {name[0]: name for name in FACE_NAMES}
ADJACENT_EDGES = {
    FACE_NAMES[0]: ((42, 43, 44), (9, 12, 15), (47, 46, 45), (35, 32, 29)),
    FACE_NAMES[1]: ((44, 41, 38), (18, 21, 24), (53, 50, 47), (8, 5, 2)),
    FACE_NAMES[2]: ((38, 37, 36), (27, 30, 33), (51, 52, 53), (17, 14, 11)),
    FACE_NAMES[3]: ((36, 39, 42), (0, 3, 6), (45, 48, 51), (26, 23, 20)),
    FACE_NAMES[4]: ((20, 19, 18), (11, 10, 9), (2, 1, 0), (29, 28, 27)),
    FACE_NAMES[5]: ((6, 7, 8), (15, 16, 17), (24, 25, 26), (33, 34, 35)),
}

class Cube:
    
    def __init__(self, cube_str):
        self.cube_str = cube_str
        self.faces = {
            face: [
                [cube_str[offset + 0], cube_str[offset + 1], cube_str[offset + 2]],
                [cube_str[offset + 3], cube_str[offset + 4], cube_str[offset + 5]],
                [cube_str[offset + 6], cube_str[offset + 7], cube_str[offset + 8]],
            ]
            for face, offset in zip(FACE_NAMES, (0, 9, 18, 27, 36, 45))
        }
    
    def __getitem__(self, key):
        return self.faces[FACE_NAMES[key // 9]][key % 9 // 3][key % 3]

    def __setitem__(self, key, value):
        self.faces[FACE_NAMES[key // 9]][key % 9 // 3][key % 3] = value
    
    def __str__(self):
        result = ''.join(
            f'{f[0][0]}{f[0][1]}{f[0][2]}'
            for f in (self.faces[face] for face in FACE_NAMES)
        )
        return result
    
    def __repr__(self):
        result = '\n'.join(
            face + '\n' + '\n'.join(', '.join(row) for row in self.faces[face]) + '\n' for face in FACE_NAMES
        )
        return result
    
    def rotate(self, rotation: str) -> None:
        # upper case - clockwise, lower case - counterclockwise
        turn_cw = rotation.isupper()
        self._rotate_face(OPERATIONS[rotation.lower()], turn_cw)
        self._rotate_edges(OPERATIONS[rotation.lower()], turn_cw)
    
    def _rotate_face(self, face_name: str, turn_cw: bool):
        offset = FACE_NAMES.index(face_name) * 9
        for x in range(0, 1):
            for y in range(x, 2 - x):
                temp = self[offset + (x * 3 + y)]
                if turn_cw == True:
                    self[offset + (x * 3 + y)] = self[offset + ((2 - y) * 3 + x)]
                    self[offset + ((2 - y) * 3 + x)] = self[offset + ((2 - x) * 3 + (2 - y))]
                    self[offset + ((2 - x) * 3 + (2 - y))] = self[offset + (y * 3 + (2 - x))]
                    self[offset + (y * 3 + (2 - x))] = temp
                else:
                    self[offset + (x * 3 + y)] = self[offset + (y * 3 + (2 - x))]
                    self[offset + (y * 3 + (2 - x))] = self[offset + ((2 - x) * 3 + (2 - y))]
                    self[offset + ((2 - x) * 3 + (2 - y))] = self[offset + ((2 - y) * 3 + x)]
                    self[offset + ((2 - y) * 3 + x)] = temp
                    
    def _rotate_edges(self, face_name: str, turn_cw: bool):
        for a, b, c, d in zip(*ADJACENT_EDGES[face_name]):
            temp = self[a]
            if turn_cw:
                self[a] = self[d]
                self[d] = self[c]
                self[c] = self[b]
                self[b] = temp
            else:
                self[a] = self[b]
                self[b] = self[c]
                self[c] = self[d]
                self[d] = temp
    
# testing
c = Cube('gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy')
print(c.__str__())
#print(c.__repr__())


    