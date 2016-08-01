def get_bal_locations(span, bal_width=1.625, centered=True, gap=4):
  if centered:
    start = gap + (bal_width / 2)
    iter_val = (bal_width / 2)
  else:
    start = gap
    iter_val = bal_width
  locations = [start]
  i = start
  while i < span:
    i += iter_val + gap
    locations.append(i)
  return locations