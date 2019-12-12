import unittest
import model

class TestLevel(unittest.TestCase):

    def test_mario_initial_position(self):
        level = model.Level(None, 10, 10, 9, 0)
        self.assertEqual(level.mario.l, 9)
        self.assertEqual(level.mario.c, 0)

    def test_mario_move_right(self):
        level = model.Level(None, 10, 10, 9, 0)
        level.move_mario(1)
        self.assertEqual(level.mario.c, 1)
    
    def test_mario_move_left(self):
        level = model.Level(None, 10, 10, 9, 2)
        level.move_mario(-1)
        self.assertEqual(level.mario.c, 1)

    def test_mario_cannot_move_left_at_leftmost_point(self):
        level = model.Level(None, 10, 10, 9, 0)
        level.move_mario(-1)
        self.assertEqual(level.mario.c, 0)

    def test_mario_can_jump(self):
        level = model.Level(None, 10, 10, 9, 0)
        level.jump_mario()
        self.assertTrue(level.mario.vl > 0)

    def test_if_mario_jump_mario_move_up(self):
        level = model.Level(None, 10, 10, 9, 0)
        level.jump_mario()
        level.update()
        self.assertEqual(level.mario.l, 7)
    
    def test_if_mario_jump_below_a_platform_mario_doesnot_move_above_the_platform(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
