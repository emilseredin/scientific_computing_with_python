import copy
import random


class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, num in balls.items():
            # add balls to contents[] num times
            for i in range(num):
                self.contents.append(color)

      
    def draw(self, num_of_balls):
        if num_of_balls > len(self.contents):
            return self.contents
        sample = []
        for draw in range(num_of_balls):
            random_index = random.randint(0, len(self.contents)-1)
            sample.append(self.contents[random_index])
            self.contents.pop(random_index)
             
        return sample
 
 
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0 
    for experiment in range(num_experiments):
        # start each experiment with "fresh" hat
        hat_copy = copy.deepcopy(hat)
        draw = hat_copy.draw(num_balls_drawn)
        draw_count = {}
        matched_colors = 0
        # count drawn balls and save this in a dictionary
        for ball in draw:
            if ball not in draw_count:
                draw_count[ball] = 0 
            draw_count[ball] += 1
        for color, num in expected_balls.items():
            if color in draw_count:
                if draw_count[color] >= num:
                    matched_colors += 1
        # check whether the experiment was successful
        if matched_colors == len(expected_balls):
            count += 1
    return count / num_experiments
