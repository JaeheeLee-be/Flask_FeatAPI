def add(a: int, b: int) -> int:
    return a + b


def test_add() -> None:
    # Given: 재료 준비
    a, b = 1, 1

    # When: 테스트 대상이 되는 함수를 호출합니다.
    result = add(a, b)

    # Then
    assert result == 2