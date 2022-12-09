# PEP 563의 postponed evalution
from __future__ import annotations

from copy import deepcopy

import typing


class Widget:

    # Widget 에 대한 타입 힌팅은 Widget 클래스가
    # 해당 Syntax가 끝날 때까지 정의되지 않기 떄문에
    # 정방향 참조(forward reference) 이다.

    # python은 이 참조를 평가하려고 시도하여 NameError를 발생시킨다
    def copy1(self) -> Widget:
        return deepcopy(self)

    # 위의 예시에서 이 type hinting을 가능하게 하는 방법은 따옴표로 묶는 방법이다.
    # 따옴표로 묶어진 타입은 파일의 끝에서 Type Checker에 의해서 평가된다.
    # 런타임 시점에는 문자열로 판단한다.
    def copy2(self) -> "Widget":
        return deepcopy(self)

    # PEP 563은 postponed evaluation 라는 행동으로 정의했다.
    # 따옴표로 묶는 Syntax를 요구하지 않고 모든 Type hinting이 이 패턴을 따르도록 이동한다.
    # from __future__ import annotations # 파일 최상단에 정의할것
    # 이렇게 하면 파이썬은 런타임에 해석하지 않으므로 NameError를 일으키지 않는다

    def copy3(self) -> Widget:
        return deepcopy(self)


# 호환성 문제
# - 런타임에 type hinting을 사용할 때 발생함
# - 런타임에 함수 또는 클래스에 대한 유형 힌트를 가져오기 위해
#    typing.get_type_hints() 함수를 제공하지만
#    python의 scope로 인해 항상 작동하는 건 아님

Book = typing.ForwardRef('Book')


def make_author():
    class Book:
        author: str

    class Author:
        book: Book

    return Author


Author = make_author()
print(typing.get_type_hints(Author))

# 하지만 위와 같이 정방향 참조를 사용하는 경우는 드물다
