from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()

x_dim, y_dim = m.screen_size()

m.click(int(x_dim/2), int(y_dim/2), 1,1)


f = 'fsefsef sefs fsef sef fse'

for i in f:
    k.tap_key(i,n=1,interval=0.1)