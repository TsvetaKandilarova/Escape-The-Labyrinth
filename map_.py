class Map:
    # map_'s constructor. it loads a map
    # from a simple text file with a path 'path_to_map'
    def __init__(self, path_to_map):
        file_ = open(path_to_map, "r")
        self.map_ = self.map_to_array(file_.read())
        file_.close()

        self.height = len(self.map_)
        self.width = len(self.map_[0])

    # returns an array (indeed a matrix)
    # formed from the string 'map_'
    @staticmethod
    def map_to_array(map_):
        return [list(row) for row in map_.splitlines()]

    # returns our map's current state
    def map_state(self):
        return '\n'.join(''.join(row) for row in self.map_)

    # spawns our hero on the left corner of the map
    def spawn(self):
        if self.map_[0][0] != 'S':
            return False
        self.map_[0][0] = 'H'
        return True

    # returns true if the field 'position'
    # is on the map, else false
    def on_map(self, position):
        return position[0] in range(0, self.height) and position[1] in range(
            0, self.width)

    # returns true if the field 'position' is an obstacle ('#')
    def is_obstacle(self, position):
        return self.map_[position[0]][position[1]] == '#'

    # returns true if the field 'position' is a gate to the next level
    def is_gate(self, position):
        return self.map_[position[0]][position[1]] == 'G'

    # returns true if the field 'position' contains an item
    def is_item(self, position):
        return self.map_[position[0]][position[1]] == 'I'

    # returns true if there's a enemy on field 'position'
    def is_enemy(self, position):
        return self.map_[position[0]][position[1]] == 'E'

    # returns true if there's a boss on field 'position'
    def is_boss(self, position):
        return self.map_[position[0]][position[1]] == 'B'

    # moves our hero from 'old_position' to 'new_position'
    def update_map(self, old_position, new_position):
        self.map_[old_position[0]][old_position[1]] = '.'
        self.map_[new_position[0]][new_position[1]] = 'H'

    # returns all fields visible from our hero
    # (i.e. all fields next to her) as an array
    @staticmethod
    def _visible_positions(from_position):
        positions = [(-1, -1), (-1, 0), (-1, 1),
                     (0, -1), (0, 0), (0, 1),
                     (1, -1), (1, 0), (1, 1)]
        # the coordinates of visible fields starting from current field
        sum_tuples = lambda x, y: (x[0] + y[0], x[1] + y[1])

        return [sum_tuples(x, from_position) for x in positions]

    # returns all fields visible from our here, but
    # in a printable format (i.e. a string)
    def show_map(self, from_position):
        positions = self._visible_positions(from_position)
        show = lambda x: '#' if not self.on_map(x) else self.map_[x[0]][x[1]]

        visible_map = [show(x) for x in positions]
        visible_map = visible_map[0:3] + ['\n'] + visible_map[3:6] + [
            '\n'] + visible_map[6:9]

        return ''.join(visible_map)
