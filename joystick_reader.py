import serial
import struct

class Joystick:
    def __init__(self, port, num_axes, baudrate=9600):
        """
        初始化操纵杆类。
        :param port: 串口号 (如 COM3, /dev/ttyUSB0)
        :param num_axes: 轴数量 (2 或 3)
        :param baudrate: 波特率，默认值为 9600
        """
        self.port = port
        self.num_axes = num_axes
        self.baudrate = baudrate
        self.ser = None  # 串口对象

    def connect(self):
        """
        连接到串口。
        """
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=3)
            print(f"连接到操纵杆: {self.port}, 波特率: {self.baudrate}")
        except serial.SerialException as e:
            print(f"串口错误: {e}")
            raise  # Raise the error after logging it

    def read_data(self):
        """
        读取一次操纵杆数据。
        :return: 返回操纵杆数据 (x, y, z, button)，如果无效则返回 None
        """
        if self.ser is None or not self.ser.is_open:
            print("串口未连接，请先连接。")
            return None

        try:
            # 读取一次数据（假设每次返回9字节）
            data = self.ser.read(9)  # 根据实际情况修改字节数
            if len(data) < 9:
                print("未收到完整数据包，退出...")
                return None

            # 解析数据
            header, x_high, x_low, y_high, y_low, z_high, z_low, button, checksum = struct.unpack("BBBBBBBBB", data)

            if header == 0xFF:
                x = (x_high << 8) | x_low
                y = (y_high << 8) | y_low
                z = (z_high << 8) | z_low if self.num_axes == 3 else None
                return x, y, z, button
            else:
                print("无效的数据包头")
                return None
        except serial.SerialException as e:
            print(f"串口错误: {e}")
        except Exception as e:
            print(f"发生错误: {e}")
        return None

    def close(self):
        """
        关闭串口连接。
        """
        if self.ser and self.ser.is_open:
            self.ser.close()
            print(f"关闭与操纵杆的连接: {self.port}")

