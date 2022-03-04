import unittest
from rubik.cube import Cube

class CubeTest(unittest.TestCase):

    def test_cube_01_cuberead(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        self.assertEqual(cube_str, str(cube))
        
    def test_cube_02_cuberotate_F(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('F')
        self.assertEqual(str(cube), 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy')
        
    def test_cube_03_cuberotate_f(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('f')
        self.assertEqual(str(cube), 'gggggggggyrryrryrrbbbbbbbbboowoowoowwwwwwwrrroooyyyyyy')
        
    def test_cube_04_cuberotate_R(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('R')
        self.assertEqual(str(cube), 'ggyggyggyrrrrrrrrrwbbwbbwbbooooooooowwgwwgwwgyybyybyyb')
    
    #@unittest.skip    
    def test_cube_05_cuberotate_r(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('r')
        self.assertEqual(str(cube), 'ggwggwggwrrrrrrrrrybbybbybbooooooooowwbwwbwwbyygyygyyg')
        
    #@unittest.skip    
    def test_cube_06_cuberotate_B(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('B')
        self.assertEqual(str(cube), 'gggggggggrryrryrrybbbbbbbbbwoowoowoorrrwwwwwwyyyyyyooo')
        
    #@unittest.skip    
    def test_cube_07_cuberotate_b(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('b')
        self.assertEqual(str(cube), 'gggggggggrrwrrwrrwbbbbbbbbbyooyooyooooowwwwwwyyyyyyrrr')
        
    #@unittest.skip    
    def test_cube_08_cuberotate_L(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('L')
        self.assertEqual(str(cube), 'wggwggwggrrrrrrrrrbbybbybbyooooooooobwwbwwbwwgyygyygyy')
        
    #@unittest.skip    
    def test_cube_09_cuberotate_l(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('l')
        self.assertEqual(str(cube), 'yggyggyggrrrrrrrrrbbwbbwbbwooooooooogwwgwwgwwbyybyybyy')
        
    #@unittest.skip    
    def test_cube_10_cuberotate_U(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('U')
        self.assertEqual(str(cube), 'rrrggggggbbbrrrrrrooobbbbbbgggoooooowwwwwwwwwyyyyyyyyy')
        
    #@unittest.skip    
    def test_cube_11_cuberotate_u(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('u')
        self.assertEqual(str(cube), 'ooogggggggggrrrrrrrrrbbbbbbbbboooooowwwwwwwwwyyyyyyyyy')
        
    @unittest.skip    
    def test_cube_12_cuberotate_D(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('D')
        self.assertEqual(str(cube), '')
        
    @unittest.skip    
    def test_cube_13_cuberotate_d(self):
        cube_str = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        cube = Cube(cube_str)
        cube.rotate('d')
        self.assertEqual(str(cube), '')
        