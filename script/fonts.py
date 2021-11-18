import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import os

nanum_fonts = [f for f in fm.fontManager.ttflist if 'Nanum' in f.name]

if len(nanum_fonts) == 0:
    fm._rebuild()
    print('Nanum fonts installed. Restart Colab runtime.')
    # 단계 2: 런타임 재시작
    os.kill(os.getpid(), 9)
else:    
    print('Nanum fonts are ready for plot.')
    # 한글 폰트 설정
    plt.rc('font', family='NanumGothic')
    # 마이너스 표시 문제
    plt.rcParams['axes.unicode_minus'] = False
    
    
import requests

def save_url_file(url, filename):
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)
        
        
