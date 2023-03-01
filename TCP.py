import socket
import serial


def main():
    # 创建TCP套接字
    TCP_Client_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接服务器
    serve_ip = input("请输入要连接的服务器ip:")
    serve_port = int(input("请输入要连接的服务器端口号:"))
    serve_addr = (serve_ip, serve_port)
    TCP_Client_Socket.connect(serve_addr)
    print("服务器连接成功")
    # 发送数据/接收数据
    send_data = input("请输入要发送给客户端的数据:")
    TCP_Client_Socket.send(send_data.encode())
    # 串口测试
    com = serial.Serial("COM4", 115200)
    print("COM4打开，波特率115200")
    # 测试数据
    while True:
        msg = TCP_Client_Socket.recv(1024)
        if not msg:
            break
        val = msg.decode("utf-8")
        print("监听到服务器数据是：")
        print(val)
        success_bytes = com.write(val.encode())
        print("服务器数据发送到COM4数据字节个数是：", success_bytes)
        print("服务器数据发送到COM4数据内容是：", val)
    # 关闭套接字
    TCP_Client_Socket.close()
    print("套接字关闭")


if __name__ == "__main__":
    main()
