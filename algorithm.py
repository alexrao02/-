l = [[], [], [], [], []]
flag = 0
song_repeat = []
def insert(list):

    global flag
    l[flag] = list
    flag += 1

def put():
    return findMostLisented(l[0], l[1], l[2], l[3], l[4])

def findMatchPercent(songInfo1, songInfo2):
    song_repeat.clear()
    length = 0
    for i in range(len(songInfo1)):
        for j in range(len(songInfo2)):
            if songInfo1[i]==songInfo2[j]:
                song_repeat.append(songInfo1[i])
                length += 1
    return length/min(len(songInfo1), len(songInfo2))

def findMostLisented(songInfo1, songInfo2, songInfo3, songInfo4, songInfo5):
    songDic = {}
    for song in songInfo1:
        songDic[song] = songDic.get(song, 0) + 1
    for song in songInfo2:
        songDic[song] = songDic.get(song, 0) + 1
    for song in songInfo3:
        songDic[song] = songDic.get(song, 0) + 1
    for song in songInfo4:
        songDic[song] = songDic.get(song, 0) + 1
    for song in songInfo5:
        songDic[song] = songDic.get(song, 0) + 1
    Song, Number = "", 0
    for song, playNumber in songDic.items():
        #print(song, playNumber)
        if playNumber > Number:
            Number = playNumber
            Song = song
    return Song

def listChange(songInfo1, songInfo2):
    changeNumber = [[0 for j in range(2000)] for i in range(2000)]
    flag = 0
    for i in range(len(songInfo1) + 1): changeNumber[i][0] = i
    for i in range(len(songInfo2) + 1): changeNumber[0][i] = i
    for i in range(1, len(songInfo1) + 1):
        for j in range(1, len(songInfo2) + 1):
            if songInfo1[i-1] == songInfo2[j-1]: flag = 0
            else: flag = 1
            changeNumber[i][j] = min(changeNumber[i][j-1]+1, changeNumber[i-1][j]+1, changeNumber[i-1][j-1]+flag)
    return changeNumber[len(songInfo1)][len(songInfo2)]
