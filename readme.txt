CBV

FormView
양식을 표시하는 보기입니다. 오류 시 유효성 검사 오류가 있는 양식을 다시 표시하고, 성공하면 새 URL로 리디렉션합니다.

form_valid
리디렉션- 방문자에게 초기에 요청한 URL이 아닌 다른 URL을 제공하는 행위

CreateView
개체를 만들고 유효성 검사 오류가 있는 경우 양식을 다시 표시하고 개체를 저장하는 양식을 표시하는 보기입니다.

template_name_suffix
GET 요청에 표시되는 CreateView 페이지는 '_form'의 template_name_suffix를 사용합니다. 예를 들어, 작성자 모델에 대한 객체를 생성하는 보기에 대해 이 속성을 '_create_form'으로 변경하면 기본 template_name이 'myapp/author_create_form.html'이 됩니다.

object
CreateView를 사용하면 생성 중인 개체인 self.object에 액세스할 수 있습니다. 개체가 아직 생성되지 않은 경우 값은 없음이 됩니다.

행동 양식
get( 요청 , * args , ** kwargs ) ¶
현재 개체 인스턴스 ( self.object)를로 설정합니다 None.
post( 요청 , * args , ** kwargs ) ¶
현재 개체 인스턴스 ( self.object)를로 설정합니다 None.

UpdateView
기존 개체를 편집하고 유효성 검사 오류가 있는 경우 양식을 다시 표시하고 개체에 변경 내용을 저장하는 양식을 표시하는 보기입니다. 이 작업은 개체의 모델 클래스에서 자동으로 생성된 양식을 사용합니다(양식 클래스를 수동으로 지정하지 않는 경우).
self.object업데이트되는 객체 인에 액세스 할 수 있습니다 .

template_name_suffix
GET 요청에 표시되는 UpdateView 페이지는 '_form'의 template_name_suffix를 사용합니다. 예를 들어 Author 모델의 보기 업데이트 개체에 대해 이 속성을 '_update_form'으로 변경하면 기본 template_name이(가) 'myapp/author_update_form.html'이 됩니다.

object
UpdateView를 사용할 때 업데이트할 개체인 self.object에 액세스할 수 있습니다.

DeleteView
확인 페이지를 표시하고 기존 개체를 삭제하는 보기입니다. 요청 방법이 POST인 경우에만 지정된 개체가 삭제됩니다. GET를 통해 이 보기를 가져오면 동일한 URL에 POST하는 양식을 포함하는 확인 페이지가 표시됩니다.

template_name_suffix
GET 요청에 표시되는 DeleteView 페이지는 '_confirm_delete'의 template_name_suffix를 사용합니다. 예를 들어 Author 모델의 개체를 삭제하는 보기에 대해 이 속성을 '_check_delete'로 변경하면 기본 template_name이(가) 'myapp/author_check_delete'가 됩니다.html'



DetailView
이 보기가 실행되는 동안 self.object에는 보기가 작동 중인 개체가 포함됩니다.

기본적으로 이것은 'self'에서 조회한 모델 인스턴스이다.아직 조사하지 않았지만
view는 "self.get_object"를 재정의하여 *any* 객체의 표시를 지원합니다.


ListView
개체 목록을 나타내는 페이지입니다.
이 보기가 실행되는 동안 self.object_list에는 보기가 작동 중인 개체 목록이 포함됩니다(보통 쿼리 집합은 아님).

get_paginator



기반 뷰(Base View)
View: 최상위 부모 제너릭 뷰 클래스
TemplateView: 주어진 템플릿으로 렌더링
RedirectView: 주어진 URL로 리다이렉트
제너릭 보기 뷰(Generic Display View)
DetailView: 조건에 맞는 하나의 객체 출력
ListView: 조건에 맞는 객체 목록 출력
제너릭 수정 뷰(Generic Edit View)
FormView: 폼이 주어지면 해당 폼을 출력
CreateView: 객체를 생성하는 폼 출력
UpdateView: 기존 객체를 수정하는 폼을 출력
DeleteView: 기존 객체를 삭제하는 폼을 출력
제너릭 날짜 뷰(Generic Date View)
YearArchiveView: 주어진 연도에 해당하는 객체 출력
MonthArchiveView: 주어진 월에 해당하는 객체 출력
DayArchiveView: 주어진 날짜에 해당하는 객체 출력
TodayArchiveView: 오늘 날짜에 해당하는 객체 출력
DateDetailView: 주어진 연, 월, 일 PK(또는 슬러그)에 해당하는 객체 출력


PEP-8

들여쓰기
-4개의 스페이스를 사용
if 구문이 여러줄을 사용할정도로 길경우()여는괄호

들여쓰기-괄호 (여러줄)
mylist=[
 1,2,3,
 4,5,6
]
-tt옵션을 사용하는 경우에는 경고가 아니라 에러가되며 스페이스와 탭을 섞어서 작성된 코드에는 경고가 뜬다
----------------------
한줄의 최대길이는 79문자로 제한한다
주석이나 닥스트링 72제한
닥스트링""" """
--------------------------------------------
소스 파일 인코딩
핵심 Python 배포의 코드는 항상 UTF-8 (또는 Python 2의 ASCII)을 사용해야합니다.
------------------------------------------------

작업효율개선, 기본행바꿈에 의해 구조가 파괴되는 상황을 피하기 위함
----------------
여러줄 특히 with구문은 빽슬래시\ 사용권장

이항연산자 에서의 줄바꿈 가독성을위해 이항연산자 기호 먼저 쓰고 줄바꿈 권장
예) +taxable
     - ira
파이썬 코드에서는 이항연산자 이전혹은 이후에 줄바꿈을 하는것이 가능하다

핵심파이썬 배포판의 코드는 항상UTF-8을 사용

import는 행으로 구분되어서 사용
from subprocess import Popen,PIPE
O사용가능
Absolute import 권장

__all__=[1,2,3]
Dunder Names은 반드시 모듈 닥스트링 뒤에쓰여져야하고 from__future__import 제외하고 import 문 전에 쓰여져야한다.

함수 불로오기 변수리스트시작을 알리는 여는괄호전에서의 공백
인덱싱공백,할당공백,후행공백,키워드독립변수공백
콤마,세미클론,혹은 콜론 전 슬라이스에서 공백
중괄호,대괄호,괄호안에 관계없는 공백은 피하도록한다.

뒤에있는 콤마를 사용할 경우 괄호로 문자를 덮는것이 권장된다

주석은 가능한 첫번째는 대문자 마지막문장을 제외하곤 문장의 끝에 두개의 스페이스를 사용한다.
주석을 가능한 영어로한다

블럭 주석은 #와 하나의 스페이스로 시작
인라인 주석은 최소 2개의 스페이스로 구분되어야한다.

인라인 주석
인라인 주석을 사용하지 마십시오.

네이밍 스타일
CapWord에서 줄임말을 사용할 때 줄임말의 글자는 모두 대문자로 한다.

네이밍 규칙
한글자x, ACSII호환O, c/c++모듈은 이름앞에 언더스코어가 있어야한다.

클래스 이름
클래스이름은 CapWords작성규칙을 사용한다.

전역변수 __all__매커니즘을 사용하여야 하며 혹은 언더스코어의 위의 전역변수앞에 접두사로 붙이는 구식의 작성규칙을 사용한다.

함수이름은 가독성을 위해 언더스코어로 구분된 소문자 단어로 구성

함수 독립변수의 이름이 키워드와 충돌한다면 하나의 언더스코어를 끝에 덧붙이는것이 일반적으로 더좋다.

상수-대문자,언더스코어로 구분
public속성은 이름앞에 _언더스코어를 가지지않는다.
빈 리스트에서의 __all__세팅은 모듈이 public API를 가지고 있지 않음을 나타냄

라이브러리의 성능에 민감한 부분에 대해선 ''.join()형태를 대신에 사용하여야한다.

None과 같이 개체에 대한 비교는 equality operator가 아니라 is 혹은 is not과 함께 수행되야한다.
--------------------------------------------------
Not ...is보다는 is not 오퍼레이터를 사용할 것
---------------------------------------------------

다양한 비교를 사용하여 순서지정 연산을 구현할때에는, 특정코드만 사용하여 다른코드를 사용하는 대신 6가지 연산
__eq__,__ne__,__lt__,__le__,__gt__,__ge__을 사용

sort()및 min() <연산자를 사용하도록 보장되며 max()함수는 >연산자를 사용하나 그러나 다른 상황에서 혼동이 발생하지 않도록 6가지 작업을 모두 구현하는 것이 좋다

람다 표현식을 식별자에 직접 바인드 하는 할당문 대신에 항상 def 문을 사용하도록 한다.

BaseExceptions보단 Exception으로부터 예외를 얻도록 한다.
-무엇이 문제로 이끄는가에 대한 질문에 대답하는 것을 목표로 하도록 한다.

raise ValueError('message')권장

excep:사용보다 특정한 예외를 언급하도록 한다.
모든 예외를 잡길 원하면 excep Exception:사용

try구문의 절대적인 수를 최소한
좋은 예:
try:
    value=collection[key]
except KeyError:
    return key_not_found(key)
else:
    return handle_value(value)

try/finally

return 구문이 표현식을 반환했다면, 어떤 return구문이 반환되는 값이 없는 곳에서는 'return None'을 명시하고 함수의 끝에 explitict return 구문이 존재해야한다.

문자열 모듈 대신에 문자열 메서드를 사용하도록한다.

접두사 혹은 접미사를 확인하기 위해서는 문자열 슬라이싱 대신에 .startswith()와 .endswith()를 사용

오브젝트 타입 비교는 타입비교대신 isinstance()를 사용

불린값을 True혹은 False에 ==를 사용하여 비교하지 말도록한다.

함수주석 pep484
변수주석 pep526


