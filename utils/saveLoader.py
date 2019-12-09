import pandas as pd
import numpy as np
from utils.config import *
from utils.decorator import *

@count_time
def get_text(*dataframe):
    """
    把训练集，测试集的文本拼接在一起
    :param file: 若为空则不保存文件
    :param dataframe: 传入一个包含数个df的元组
    :return:
    """
    text = ""
    for df in dataframe:
        # 把从第三列(包括)开始的数据拼在一起
        text += "\n".join(df.iloc[:, 3:].apply(lambda x: " ".join(x.to_list()), axis=1))
        # text += "<end>\n".join(df.iloc[:, 3:].apply(lambda x: " ".join(["<start>"] + x.to_list()), axis=1))

    return text


def save_text(text, file):
    with open(file, mode="w", encoding="utf-8") as f:
        f.write(text)


def load_text(file):
    with open(file, mode="r", encoding="utf-8") as f:
        text = f.read()
    return text


def save_user_dict(user_dict, file):
    """
    user_dict
    :param user_dict:
    :param file:
    """
    with open(file, mode="w", encoding="utf-8") as f:
        f.write("\n".join(user_dict))



def load_dataset(train_data_path_, test_data_path_):
    """
    数据数据集
    :param train_data_path_:训练集路径
    :param test_data_path_: 测试集路径
    :return:
    """
    # 读取数据集
    train_data = pd.read_csv(train_data_path_)
    test_data = pd.read_csv(test_data_path_)

    # 空值处理
    # train_data.dropna(subset=['Question', 'Dialogue', 'Report'], how='any', inplace=True)
    # test_data.dropna(subset=['Question', 'Dialogue'], how='any', inplace=True)

    train_data = train_data.fillna('')
    test_data = test_data.fillna('')
    return train_data, test_data


def save_vocab(path, vocab_index):
    """

    :param path: 要保存的vocab文件路径
    :param vocab_index: vocab
    """
    with open(path, mode="w", encoding="utf-8") as f:
        for key, value in vocab_index.items():
            f.write(str(key)+" ")
            f.write(str(value)+"\n")


def load_vocab(path):
    # path:
    vocab_index_ = {}
    index_vocab_ = {}
    with open(path, mode="r", encoding="utf-8") as f:
        for line in f.readlines():
            [vocab, index] = line.strip("\n").split(" ")
            vocab_index_[vocab] = int(index)
            index_vocab_[int(index)] = vocab
    return vocab_index_, index_vocab_


def load_train_dataset():
    """
    :return: 加载处理好的数据集
    """
    train_x = np.loadtxt(TRAIN_X)
    train_y = np.loadtxt(TRAIN_Y)
    test_x = np.loadtxt(TEST_X)
    train_x.dtype = 'float64'
    train_y.dtype = 'float64'
    test_x.dtype = 'float64'
    return train_x, train_y, test_x