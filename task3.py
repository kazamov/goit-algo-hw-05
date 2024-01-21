import timeit

from search.boyer_moore_search import boyer_moore_search
from search.kmp_search import kmp_search
from search.rabin_karp_search import rabin_karp_search


def read_article(filename):
    with open(filename, "r") as f:
        return f.read()


if __name__ == "__main__":
    article1_content = read_article("data/article1.txt")
    article2_content = read_article("data/article2.txt")

    not_existed_search_pattern = "loremp ipsum dolor sit amet"

    article1_search_pattern = (
        "Стрибки припиняються, коли знайдений елемент більше шуканого."
    )
    article2_search_pattern = "рекомендаційні системи, бази даних, структури даних, програмна імітаційна модель"

    article1_content_kpm_time_success = timeit.timeit(
        lambda: kmp_search(article1_content, article1_search_pattern), number=10
    )
    article1_content_kpm_time_fail = timeit.timeit(
        lambda: kmp_search(article1_content, not_existed_search_pattern), number=10
    )
    article1_content_rabin_karp_time_success = timeit.timeit(
        lambda: rabin_karp_search(article1_content, article1_search_pattern), number=10
    )
    article1_content_rabin_karp_time_fail = timeit.timeit(
        lambda: rabin_karp_search(article1_content, not_existed_search_pattern),
        number=10,
    )
    article1_content_boyer_moore_time_success = timeit.timeit(
        lambda: boyer_moore_search(article1_content, article1_search_pattern), number=10
    )
    article1_content_boyer_moore_time_fail = timeit.timeit(
        lambda: boyer_moore_search(article1_content, not_existed_search_pattern),
        number=10,
    )

    article2_content_kpm_time_success = timeit.timeit(
        lambda: kmp_search(article2_content, article2_search_pattern), number=10
    )
    article2_content_kpm_time_fail = timeit.timeit(
        lambda: kmp_search(article2_content, not_existed_search_pattern), number=10
    )
    article2_content_rabin_karp_time_success = timeit.timeit(
        lambda: rabin_karp_search(article2_content, article2_search_pattern), number=10
    )
    article2_content_rabin_karp_time_fail = timeit.timeit(
        lambda: rabin_karp_search(article2_content, not_existed_search_pattern),
        number=10,
    )
    article2_content_boyer_moore_time_success = timeit.timeit(
        lambda: boyer_moore_search(article2_content, article2_search_pattern), number=10
    )
    article2_content_boyer_moore_time_fail = timeit.timeit(
        lambda: boyer_moore_search(article2_content, not_existed_search_pattern),
        number=10,
    )

    print(
        f"{'|Alogrithm': <20} | {'A1 success': <10} | {'A1 fail': <10} | {'A2 success': <10} | {'A2 fail': <10}|"
    )
    print(f"{'|':-<20} | {'':-<10} | {'':-<10} | {'':-<10} | {'':-<10}|")
    print(
        f"{'|KMP': <20} | {article1_content_kpm_time_success: <10.5f} | {article1_content_kpm_time_fail: <10.5f} | {article2_content_kpm_time_success: <10.5f} | {article2_content_kpm_time_fail: <10.5f}|"
    )
    print(
        f"{'|Rabin-Karp': <20} | {article1_content_rabin_karp_time_success: <10.5f} | {article1_content_rabin_karp_time_fail: <10.5f} | {article2_content_rabin_karp_time_success: <10.5f} | {article2_content_rabin_karp_time_fail: <10.5f}|"
    )
    print(
        f"{'|Boyer-Moore': <20} | {article1_content_boyer_moore_time_success: <10.5f} | {article1_content_boyer_moore_time_fail: <10.5f} | {article2_content_boyer_moore_time_success: <10.5f} | {article2_content_boyer_moore_time_fail: <10.5f}|"
    )
