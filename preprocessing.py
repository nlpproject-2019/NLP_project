from konlpy.tag import Hannanum
from konlpy.tag import Okt

#hannanum = Hannanum()
#print(hannanum.analyze(u'롯데마트의 흑마늘 양념 치킨이 논란이 되고 있다.'))

chat1 = "이게 맞지 모우라가 아약스전 잘했다고 선발은 빡쌔지 데스크로 전반 버티고 후반에 케인 빼면서 손,모우라 역습 조지는게 맞다 ^^"
chat2 = "4-2-3-1이 가장 자신있는 포메이션 같다"
chat3 = "존나 이게 현실이다 손뽕색들아ㅋㅋㅋㅋ"

chat = []
chat.append(chat1)
chat.append(chat2)
chat.append(chat3)

twitter = Okt()

for i in chat:
    k = twitter.pos(i, norm=True, stem=False)
    print(k)
    print(k[0][0])

