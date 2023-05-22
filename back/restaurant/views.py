from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def round(x,y,z,a,b,c):
    x=int(x)
    y=int(y)
    z=int(z)
    a=int(a)
    b=int(b)
    c=int(c)
    r= (x-a)*(x-a)+(y-b)*(y-b)+(z-c)*(z-c)
    return r


@csrf_exempt
def calculator(request):
    #데이터 확인
    x = request.GET.get('x')#가격
    y = request.GET.get('y')#맛
    z = request.GET.get('z')#양
    drink = request.GET.get('drink')#술
    delivery = request.GET.get('delivery')#배달
    category = request.GET.get('category')#메뉴
    

    #저장된 값.
    #ex) category 0 한식 1 일식 2중식 3양식 4치킨
    #ex) drink,delivery 0 가능 1 불가능
    # menulist x,y,z,delivery, category
    menulist=[[0,0,0,0,0,0],
              [48,75,73,0,1], # 낙지도가
              [56,77,76,0,1], # 성수식당
              [76,73,74,0,0], # 로뎀식당
              [59,67,67,0,1], # 백채김치찌개
              [63,71,76,], # 명동찌개마을
              [56,68,67], # 돈피그
              [44,70,63], # 돼지가예술
              [62,64,77], # 호가
              [50,85,71], # 중앙정육식당
              [52,64,74], # 진성곱창
              [57,67,73], # 샤브향
              [49,78,83], # 산채가
              [46,77,79], # 대만족
              [49,78,81], # 보쌈주는족발짐
              [62,70,69], # 원할머니보쌈
              [52,71,76], # 진성부대찌개
              [53,77,73], # 두찜
              [48,79,66], # 대박삼겹김치찜
              [49,72,70], # 왕십리 야채곱창
              [65,71,71], # 엄마손칼국수(칼국수)
              [62,79,79], # 엽떡
              [65,79,79], # 신천떡볶이
              [67,72,60], # 명수당분식
              [71,83,61], # 이태리식당
              [56,85,64], # 당신
              [86,87,80], # 리오브리또
              [56,80,73], # 청년피자
              [64,80,69], # 피자보이
              [67,68,64], # 더더피자
              [73,73,78], # 맘스터치
              [57,69,57], # 666버거
              [72,70,70], # 롯데리아
              [68,73,75], # 이백장돈까스
              [59,86,75], # 미가초밥
              [58,79,57], # 스시어게인
              [50,78,68], # 고인돌횟집
              [73,80,79], # 엄마손칼국수(돈까스)
              [61,77,62], # 교촌치킨
              [68,76,70], # BHC
              [66,82,69], # 전설의치킨
              [76,84,80], # 미쳐버린파닭
              [62,82,68], # BBQ
              [67,74,75], # 페리카나
              [73,79,79], # 치킨마루
              [67,87,66], # 지코바
              [73,83,76], # 신통치킨
              [55,79,76], # 모현양꼬치
              [73,67,67], # 상원
              [76,73,68], # 차이나타운
              [74,84,81], # 야미마라탕
              [79,65,67], # 모현각
              [70,87,81], # 마라장룔


            ]
    #순서대로 가격, 맛, 양, 배달, 술, 메뉴
    menuname=[
        ['음식점a','a설명'],
        ['낙지도가'],
        ['성수식당'],
        ['로뎀식당'],
        ['백체김치찌개'],
        ['명동찌개마을'],
        ['돈피그'],
        ['돼지가예술'],
        ['호가'],
        ['정육정육식당'],
        ['진성정육식당'],
        ['진성곱창'],
        ['샤브향'],
        ['산채가'],
        ['대만족'],
        ['보쌈주는족발집'],
        ['원할머니보쌈'],
        ['진성부대찌개'],
        ['그집곱도리탕'],
        ['두찜'],
        ['대박삼겹김치찜'],
        ['왕십리 야채곱창'],
        ['엄마손칼국수(칼국수)'],
        ['엽떡'],
        ['신전떡볶이'],
        ['명수당분식'],
        ['이태리식당'],
        ['당신'],
        ['리오브리또'],
        ['청년피자'],
        ['피자보이'],
        ['더더피자'],
        ['맘스터치'],
        ['666버거'],
        ['롯데리아'],
        ['이백장돈까스'],
        ['미가초밥'],
        ['스시어게인'],
        ['고인돌횟집'],
        ['엄마손칼국수(돈까스)'],
        ['교촌치킨'],
        ['BHC'],
        ['전설의치킨'],
        ['미쳐버린파닭'],
        ['BBQ'],
        ['페리카나'],
        ['치킨마루'],
        ['지코바'],
        ['신통치킨'],
        ['모현양꼬치'],
        ['상원'],
        ['차이나타운'],
        ['모현각'],
        ['마라장룡'],



    ]
    store=''
    explan=''
    #계산
    shortlength=40000
    resultnum=6
    for i in range(len(menulist)):
        if(menulist[i][3]==int(drink) and menulist[i][4]==int(delivery)):
            if(menulist[i][5]==int(category)):
                length=round(x,y,z,menulist[i][0],menulist[i][1],menulist[i][2])
                if(shortlength>=length):
                    shortlength=length
                    resultnum=i

    store=menuname[resultnum][0]
    explan=menuname[resultnum][1]

    #응답
    return render(request,'calculator.html',{'store':store,'explan':explan})