from ft_filter import ft_filter
import sys
def filterstring():
    s = sys.argv[1]
    n = int(sys.argv[2])
    assert isinstance(s, str)
    assert isinstance(n, int)
    
    words = s.split()
    result = ft_filter(lambda word: len(word) > n, words)
    print(result)


def main():
    try:
        filterstring()
    except Exception as e:
        print(f"{e}")


if __name__ == "__main__":
    main()