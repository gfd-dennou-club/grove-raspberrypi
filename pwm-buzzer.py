import time
import pigpio

pi = pigpio.pi()

#PWMパラメータ
pwm_pin = 12 #PWM出力ピンを指定 (PWM ピン)
duty = 70 #デューティー比を%で指定
freq = 400 #PWM周波数をHzで指定

#パラメータ変換
cnv_dutycycle = int((duty * 1000000 / 100))

#PWMを出力
pi.hardware_PWM(pwm_pin, freq, cnv_dutycycle)

# 3 秒間鳴らす
time.sleep(3)

#PWMを止める. duty = 0 に．
pi.hardware_PWM(pwm_pin, freq, 0)
