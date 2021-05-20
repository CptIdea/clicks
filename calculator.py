def get_clicks(input_nums):
    counter = -1
    sets_I_nom = 0
    sets_J_nom = 0

    sets_I = [set({}) for _ in range(len(input_nums))]
    sets_J = [set({}) for _ in range(len(input_nums))]
    uses = set({})
    anti_uses = set({})

    for num in input_nums:
        counter += 1
        if not num in uses:
            sets_J_nom += 1
            sets_I[sets_I_nom].add(num)
            uses.add(input_nums[counter])
            continue
        if not num in anti_uses:
            sets_I_nom += 1
            sets_J[sets_J_nom].add(num)
            anti_uses.add(input_nums[counter])
            continue

    sets_I = [click for click in sets_I if len(click) > 0]
    sets_J = [click for click in sets_J if len(click) > 0]

    clicks = []
    for i in range(len(sets_I)):
        if i == 0:
            clicks.append(sets_I[i])
        else:
            clicks.append(
                clicks[i - 1].union(sets_I[i]).difference(sets_J[i - 1])
            )

    return clicks


