

def ft_tqdm(lst: range) -> None:
    total = len(lst)
    for i, item in enumerate(lst):
        percent = int((i + 1) / total * 100)
        bar_length = 100 
        filled_length = int(bar_length * (i + 1) // total)
        bar = '=' * filled_length + '>' + ' ' * (bar_length - filled_length)
        
        print(f'\r {percent}% | [{bar}] {i + 1}/{total}', end=' ')

        yield item
    print()
    
