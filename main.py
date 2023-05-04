import time

import model
import view
import controller

while True:
    time.sleep(1 / 60)
    controller.p()
    view.view1()
    model.move_vrag()
