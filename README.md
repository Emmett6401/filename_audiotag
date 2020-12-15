# 파일이름일괄수정하고 오디오tag수정해서 다시 써넣기 
## pip install eyed3 하셔야 합니다. 
"""
filename handle and audio tag convert by python 파일이름을 바꾸고 오디오tag를 수정하는 파이썬소스
이프로그램은 mp3파일을 네이버더빙으로 다운로드 받으면 376개의 파일이 아래와 같이 다운로드 됩니다.
01_영상.mp3 부터 375_안녕하세요_만나서_반_가_워.mp3등으로 불규칙한 파일이름을
7001 ~ 7399.mp3 형태로 바꾸어 주는 것이다.
그리고 오디오파일 tag를 수정해서 제목에 이름이 나오도록 했다.
그리고 정리된 파일은 list.txt라는 파일이름으로 저장해 두도록 했다.
2020. 12. 15
By Emmett
""" 
import os
import eyed3

file_path = 'F:\\cut'
filenames = os.listdir(file_path)
print(filenames)

f = open('F:\\list.txt', 'w')
for name in filenames:
    src = os.path.join(file_path, name)
    audiofile = eyed3.load(src);

    """ 자르고 어쩌고 저쩌고 해서 최종 dst를 만드는 과정 """
    tt = name.split('_')
    ttf = '%04d' % (int(tt[0]) + 7000)
    mdst = str(ttf)
    ddst = str(ttf)
    for i in range(1, len(tt)):
        mdst = mdst + "_" + tt[i]

    """ 여기는 오디오 태그를 정리 하는 곳입니다. """
    audiofile.tag.artist = "SBLabs 2020.12.15"
    audiofile.tag.title = mdst

    audiofile.tag.album = "Free For All Comp LP"
    audiofile.tag.album_artist = "For DOF18"
    audiofile.tag.track_num =  ttf
    audiofile.tag.save()

    """ 여기는 파일 이름을 정리 하는 곳이구요."""
    print(name + "\t\t\t>>>" + '{' + tt[0] + '}' + '{' + tt[1] + '}' + "\t>>>" + str(ttf) + "\tdst>>>" + mdst)
    ddst = ddst + ".mp3"
    dst = os.path.join(file_path, ddst)
    os.rename(src, dst)
    abc = str(ttf) + "           " + mdst
    f.write(abc)
    f.write("\n")

f.close()
