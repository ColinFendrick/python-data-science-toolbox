fellowship = ['frodo', 'samwise', 'merry', 'pippin',
              'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

result = filter(lambda member: len(member) > 6, fellowship)
result_list = list(result)
print(result_list)
