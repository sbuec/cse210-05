from pyray import check_collision_recs

'''
NOTE This is class and file are likely to be removed!
'''

class Collision:
    '''Class that holds collision methods'''

    def player_collide_check(tail, player) -> bool:
        ''' checks for collision of player and new possible tail'''
        return check_collision_recs(
                [tail.pos_x, tail.pos_y, tail.texture.width, tail.texture.height],
                [player.pos_x, player.pos_y, player.texture.width, player.texture.height]
            )

    def tail_collide_check(tail1, tail2) -> bool:
        '''
        checks for collision between tail piece and possible tail piece

        Args:
        - tail1: tail already created
        - tail2: possible tail
        '''
        if tail2 != None:
            return check_collision_recs(
                    [tail1.pos_x, tail1.pos_y,tail1.width, tail1.height],
                    [tail2.pos_x, tail2.pos_y, tail2.width, tail2.height]
                )
        return False