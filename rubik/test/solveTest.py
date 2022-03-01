import unittest
import rubik.solve as solve

class SolveTest(unittest.TestCase):
    
    def test_solve_01_emptycube(self):
        parms = {'op': 'solve'}
        result = solve._solve(parms)
        self.assertIn('status', result)
        status = result.get('status')
        self.assertNotEqual('ok', status)
    
    @unittest.skip('cube model incomplete')
    def test_solve_02_badcube(self):
        pass
    
    @unittest.skip('cube rotate incomplete')
    def test_solve_03_rotate_notstring(self):
        pass
    
    @unittest.skip('cube rotate incomplete')
    def test_solve_04_rotate_notletter(self):
        pass
    
    @unittest.skip('cube rotate incomplete')
    def test_solve_05_rotate_empty(self):
        pass
    
    @unittest.skip('cube rotate incomplete')
    def test_solve_06_rotate_missing(self):
        parms = {'op':'solve',
                'rotate':'',
                'cube':'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'}
    
    @unittest.skip('cube rotate incomplete')
    def test_solve_07_rotate_invalidchars(self):
        pass
    
    @unittest.skip('cube rotate incomplete')
    def test_solve_08_rotate_valid(self):
        pass
        