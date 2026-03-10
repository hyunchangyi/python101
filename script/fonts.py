import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import os

!sudo apt-get install -y fonts-nanum > /dev/null 2>&1                  
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

fm.fontManager.addfont('/usr/share/fonts/truetype/nanum/NanumGothic.ttf')
plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False

# nanum_fonts = [f for f in fm.fontManager.ttflist if 'Nanum' in f.name]

# if len(nanum_fonts) == 0:
#     fm.fontManager.__init__()
#     print('Nanum fonts installed. Restart Colab runtime.')
#     # 단계 2: 런타임 재시작
#     os.kill(os.getpid(), 9)
# else:    
#     print('Nanum fonts are ready for plot.')
#     # 한글 폰트 설정
#     plt.rc('font', family='NanumGothic')
#     # 마이너스 표시 문제
#     plt.rcParams['axes.unicode_minus'] = False
    
    
# import requests

# def save_url_file(url, filename):
#     r = requests.get(url, allow_redirects=True)
#     open(filename, 'wb').write(r.content)
        
        
