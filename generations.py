import random


def generate_random_graph(nums: int) -> str:
    list_I = [x + 1 for x in range(nums)]
    list_J = [x + 1 for x in range(nums)]
    list_ans = []

    while len(list_I) > 0 or len(list_J) > 0:
        select = random.randint(0, 1)
        if select == 0 and len(list_I) > 0:
            list_ans.append(list_I[0])
            del list_I[0]
        elif len(list_J) > 0:
            rand_choose = random.randrange(0, len(list_J))
            if list_J[rand_choose] in list_ans:
                list_ans.append(list_J[rand_choose])
                del list_J[rand_choose]

    return ' '.join(list(map(str, list_ans)))
