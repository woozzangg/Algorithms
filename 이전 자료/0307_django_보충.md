# django 보충 1

Hyper Text

어떠한 문서

하나의 규약인데 클라이언트가 서버에 요청을 보내서 응답을 받는것

[요청-응답]

URL을 통해서 요청

HTML, JSON ... 문서등을 통해서 응답 받음.





HTML/CSS - 문서를 만드는 문법

Django - 서버를 만드는 하나의 Framework 중 하나

Django - URL로 요청을 받아서 처리를 하고, HTML문서를 응답해주는것

urls.py / views.py  

요청 받아서 처리

---

template

html문서 응답



프레임워크 -> 함수, 객체 개념 많이필요

함수 - 블랙박스 인풋 - 아웃풋

why? - 다른 사람이 만든 코드를 활용하는 것

객체 - 어떤 하나의 type - 메서드, 속성 만 기억

---



## 교수님 정리

- 대원칙!!!!!!!!!!!!!!!!!!!!!!!!이 세상에 그냥은 없다.import를 한 것 혹은 views.py 함수 내에서는 request + a

- 직접 처음부터 만들어봐야해요 *

- 앱을 만든다?

  - settings.py 에 등록
  - urls.py 분리 (include)
  - urls.py 생성 (app_name)

- 요청을 처리하는 흐름을 만든다?

  - Url

    - URL 경로를 어떻게 만들지 ???
    - views 함수 뭐로 이름 짓지?
    - 이 URL을 어떻게 부르지?

    Python

    1

    `path('URL경로', views.____, name=____)`

  - View

    - 함수이름은 정해짐! urls.py에서

    - IF, 

      - URL에서 변수처럼 쓰는 것이 없다면

        Python

        1

        `def aaa(request):`

      - 쓰는 것이 있다면 (`path ('<name>/', views.aaa, name='aaa')`)

        Python

        1

        `def aaa(request, name):`

    - 어떤 템플릿 파일을 만들어서 던질지!

      Python

      1

      `return render(request, '앱이름/view이름.html')`

  - Template

    - 적절한 html 파일을 만든다.

    - if 템플릿에서 내가 어떠한 파이썬 결과를 쓰고 싶다면, views.py 에서 context로 넘기기!!!!! 출력은

      Django

      1

      `{{ 키 }}`

---

![Image Pasted at 2022-3-7 19-17](C:\Users\dannb\Desktop\잡동사니\Image Pasted at 2022-3-7 19-17.jpg)

![Image Pasted at 2022-3-7 19-31](C:\Users\dannb\Desktop\잡동사니\Image Pasted at 2022-3-7 19-31.jpg)

![Image Pasted at 2022-3-7 19-39](C:\Users\dannb\Desktop\잡동사니\Image Pasted at 2022-3-7 19-39.jpg)

![371](C:\Users\dannb\Desktop\잡동사니\371.png)![Image Pasted at 2022-3-7 20-19](C:\Users\dannb\Desktop\잡동사니\Image Pasted at 2022-3-7 20-19.jpg)

<img src="C:\Users\dannb\Desktop\잡동사니\372.png" alt="372" style="zoom:60%;" />