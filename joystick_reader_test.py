import serial
import struct


def read_joystick_data(port, num_axes):
    """
    读取 SMC35 操纵杆数据。
    :param port: 串口号 (如 COM3, /dev/ttyUSB0)
    :param num_axes: 轴数量 (2 或 3)
    """
    try:
        # 初始化串口
        with serial.Serial(port, 9600, timeout=3) as ser:
            print(f"连接到操纵杆: {port}, 波特率: 9600")

            # 持续接收数据
            while True:
                # 读取返回数据（假设每次返回9字节）
                data = ser.read(9)  # 根据实际情况修改字节数
                if len(data) < 9:
                    print("未收到完整数据包，继续等待...", end="\r")
                    continue

                # 解析数据
                header, x_high, x_low, y_high, y_low, z_high, z_low, button, checksum = struct.unpack("BBBBBBBBB", data)

                if header == 0xFF:
                    x = (x_high << 8) | x_low
                    y = (y_high << 8) | y_low
                    z = (z_high << 8) | z_low if num_axes == 3 else None

                    # 使用回车符覆盖上次打印内容，避免滚动
                    print(f"\r操纵杆数据： X轴: {x}  Y轴: {y}  Z轴: {z if z is not None else 'N/A'}  按钮状态: {button}", end="")
                else:
                    print("无效的数据包头", end="\r")
    except serial.SerialException as e:
        print(f"串口错误: {e}")
    except Exception as e:
        print(f"发生错误: {e}")


if __name__ == "__main__":
    # 用户配置
    PORT = "/dev/ttyUSB0"  # 根据实际连接更改  /dev/ttyUSB0  COM5
    NUM_AXES = 3  # 操纵杆轴数量 (2 或 3)

    # 只使用波特率 9600
    read_joystick_data(PORT, NUM_AXES)
