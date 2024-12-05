import time

# 定义间隔时间
FLICKER_INTERVAL = 0.2  # 闪烁间隔(秒)

try:
    import Jetson.GPIO as GPIO
    print("Jetson.GPIO 模块已导入")
except ImportError:
    import RPi.GPIO as GPIO
    print("RPi.GPIO 模块已导入")

# 配置GPIO模式
GPIO.setmode(GPIO.BOARD)

# 定义GPIO引脚（假设使用引脚 3 到 42，共 40 个引脚）
gpio_pins = list(range(1, 40))

available_pins = []
unaviailable_pins = []

# 设置所有GPIO为输出模式
for pin in gpio_pins:
    try:
        GPIO.setup(pin, GPIO.OUT)
        available_pins.append(pin)
    except:
        unaviailable_pins.append(pin)

print(f"不可用GPIO引脚：{unaviailable_pins}")
print(f"可用GPIO引脚：{available_pins}")

print("开始检测GPIO，可用的GPIO将不断闪烁……")

try:
    while True:
        # 循环依次设置GPIO为高电平和低电平
        for pin in available_pins:
            GPIO.output(pin, GPIO.HIGH)
        time.sleep(FLICKER_INTERVAL)
        for pin in available_pins:
            GPIO.output(pin, GPIO.LOW)
        time.sleep(FLICKER_INTERVAL)

except KeyboardInterrupt:
    # 如果程序被中断，清理GPIO设置
    GPIO.cleanup()
    print("程序已终止，GPIO已清理。")
