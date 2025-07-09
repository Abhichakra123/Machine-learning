def count_frequency(String):
  list_str=list(String)
  list_unique_str=list(set(String))
  count_list=[]
  for i in list_unique_str:
    result=list_str.count(i)
    count_list+=[result]
  max_num=max(count_list)
  get_index=count_list.index(max_num)
  letter=list_unique_str[get_index]
  return letter,max_num
String="hippopotamus"
letter,num=count_frequency(String)
print("{} is repeated {} and is the most repeated one".format(letter,num))