
import Adafruit_BBIO.PWM as PWM

pwm1 = "P8_13"

PWM.start (pwm1, 0, 50)

for index in range (0, 5):
        # frequency = input ("Enter frequency: ")
        # dutyCycle = input ("Enter duty cycle: ") 
        
        volt = input ("Enter volt: ")
        dutyCycle = (volt * 100) / 3.3
        if dutyCycle > 100:
            dutyCycle = 100
        elif dutyCycle < 0:
            dutyCycle = 0

        # PWM.set_frequency (pwm1, frequency)
        PWM.set_duty_cycle (pwm1, dutyCycle)

PWM.stop (pwm1)
PWM.cleanup ()
