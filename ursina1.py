from ursina import *
screen= Ursina()
test1=Entity(model="StarSparrow03", rotation=(170,38,48), texture="StarSparrow_Emissive", postion=(0,100,0), scale=(1,1,1))
def update():
    if held_keys['w']:
        test1.y+=5*time.dt
    elif held_keys['s']:
        test1.y-= 5*time.dt
    elif held_keys['a']:
        test1.x-= 5*time.dt
    elif held_keys['d']:
        test1.x+= 5*time.dt
    elif held_keys['i']:
        test1.z-=5*time.dt
    elif held_keys['k']:
        test1.z+=5*time.dt
    elif held_keys['right arrow']:
        test1.rotation_y-=30*time.dt
    elif held_keys['left arrow']:
        test1.rotation_y+=30*time.dt
    elif held_keys['up arrow']:
        test1.rotation_x-=30*time.dt
    elif held_keys['down arrow']:
        test1.rotation_x+=30*time.dt
screen.run()
