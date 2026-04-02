import random

class PerlinNoise:
    def __init__(self, seed=None):
        local_rng = random.Random(seed)
        random.seed(seed)

        self.p = list(range(256))
        local_rng.shuffle(self.p)
        self.p = self.p * 2

    def fade(self, t):
        """S-кривая"""
        return 6*t**5 - 15*t**4 + 10*t**3

    def lerp(self, t, a, b):
        return a + t * (b - a)

    def grad(self, hash_code, x, y):
        h = hash_code & 7
        if h == 0: return  x + y
        if h == 1: return -x + y
        if h == 2: return  x - y
        if h == 3: return -x - y
        if h == 4: return  x
        if h == 5: return -x
        if h == 6: return  y
        if h == 7: return -y
        return 0

    def noise(self, x, y):
        xi = int(x) & 255
        yi = int(y) & 255
        
        xf = x - int(x)
        yf = y - int(y)
        
        u = self.fade(xf)
        v = self.fade(yf)
        
        p = self.p
        aa = p[p[xi] + yi]
        ab = p[p[xi] + yi + 1]
        ba = p[p[xi + 1] + yi]
        bb = p[p[xi + 1] + yi + 1]
        
        x1 = self.lerp(u, self.grad(aa, xf, yf), self.grad(ba, xf - 1, yf))
        x2 = self.lerp(u, self.grad(ab, xf, yf - 1), self.grad(bb, xf - 1, yf - 1))
        
        return self.lerp(v, x1, x2)
    

class Pathfinder:
    def __init__(self, game_map):
        self.game_map = game_map

    def get_dist(self, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    def find_path(self, start_x, start_y, target_x, target_y):
        to_visit = [(start_x, start_y)]
        
        came_from = {}
        
        cost_so_far = {(start_x, start_y): 0}

        while len(to_visit) > 0:
            current = to_visit[0]
            best_index = 0
            
            for i in range(len(to_visit)):
                node = to_visit[i]
                current_f = cost_so_far[current] + self.get_dist(current[0], current[1], target_x, target_y)
                node_f = cost_so_far[node] + self.get_dist(node[0], node[1], target_x, target_y)
                
                if node_f < current_f:
                    current = node
                    best_index = i
            
            if current[0] == target_x and current[1] == target_y:
                return self.reconstruct(came_from, current)

            to_visit.pop(best_index)

            curr_x, curr_y = current
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = curr_x + dx, curr_y + dy

                if 0 <= nx < self.game_map.width and 0 <= ny < self.game_map.height:
                    
                    idx = self.game_map.get_index(nx, ny)
                    is_rock = self.game_map.tile[idx] == self.game_map.defs.tiles_str_to_int["rock_granite"]
                    is_tree = self.game_map.objects[idx] == self.game_map.defs.obj_str_to_int["tree"]
                    
                    if not is_rock and not is_tree:
                        new_cost = cost_so_far[current] + 1
                        
                        if (nx, ny) not in cost_so_far or new_cost < cost_so_far[(nx, ny)]:
                            cost_so_far[(nx, ny)] = new_cost
                            came_from[(nx, ny)] = current
                            to_visit.append((nx, ny))
        
        return None

    def reconstruct(self, came_from, current):
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path