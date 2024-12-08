ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "Word"
dest = list(ft_tuple)
dest[1] = "Turkiye"
ft_tuple = tuple(dest)

ft_set.remove("tutu!")
ft_set.add("Kocaeli")
ft_dict.update({"Hello" : "42Turkiye!"})



print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
