import jieba
import wordcloud
import imageio
mask=imageio.imread('中国地图.jpeg')
f= open('三体全集.txt','r',encoding='utf-8')
t=f.read()
f.close
ls=jieba.lcut(t)
txt=' '.join(ls)
w=wordcloud.WordCloud(font_path='C:\\$Recycle.Bin\\S-1-5-21-956881968-3683699883-3077907830-500\\$R3UWT13\\Updates\\Download\\PackageFiles\\F48252D1-E2D1-4E3D-A011-C1A468BFE8F4\\root\\vfs\\Fonts\\private\\MSYH.TTC',width=1000,height=700,background_color='white',max_words=200,mask=mask)
w.generate(txt)
w.to_file('三体.png')