"""Problem 4

Replace every character in a list with `repl_chr` except `ret_chr`.
"""

test_list = ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T']
repl_chr = '*'
ret_chr = 'G'
new_list = [ch if ch == ret_chr else repl_chr for ch in test_list]
print(new_list)
 
test_list = ['G', 'F', 'G', 'B', 'E', 'S', 'T']
new_list = [ch if ch == ret_chr else repl_chr for ch in test_list]
print(new_list)

