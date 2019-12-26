def fill():
    map = {'C':'C#', 'C#':'D', 'D':'D#', 'D#':'E', 'E':'F', 'F':'F#', 'F#':'G', 'G':'G#', 'G#':'A', 'A':'A#', 'A#':'B', 'B':'C'}
    major_seeds = [('C', ['C', 'E', 'G']), ('C', ['C', 'E', 'G', 'B']), ('C', ['C', 'E', 'G', 'B', 'D']), ('C', ['C', 'E', 'G' ,'B', 'D', 'F']), ('C', ['C', 'E', 'G', 'B', 'D', 'F', 'A'])]
    minor_seeds = [('C', ['C', 'D#', 'G']), ('C', ['C', 'D#', 'G', 'A#']), ('C', ['C', 'D#', 'G', 'A#', 'D']), ('C', ['C', 'D#', 'G', 'A#', 'D', 'F']), ('C', ['C', 'D#', 'G', 'A#', 'D', 'F', 'A'])]
    
###################################################################
# Major
###################################################################

    for seed in major_seeds:
        if major_seeds.index(seed) == 0:
            current_key = seed[0]
            current_keys = seed[1]
            print(current_key + 'M ' + ' '.join(current_keys))
            for x in range(len(map)):
                next_key = map.get(current_key)
                new_keys = list()
                for l in current_keys:
                    new_keys.append(map.get(l))
                current_key = next_key
                current_keys = new_keys
                print(current_key + 'M ' + ' '.join(current_keys))
        elif major_seeds.index(seed) == 1:
            current_key = seed[0]
            current_keys = seed[1]
            print(current_key + 'M7 ' + ' '.join(current_keys))
            for x in range(len(map)):
                next_key = map.get(current_key)
                new_keys = list()
                for l in current_keys:
                    new_keys.append(map.get(l))
                current_key = next_key
                current_keys = new_keys
                print(current_key + 'M7 ' + ' '.join(current_keys))
        elif major_seeds.index(seed) == 2:
            current_key = seed[0]
            current_keys = seed[1]
            print(current_key + 'M9 ' + ' '.join(current_keys))
            for x in range(len(map)):
                next_key = map.get(current_key)
                new_keys = list()
                for l in current_keys:
                    new_keys.append(map.get(l))
                current_key = next_key
                current_keys = new_keys
                print(current_key + 'M9 ' + ' '.join(current_keys))
        elif major_seeds.index(seed) == 3:
            current_key = seed[0]
            current_keys = seed[1]
            print(current_key + 'M11 ' + ' '.join(current_keys))
            for x in range(len(map)):
                next_key = map.get(current_key)
                new_keys = list()
                for l in current_keys:
                    new_keys.append(map.get(l))
                current_key = next_key
                current_keys = new_keys
                print(current_key + 'M11 ' + ' '.join(current_keys))
        elif major_seeds.index(seed) == 4:
            current_key = seed[0]
            current_keys = seed[1]
            print(current_key + 'M13 ' + ' '.join(current_keys))
            for x in range(len(map)):
                next_key = map.get(current_key)
                new_keys = list()
                for l in current_keys:
                    new_keys.append(map.get(l))
                current_key = next_key
                current_keys = new_keys
                print(current_key + 'M13 ' + ' '.join(current_keys))

    ###################################################################
    # Minor
    ###################################################################

    for seed in minor_seeds:
        if minor_seeds.index(seed) == 0:
            current_key = seed[0]
            current_keys = seed[1]
            print(current_key + 'm ' + ' '.join(current_keys))
            for x in range(len(map)):
                next_key = map.get(current_key)
                new_keys = list()
                for l in current_keys:
                    new_keys.append(map.get(l))
                current_key = next_key
                current_keys = new_keys
                print(current_key + 'm ' + ' '.join(current_keys))
        elif minor_seeds.index(seed) == 1:
            current_key = seed[0]
            current_keys = seed[1]
            print(current_key + 'm7 ' + ' '.join(current_keys))
            for x in range(len(map)):
                next_key = map.get(current_key)
                new_keys = list()
                for l in current_keys:
                    new_keys.append(map.get(l))
                current_key = next_key
                current_keys = new_keys
                print(current_key + 'm7 ' + ' '.join(current_keys))
        elif minor_seeds.index(seed) == 2:
            current_key = seed[0]
            current_keys = seed[1]
            print(current_key + 'm9 ' + ' '.join(current_keys))
            for x in range(len(map)):
                next_key = map.get(current_key)
                new_keys = list()
                for l in current_keys:
                    new_keys.append(map.get(l))
                current_key = next_key
                current_keys = new_keys
                print(current_key + 'm9 ' + ' '.join(current_keys))
        elif minor_seeds.index(seed) == 3:
            current_key = seed[0]
            current_keys = seed[1]
            print(current_key + 'm11 ' + ' '.join(current_keys))
            for x in range(len(map)):
                next_key = map.get(current_key)
                new_keys = list()
                for l in current_keys:
                    new_keys.append(map.get(l))
                current_key = next_key
                current_keys = new_keys
                print(current_key + 'm11 ' + ' '.join(current_keys))
        elif minor_seeds.index(seed) == 4:
            current_key = seed[0]
            current_keys = seed[1]
            print(current_key + 'm13 ' + ' '.join(current_keys))
            for x in range(len(map)):
                next_key = map.get(current_key)
                new_keys = list()
                for l in current_keys:
                    new_keys.append(map.get(l))
                current_key = next_key
                current_keys = new_keys
                print(current_key + 'm13 ' + ' '.join(current_keys))

if __name__ == "__main__":
    fill()
