# SMC35 Joystick Data Receiver

该项目通过串口连接到 SMC35 操纵杆，并接收并解析操纵杆的数据（包括 X 轴、Y 轴、Z 轴以及按钮状态）。支持不同的操作模式，可以在终端中实时显示操纵杆的数据。

## 特性

- 支持 `9600` 波特率连接 SMC35 操纵杆。
- 连续接收操纵杆数据并实时解析。
- 每次接收到新数据时覆盖显示上次的结果，避免滚动输出。
- 简单易用，只需要指定正确的串口号即可开始接收数据。

## 环境要求

- Python 3.x
- 安装 `pyserial` 库，用于串口通信。

## 安装与依赖

### 1. 安装 Python 和依赖库

首先确保你的电脑已经安装了 Python 3。如果没有安装，可以从 [Python 官网](https://www.python.org/downloads/) 下载并安装。

接下来，安装所需的库：

```bash
pip install pyserial
```

### 2. 下载项目

可以通过 `git` 克隆此项目：

```bash
git clone https://github.com/FrankJIE09/JoystickReaderProject.git
cd JoystickReaderProject
```

或者直接下载 `joystick_reader.py` 文件并放在本地目录中。

## 使用方法

### 1. 连接 SMC35 操纵杆

将操纵杆通过串口（USB 或 RS232）连接到你的计算机。确保连接正确，并确认串口号（例如 `COM5` 或 `/dev/ttyUSB0`）。

### 2. 修改配置

打开 `joystick_reader.py` 文件，找到如下部分：

```python
PORT = "COM5"  # 根据实际连接更改
NUM_AXES = 3   # 操纵杆轴数量 (2 或 3)
```

根据你的操纵杆连接情况，修改 `PORT` 为正确的串口号。

- Windows 示例：`PORT = "COM5"`
- Linux 示例：`PORT = "/dev/ttyUSB0"`

如果你的操纵杆是 2 轴操作，修改 `NUM_AXES` 为 `2`；如果是 3 轴操作，保持 `NUM_AXES = 3`。

### 3. 运行程序

在命令行中进入项目目录并运行：

```bash
python joystick_reader.py
```

### 4. 查看结果

程序会连接到 SMC35 操纵杆并开始实时接收数据。每当接收到新的数据时，控制台中会实时更新数据，覆盖上一行输出。

示例输出：

```
连接到操纵杆: COM5, 波特率: 9600
操纵杆数据： X轴: 512  Y轴: 512  Z轴: 512  按钮状态: 0
```

### 5. 停止程序

按 `Ctrl + C` 停止程序的运行。

## 代码说明

- **串口通信**：使用 `pyserial` 库通过串口与操纵杆进行通信。
- **数据解析**：操纵杆返回的数据为固定格式，每次返回 9 字节。程序使用 `struct` 解析字节流。
- **数据输出**：每次接收到的数据都在同一行上覆盖显示，避免滚动输出。

## 常见问题

### 1. 串口连接失败

确保操纵杆已正确连接，且 `PORT` 配置为实际使用的串口号。

### 2. 数据未更新

如果数据未更新或显示无效数据包，检查串口连接和波特率是否匹配。程序默认使用波特率 `9600`。

### 3. 串口已占用

如果串口被其他程序占用，可以尝试关闭其他占用该串口的程序，然后重新运行此程序。

## 贡献

欢迎贡献代码或报告问题。请通过 [GitHub Issues](https://github.com/FrankJIE09/JoystickReaderProject/issues) 提交问题报告，或通过 Pull Request 提交代码贡献。

## License

MIT License. See [LICENSE](LICENSE) for more details.
