import os
import yaml

data_dict = {0: "0炉子开关.txt", 1: "1炉丝电机.txt", 2: "2转机1.txt", 3: "3样提机2.txt", 4: "4炉上机3.txt",
             5: "5炉中机4.txt", 6: "6炉下机5.txt", 7: "7电机状态查询.txt", 8: "8磁场.txt", 9: "9电机磁场电流.txt",
             "A": "A炉丝加热电压.txt", "B": "BPID控温曲线.txt", "C": "C在线监控状态查询.txt", "D": "D电机关闭设置.txt",
             "E": "E在线监控表头设置.txt", "F": "FPID参数设置动作表.txt"}
conf_dict = {0: "FurnaceSwitch.yaml", 1: "HearthWireMotor.yaml", 2: "Transfer1.yaml", 3: "Sample2.yaml",
             4: "Stove3.yaml", 5: "Stove4.yaml", 6: "Stove5.yaml", 7: "MotorStatusInquiry.yaml", 8: "MagneticField.yaml",
             9: "MotorMagneticFieldCurrent.yaml", "A": "FurnaceWireHeating.yaml", "B": "PIDTemperatureControl.yaml",
             "C": "OnlineMonitoringStatus.yaml", "D": "MotorClosing.yaml"}


# 存储数据到文件
def store_data(hex_data, action_code):
    """
    保存16进制的动作编码到txt文件

    :param hex_data: 要存储的16进制数据
    :param action_code: 动作类别的标识（总共16个动作）
    :return:
    """
    # 写入文件路径
    file_path = os.path.join("data", data_dict[action_code])
    # 打开文件并写入数据
    with open(file_path, 'a') as file:
        file.write(hex_data + '\n')


# 获取动作配置参数信息
def get_config(action_code):
    """
    获取动作配置参数信息（不同设置对应的16进制值）
    :param action_code: 动作类别编码
    :return: action_code动作类别对应的参数配置信息
    """
    conf_path = os.path.join("config", conf_dict[action_code])
    with open(conf_path, 'r', encoding='utf-8') as file:
        conf = yaml.safe_load(file)
    return conf


def get_action_id(config_hex, action_code):
    """
    根据配置参数编码查询动作ID，若存在则返回已存在的ID，不存在递增生成一个新ID返回
    :param config_hex:
    :param action_code:
    :return: 返回一个Tuple，(动作id, 是否是新动作：是 = 1，否 = 0)
    """
    final_id = str(action_code) + "000"
    # 读取文件
    # data_file = QFile(":/data/" + data_dict[action_code])
    # data_file.open(QIODevice.ReadOnly | QIODevice.Text)
    # all_data = str(data_file.readAll(), encoding='utf-8')
    with open("./data/" + data_dict[action_code], 'r', encoding='utf-8') as data_file:
        all_data = data_file.read()

    # 为空直接返回
    if len(all_data) == 0:
        return final_id, 1

    list_all = all_data.split("\n")

    for line in list_all:
        action_id, config = tuple(line.split(" "))
        final_id = action_id
        # 找到相同的参数配置则返回相同的ID
        if config_hex == config:
            data_file.close()
            return final_id, 0
    # 没找到相同的ID, 在最后一个ID号的基础上+1
    data_file.close()
    return format(int(final_id, 16) + 1, '04X'), 1


if __name__ == "__main__":
    ...
