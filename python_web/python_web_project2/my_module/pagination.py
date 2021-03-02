def pagination_by10(page: int) -> range :
    # 페이지를 10개씩 보여줄 때 그 범위를 리턴해주는 함수
    # 만약 12면 range(10,21), 5면 range(1,11)를 리턴함

    page_divided = page//10
    if page%10 == 0:
        page_divided -= 1

    return range(page_divided*10 + 1, page_divided*10 + 11)