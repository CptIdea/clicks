def get_clicks_color(clicks):
    ans = {}
    for click in clicks:
        current_colors = set({})
        for x in click:
            if x in ans:
                current_colors.add(ans[x])
            if ans.get(x) is None:
                color = 1
                while color in current_colors:
                    color += 1
                ans[x] = color
                current_colors.add(color)


    return ans