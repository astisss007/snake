import snake_class as scl
import time as tm
check = False
pole = scl.Field()
#pole.play()
snake = [scl.Snake('black', 'gray', 'square', i*50, i*50, 4) for i in range(1)]
food = scl.Food('red', 'square')
food.food_pos()
pole.listen_p(snake)
print(snake)
while True:
    for i in snake:
        if i.dtp():
            i.move()
        else:
            check = True
            pole.end_game()
        if i.check_food(food):
            food.food_pos()
            i.more('black', 'square')
    pole.reload()
    tm.sleep(0.2)
    if check:
        break
        
    
