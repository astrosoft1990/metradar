
# _*_ coding: utf-8 _*_

'''
快速绘制三维雷达组网拼图

'''

# %%
from metradar.graph.draw_comp_mosaic import draw_composite_operational
import os

from metradar.config import CONFIG

# 资源文件路径
RESOURCES_PATH = CONFIG.get('SETTING','RESOURCES_PATH')
COLOR_FILE=RESOURCES_PATH + '/gr2_colors/default_BR_PUP2.pal'

if __name__ == "__main__":

    
    path = '/mnt/e/metradar_test/vpr/mosaic/20230731_daxing'
    outpath = '/mnt/e/metradar_test/vpr/mosaic/20230731_daxing/mosac_pic'

    print(os.listdir(path))
    for file in os.listdir(path):
        if not file.endswith('.nc'):
            continue
        draw_composite_operational(path + os.sep + file,outpath,colorfile=None)
        pass


