import unittest
import model

class TestLevel(unittest.TestCase):

    def test_mario_initial_position(self):
        level = model.Level(None, 10, 10, 8, 0)
        level.set_platform(9,0,3)
        self.assertEqual(level.mario.l, 8)
        self.assertEqual(level.mario.c, 0)

    def test_mario_move_right(self):
        level = model.Level(None, 10, 10, 8, 0)
        level.set_platform(9,0,3)
        level.move_mario(1)
        self.assertEqual(level.mario.c, 1)
    
    def test_mario_move_left(self):
        level = model.Level(None, 10, 10, 8, 2)
        level.set_platform(9,0,3)
        level.move_mario(-1)
        self.assertEqual(level.mario.c, 1)

    def test_mario_cannot_move_left_at_leftmost_point(self):
        level = model.Level(None, 10, 10, 8, 0)
        level.set_platform(9,0,3)
        level.move_mario(-1)
        self.assertEqual(level.mario.c, 0)

    def test_mario_cannot_move_right_at_rightmost_point(self):
        level = model.Level(None, 10, 10, 8, 9)
        level.set_platform(9,0,10)
        level.move_mario(1)
        self.assertEqual(level.mario.c, 9)

    def test_mario_can_jump(self):
        level = model.Level(None, 10, 10, 8, 0)
        level.set_platform(9,0,3)
        level.jump_mario()
        self.assertTrue(level.mario.vl > 0)

    def test_if_mario_jump_mario_move_up(self):
        level = model.Level(None, 10, 10, 8, 0)
        level.set_platform(9,0,3)
        level.jump_mario()
        level.update()
        self.assertEqual(level.mario.l, 6)
    
    def test_if_mario_jump_below_a_platform_mario_doesnot_move_above_the_platform(self):

        level = model.Level(None, 10, 10, 8, 0)
        level.set_platform(7, 0, 2)
        level.set_platform(9,0,3)
        level.jump_mario()
        level.update()

        self.assertEqual(level.mario.l, 8)

    def test_if_mario_is_on_a_spike_mario_dies(self):
        
        level = model.Level(None, 10, 10, 8, 0)
        level.set_platform(9,0,3)
        level.set_spikes(9,3,2)
        level.move_mario(4)
        self.assertEqual(level.mario.c,0)
        self.assertEqual(level.mario.l, 8)

    def test_if_mario_jump_below_a_spike_mario_dies(self):

        level = model.Level(None, 10, 10, 8, 0)
        level.set_spikes(7, 0, 2)
        level.set_platform(9,0,3)
        level.move_mario(1)
        level.jump_mario()
        level.update()
        self.assertEqual(level.mario.c,0)
        self.assertEqual(level.mario.l, 8)

    def test_if_mario_jump_while_jumpin_nothing_happens(self):
        level = model.Level(None, 10, 10, 8, 0)
        level.set_platform(9,0,3)
        level.jump_mario()
        level.update()
        level.jump_mario()
        self.assertEqual(level.mario.vl,1)
        level.update()
        level.jump_mario()
        self.assertEqual(level.mario.vl,0)

    def test_if_mario_eat_mushroom_he_grows(self):
        level = model.Level(None, 10, 10, 8, 0)
        level.set_platform(9,0,3)
        level.set_items(8,2,model.MUSHROOM)
        level.move_mario(2)
        self.assertEqual(level.mario.size,2)
    
    def test_if_mario_eat_mushroom_while_tall_nothing_happens(self):
        level = model.Level(None, 10, 10, 8, 0)
        level.set_platform(9,0,6)
        level.set_items(8,2,model.MUSHROOM)
        level.move_mario(2)
        level.set_items(8,3,model.MUSHROOM)
        level.move_mario(1)
        self.assertEqual(level.mario.size,2)

    def test_if_big_mario_falls_he_become_little(self):
        level = model.Level(None, 10, 10, 8, 0)
        level.set_platform(9, 0, 3)
        level.set_spikes(9, 3, 2)
        level.set_items(8, 2, model.MUSHROOM)
        level.move_mario(2)
        level.move_mario(2)

        self.assertEqual(level.mario.c, 4)
        self.assertEqual(level.mario.l, 8)
        self.assertEqual(level.mario.size, 1)
        self.assertTrue(level.mario.cpt > 0)







if __name__ == '__main__':
    unittest.main()
