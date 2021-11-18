import os
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
from IPython import get_ipython

def install_nanum_fonts():
    nanum_fonts = [f for f in fm.fontManager.ttflist if 'Nanum' in f.name]

    if len(nanum_fonts) == 0:
        get_ipython().magic("apt-get -y install fonts-nanum")
#         !apt-get -y install fonts-nanum
        fm._rebuild()
        print('\n\nNanum fonts installed and matplotlib.font_manager rebuilt.')
        print('Restart Colab runtime.')

        # 단계 2: 런타임 재시작
        exit()  # os.kill(os.getpid(), 9)
    else:    
        print('\nNanum fonts are ready for plot.')
        # 한글 폰트 설정
        plt.rc('font', family='NanumGothic')
        # fm._rebuild() 

        # 마이너스 표시 문제
        plt.rcParams['axes.unicode_minus'] = False
