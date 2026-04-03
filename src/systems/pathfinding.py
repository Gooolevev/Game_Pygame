import heapq

class Pathfinder:
    def __init__(self, game_map):
        self.game_map = game_map
        self.ROCK_ID = self.game_map.defs.tiles_str_to_int["rock_granite"]
        self.TREE_ID = self.game_map.defs.obj_str_to_int["tree"]

    def get_distance(self, x1, x2, y1, y2):
        return abs(x1 - x2) + abs(y1 - y2)
    
    def is_walkable(self,x,y):
        if not (0 <= x < self.game_map.width and 0 <= y < self.game_map.height):
            return False
        
        idx = self.game_map.get_index(x, y)

        if self.game_map.tile[idx] == self.ROCK_ID:
            return False
        if self.game_map.objects[idx] == self.TREE_ID:
            return False
        
        return True
    
    def find_path(self,start_x, start_y, target_x, target_y):
        start = (start_x, start_y)
        goal = (target_x, target_y)

        to_visit = [(0, start)]
        
        came_from = {}
        current_cost = {start: 0}

        while to_visit:
            _, current = heapq.heappop(to_visit)

            if current == goal:
                return self.reconstruct(came_from, current)
            
            curr_x, curr_y = current

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_step = (curr_x + dx, curr_y + dy)

                if self.is_walkable(*next_step):
                    new_cost = current_cost[current] + 1

                    if next_step not in current_cost or new_cost < current_cost[next_step]:
                        current_cost[next_step] = new_cost
                        
                        priority = new_cost + self.get_distance(next_step[0], next_step[1], target_x, target_y)
                        heapq.heappush(to_visit, (priority, next_step))
                        came_from[next_step] = current

        return None


    def reconstruct(self, came_from, current):
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        return path[::-1]
