# import re
# Description  = r"Beginning at the East Quarter corner of Section 3, thence South 968 feet, thence North 56°15' West 452 feet, thence North 69° West 256 feet, thence South 85° West 420 feet, thence North 69°30' West 201 feet, thence North 58°60' West 145 feet, thence North 27°45' West 489 feet, thence North 16°0'30"+'"'+" West 85 feet, thence East 1,595.6 feet to the place of beginning."
# # Get actions
# pattern = re.compile(
#     r'.hence.(North|South|East|West|N|S|E|W|north|south|east|west).\d{1,4}.{0,2}\d{0,2}.{0,2}\d{0,2}.{0,3}(North|South|East|West|N|S|E|W|north|south|east|west){0,5}.{0,1}\d{0,4}.{0,1}\d{0,2}.(feet|rods|chains|Feet|ft|Rods)')
# matches = pattern.finditer(Description)
# matches1 = ''
# matchlist = []
# for match in matches:
#     matches1 += '\n' + match.group()
#     matchlist.append(match.group())
#
# match_split = []
# for item in matchlist:
#     # match_split.append((re.split(r"[\s°º’′'\"][\s]{0,1}", item))) # THIS INCLUDES " - don't know how to get it to add space after
#     match_split.append((re.split(r"[\s°º’′'\"]", item)))
#     #match_split.append((re.split(r"[\s]", item)))
#
#
# for i in range(len(match_split)):
#     if len(match_split[i]) < 5 and (
#             match_split[i][1] == 'North' or match_split[i][1] == 'N' or match_split[i][1] == 'n' or match_split[i][
#         1] == 'north' or match_split[i][1] == 'South' or match_split[i][1] == 's' or match_split[i][1] == 'south' or
#             match_split[i][1] == 'S'):
#         match_split[i].insert(2, '0')
#         match_split[i].insert(3, '0')
#         match_split[i].insert(4, '0')
#         match_split[i].insert(5, '0')
#     elif len(match_split[i]) < 5 and (
#             match_split[i][1] == 'East' or match_split[i][1] == 'E' or match_split[i][1] == 'e' or match_split[i][
#         1] == 'east' or match_split[i][1] == 'West' or match_split[i][1] == 'W' or match_split[i][1] == 'west' or
#             match_split[i][1] == 'w'):
#         match_split[i].insert(1, '0')
#         match_split[i].insert(2, '0')
#         match_split[i].insert(3, '0')
#         match_split[i].insert(4, '0')
#
# for list in match_split:
#     if len(list) == 9:
#         del list[5]
#     if len(list) == 7:
#         list.insert(4,'')
#
# for list in match_split:
#     if list[7] in ('rods', 'Rods', 'rod', 'Rod'):
#         list[6] = str(float(list[6]) * 16.5)
#         list[7] = 'feet'
#
# for list in match_split:
#     list.remove('thence')
#     try:
#         list.remove('feet')
#     except ValueError:
#         list.remove('ft')




arr = [4,3,1,2]
#arr = [2, 31, 1, 38, 29, 5, 44, 6, 12, 18, 39, 9, 48, 49, 13, 11, 7, 27, 14, 33, 50, 21, 46, 23, 15, 26, 8, 47, 40, 3, 32, 22, 34, 42, 16, 41, 24, 10, 4, 28, 36, 30, 37, 35, 20, 17, 45, 43, 25, 19]
print(arr[::-2])