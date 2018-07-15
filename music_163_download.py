import urllib
import urllib.request
import json


def report(blocknum, bs, size):
    '''回调函数
    @blocknum:已经下载的数据块
    @bs:数据块的大小
    @size:远程文件的大小
    '''
    if size == -1:
        # print("歌曲不存在")
        return
    per = 100.0 * blocknum * bs / size
    if per > 100:
        per = 100
        print('【HH】-> 歌曲下载完毕')
    print('%.2f%%' % per)


def search_song(s, user):
    print('[log]searching song:' + s)
    params = urllib.parse.urlencode({'keywords': s})  # 格式化参数

    f = urllib.request.urlopen("https://163.fczbl.vip/search?"+params , timeout=3)  
    
    search_result = json.loads(f.read().decode('utf-8'))

    result = search_result['result']['songs'][0]['id']

    
    print('【HH】->歌曲ID:',result)
    # print('下载地址：',"http://music.163.com/song/media/outer/url?id=" + str(result) + ".mp3")
    download_url = "http://music.163.com/song/media/outer/url?id="+str(result)+".mp3"
    
    f = urllib.request.urlopen(download_url,timeout=3)
    # 根据前三个字节来判断是不是MP3，找不到歌曲
    if(f.readline(3) == b'ID3'):
        
        urllib.request.urlretrieve("http://music.163.com/song/media/outer/url?id="+str(result)+".mp3", './download/'+str(result)+'.mp3',report)
        with open('list.ini','a') as f:
            f.write(s+'\n')
    else:
        print("【HH】-> 找不到该歌曲")



if __name__ == '__main__':
    
    song_name = input("输入歌曲名字：")
    search_song(song_name,666)   

    