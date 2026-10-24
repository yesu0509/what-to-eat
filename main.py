import random

MENUS = [
    "학식",
    "긱식",
    "교식",
    "피자",
    "김밥천국",
    "샐러드",
    "맘스터치",
    "bhc",
    "국밥",
    "편의점 도시락",
    "퀴즈노스",
    "지관서가",
    "카페리차드샌디",
    "더치앤빈",
    "롤링핀",
    "치킨",
    "칼국수",
    "배달음식"
]


def recommend_menu():
    return random.choice(MENUS)


def main():
    print("=== 뭐먹어유 ===")
    print("오늘 점심이 고민될 때!")

    input("엔터를 누르면 메뉴를 추천해드려요: ")

    retry_count = 0

    while True:
        print(f"오늘은 {recommend_menu()} 어때요?")
        answer = input("추천 메뉴를 바꿔볼까요? (y/n):")
        if answer.lower() != "y":
            print("맛있게 드세요!")
            break
        retry_count +=1
        if retry_count == 15:
            print ("아무거나 드세요...")
            break


if __name__ == "__main__":
    main()