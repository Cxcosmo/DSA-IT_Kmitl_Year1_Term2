def convert_string_to_tuples(text_in):
  values = text_in.strip('()').split(', ')
  values[0], values[1] = values[1], values[0]
  return tuple(map(float, values))

laongdao_data = convert_string_to_tuples(input())
print(laongdao_data)
