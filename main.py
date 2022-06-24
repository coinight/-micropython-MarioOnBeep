from machine import PWM,Pin
import time
import _thread
beep = PWM(Pin(2),freq=50000,duty=500)
#cdefgab
s2 = [50000,262 ,294, 330 ,349 ,392 ,220 ,247 ]
s3 = [50000,523,587,659,698,784,440,494]
s4 = [50000,1044, 1175 ,1318, 1397 ,1568 ,880 ,988]
def play(level,power = 1,deltatime = 200):
    if power == 0:
        beep.freq(s2[level])
    elif power == 1:
        beep.freq(s3[level])
    elif power == 2:
        beep.freq(s4[level])
    time.sleep_ms(deltatime)
    beep.freq(50000)
def plays(l):
    for i in l:
        if len(i) == 3:
            play(i[0],i[1],i[2])
        else:
            play(i[0],i[1])
def test():
    plays([(3,2),(3,2),(0,2),(3,2),(0,2),(1,2),(3,2),(0,2),(5,2),(0,2,500)])
    plays([(1,2,600),(5,1,600),(3,1,600),(6,1,400),(7,1,400),(7,1),(6,1,400)])
    plays([(5,1),(3,2,400),(5,2),(6,2,400),(4,2),(5,2,400),(3,2,400),(1,2),(2,2),(7,1)])
    plays([(1,2,600),(5,1,600),(3,1,600),(6,1,400),(7,1,400),(7,1),(6,1,400)])
    plays([(5,1),(3,2,400),(5,2),(6,2,400),(4,2),(5,2,400),(3,2,400),(1,2),(2,2),(7,1)])
_thread.start_new_thread(test,())