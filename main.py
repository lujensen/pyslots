
import random

score_table = {
    '🍋': 10,
    '🍌': 15,
    '🍊': 25,
    '🍉': 30,
    '🍎': 45,
    '🍇': 55,
    '🍒': 70,
    '🚫': 100,
    '💎': 500
    }

lemon = '🍋'
banana = '🍌'
orange = '🍊'
watermelon = '🍉'
apple = '🍎'
grapes = '🍇'
cherry = '🍒'
bar = '🚫'
diamond = '💎'

def fill_slots():
    slot_chars = []
    for i in range(0,2):
        slot_chars.append(diamond)
    for i in range(0,9):
        slot_chars.append(bar)
    for i in range(0,14):
        slot_chars.append(cherry)
    for i in range(0,18):
        slot_chars.append(grapes)
    for i in range(0,22):
        slot_chars.append(apple)
    for i in range(0,26):
        slot_chars.append(watermelon)
    for i in range(0,29):
        slot_chars.append(orange)
    for i in range(0,33):
        slot_chars.append(banana)
    for i in range(0,38):
        slot_chars.append(lemon)
    random.shuffle(slot_chars)
    return slot_chars


def get_results(slot_chars):
    results = []
    for i in range(0, 3):
        row = []
        row.append(random.choice(slot_chars))
        row.append(random.choice(slot_chars))
        row.append(random.choice(slot_chars))
        results.append(row)
    return results

def print_board(results):
    for row in results:
        print(f'| {row[0]} | {row[1]} | {row[2]} |')


def calc_score(results):
    score = 0
    top = results[0]
    middle = results[1]
    bottom = results[2]
    match_val = ''
    multiplier = 1
    if (top[0] == top[1] == top[2]) and (middle[0] == middle[1] == middle[2]) and (bottom[0] == bottom[1] == bottom[2]):
        if (top[0] == diamond):
            print("JACKPOT!!!!!!")
        multiplier = 3
        match_val = top[0]
    if (top[0] == top[1] == top[2]) and (middle[0] == middle[1] == middle[2]):
        multiplier = 2
        match_val = top[0]  
    if (top[0] == top[1] == top[2]) and (bottom[0] == bottom[1] == bottom[2]):
        multiplier = 2
        match_val = top[0]
    if (middle[0] == middle[1] == middle[2]) and (bottom[0] == bottom[1] == bottom[2]):
        multiplier = 2
        match_val = middle[0]
    if (top[0] == middle[0] == bottom[0]) and (top[1] == middle[1] == bottom[1]):
        multiplier = 2 
        match_val = top[0]
    if (top[0] == middle[0] == bottom[0]) and (top[2] == middle[2] == bottom[2]):
        multiplier = 2
        match_val = top[0]
    if (top[1] == middle[1] == bottom[1]) and (top[2] == middle[2] == bottom[2]):
        multiplier = 2
        match_val = top[1]
    if (top[0] == middle[1] == bottom[2]) and (top[2] == middle[1] == bottom[0]):
        multiplier = 2
        match_val = top[0]
    if (top[0] == top[1] == top[2]):
        match_val = top[0]
    if (middle[0] == middle[1] == middle[2]):
        match_val = middle[0]
    if (bottom[0] == bottom[1] == bottom[2]):
        match_val = bottom[0]
    if (top[0] == middle[0] == bottom[0]):
        match_val = top[0]
    if (top[1] == middle[1] == bottom[1]):
        match_val = top[1]
    if (top[2] == middle[2] == bottom[2]):
        match_val = top[2]
    if (top[0] == middle[1] == bottom[2]):
        match_val = top[0]
    if (top[2] == middle[1] == bottom[0]):
        match_val = top[2]
        
    if match_val != '':
        print("YOU WIN!!!!")
        score = score_table[match_val] *3 * multiplier
        print("SCORE: ", score)
        
    else:
        print("SCORE: ", score)
        print("Please spin again.")
    

def main():
    while True:
        print("Press enter to play. Press X to quit.")
        x = input()
        if (x.lower() == "x"):
            break 
        slot_chars = fill_slots()
        results = get_results(slot_chars)
        print_board(results)
        calc_score(results)    


if __name__ == "__main__":
    main()
