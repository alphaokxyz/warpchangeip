import subprocess
import time

while True:
    # 断开 Warp 连接
    subprocess.run(['warp-cli', 'disconnect'])

    # 等待 3 秒钟
    time.sleep(3)

    # 连接 Warp
    subprocess.run(['warp-cli', 'connect'])

    # 等待 3 秒钟
    time.sleep(3)

    # 使用 curl 测试连接
    output = subprocess.run(['curl', 'myip.ipip.net', '--proxy', 'socks5://127.0.0.1:40000'], capture_output=True)

    # 解析输出并检查 IP 地址是否匹配
    output_str = output.stdout.decode('utf-8')
    if '当前 IP：104.28.222.43' not in output_str:
        print('IP 地址不匹配')
        break

    # 输出成功信息
    print('Success')

    # 等待 5 秒钟
    time.sleep(1)