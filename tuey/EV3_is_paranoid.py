
import mqtt_remote_method_calls as com
import robot_controller as robo
import ev3dev.ev3 as ev3
import time

def main():
    robot = robo.Snatch3r()
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()

    print("-----------------Computer:------------------")
    print('Starting up EV3 is Paranoid')
    print("--------------------------------------------")

    speech = 0
    btn = ev3.Button()
    robot.pixy.mode = "SIG1"
    while not robot.touch_sensor.is_pressed:
        if btn.left or btn.right or btn.up or btn.down and robot.man_up_value == 1:
            ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
            freak_out(robot)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)

        width_value = robot.pixy.value(3)

        if width_value > 0 and speech == 0 and robot.man_up_value == 1:
            run_away(robot)
            ev3.Sound.speak("Lets never go there again").wait()
            time.sleep(2)
            computer_advice('Dialogue Number:',speech, "of 4")
            speech = speech + 1
        elif width_value > 0 and speech == 1:
            run_away(robot)
            ev3.Sound.speak("Why do you have to do this").wait()
            time.sleep(2)
            speech = speech + 1

        elif width_value > 0 and speech == 2 and robot.man_up_value == 1:

            run_away(robot)
            ev3.Sound.speak("That was so scary").wait()
            time.sleep(2)
            computer_advice('Dialogue Number:', speech, "of 4")
            speech = speech + 1

        elif width_value > 0 and speech == 3 and robot.man_up_value == 1:

            run_away(robot)
            ev3.Sound.speak("What was that").wait()
            time.sleep(3)
            computer_advice('Dialogue Number:', speech, "of 4")
            speech += 1

        elif width_value > 0 and speech == 4 and robot.man_up_value == 1:

            run_away(robot)
            ev3.Sound.speak("What did I just see")
            computer_advice('Dialogue Number:', speech, "of 4")
            speech = 0

def computer_advice(advice1,advice2,advice3):
    print("-----------------Computer:------------------")
    print(advice1,str(advice2),advice3)
    print("--------------------------------------------")
def run_away(robot):
    print("-----------------Computer:------------------")
    print("EV3 is scared!")
    print("--------------------------------------------")
    if robot.man_up_value == 1:
        ev3.Sound.beep().wait()
        robot.stop_both()
        robot.turn_degrees(180, 800)
        time.sleep(1)
        robot.drive(700, 700)
        time.sleep(3)
        robot.stop_both()
def freak_out(robot):
    ev3.Sound.beep().wait()
    robot.turn_degrees(360, 800)
    time.sleep(3)


main()
