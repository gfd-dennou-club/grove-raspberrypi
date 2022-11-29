import time
import pigpio

pi = pigpio.pi()

#PWMパラメータ
pwm_pin = 12 #PWM出力ピンを指定 (PWM ピン)
freq = 400 #PWM周波数をHzで指定

duty = 0
while True: 
    cnv_dutycycle = int((duty * 1000000 / 100)) #パラメータ変換

    #PWMを出力
    pi.hardware_PWM(pwm_pin, freq, cnv_dutycycle)

    # 1 秒間
    time.sleep(0.5)

    duty = (duty + 10) % 100
    print( duty )
