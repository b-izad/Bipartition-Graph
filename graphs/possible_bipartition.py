# Can be used for BFS
from collections import deque 

def possible_bipartition(dislikes):
  
    # Can be used for BFS
    from collections import deque 


  
    if len(dislikes) == 0:
        return True

    checked = set()

    for each_dog in dislikes.keys():

        colored_dogs = {each_dog: 'red'}  # visited
        queue = [each_dog]

        while queue:
            
            dog = queue.pop(0)  # current dog
            checked.add(dog)

            color = 'red' if colored_dogs[dog] == 'blue' else 'blue'

            for neighbor in dislikes[dog]:
                if neighbor not in colored_dogs:
                    colored_dogs[neighbor] = color
                    queue.append(neighbor)
                elif colored_dogs[neighbor] != color:
                    return False

    return True

    

