from practicum import find_mcu_boards , McuBoard , PeriBoard
import time
import requests
devices = find_mcu_boards()
print(f"found {len(devices)}")

for i in devices:
    print(f"    {i}")
    
mcu = McuBoard(devices[0])
print("__________________________")
print(f"__selected {devices[0]}")
peri = PeriBoard(mcu)

peri.led_on_red()
#test = open('./data.txt','w').write("test")

#file = open('./data.txt','w')
card_place = False
send = False
while True:

    r0 = peri.reed0()          # read REED 0
    r1 = peri.reed1()          # read REED 1
    r2 = peri.reed2()          # read REED 2
    r3 = peri.reed3()          # read REED 3
    card = peri.check_card()    # check if card placed
    #print(f"{r0} {r1} {r2} {r3} => card: {card}")
    #print(card)
    if (card):
        
        send = False
        a = r0*8+r1*4+r2*2+r3
        r = requests.get(f"https://practicum-po.herokuapp.com/getHard?id={a}")
        print(r)
        #file.write(str(a))
        print(f"id: {a}")
        if not card_place: 
            peri.led_off_red()
            peri.led_on_green()
        if not card_place:
            peri.buzzer_on()
            time.sleep(0.1)
            peri.buzzer_off()
            

        card_place = True
        peri.buzzer_off()
     
        #peri.led_off_green()
        #peri.led_on_red()
    else:
        if not send: 
            r = requests.get("https://practicum-po.herokuapp.com/getHard?id=0")
            send = True
        if card_place:
            peri.led_on_red()
            peri.led_off_green()
        card_place = False
        #file.write("0")
        #print("0")
    time.sleep(0.2)

