from ursina import *


def update():
	firstEntity.rotation_y +=100 * time.dt
	firstEntity.position += firstEntity.forward * time.dt

app = Ursina()

firstEntity = Entity(model = 'cube',
	color= color.rgb(255,0,0),
	texture = 'brick',

	position = (0,0,0),
	rotation = (0,0,0),

	scale = 2.5,
	)

EditorCamera()

app.run()
