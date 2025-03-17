from datetime import datetime
import logging
import os


class logUtil:
    # 打印日志到控制台和文件
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 指定目录和文件名
        directory = '/Users/ouyanghongbin/bgmgit/log'
        now = datetime.now()
        datetime_str = now.strftime('%Y-%m-%d')
        filename = f'{datetime_str}.log'
        file_path = os.path.join(directory, filename)
        # 写入文件
        with open(file_path, 'a', encoding='utf-8') as f:
            pass
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(file_path)
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)


        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


if __name__ == '__main__':
    log = logUtil()
    log.logger.debug('debug message')
    log.logger.info('info message')
