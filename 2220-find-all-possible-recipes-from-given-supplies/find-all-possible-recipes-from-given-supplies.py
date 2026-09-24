class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        have = set(supplies)
        ing = dict(zip(recipes, ingredients))
        state = {}

        def dfs(r):
            if r in have:
                return True
            if r not in ing:
                return False
            if state.get(r) == 1:
                return False
            if state.get(r) == 2:
                return True

            state[r] = 1

            for x in ing[r]:
                if not dfs(x):
                    return False

            state[r] = 2
            have.add(r)
            return True

        return [r for r in recipes if dfs(r)]