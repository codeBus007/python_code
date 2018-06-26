# 已经完成是关于print 的问题
# 解决办法如下
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

