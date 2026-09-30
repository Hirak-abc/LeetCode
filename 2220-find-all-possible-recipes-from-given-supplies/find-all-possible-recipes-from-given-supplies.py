class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):

        g = dict(zip(recipes, ingredients))
        have = set(supplies)
        state = {}
        ans = []

        def dfs(recipe):

            if recipe in have:
                return True

            if state.get(recipe) == 1:
                return False

            if state.get(recipe) == 2:
                return True

            if state.get(recipe) == 3:
                return False

            state[recipe] = 1

            for x in g[recipe]:

                if x not in have:

                    if x not in g or not dfs(x):
                        state[recipe] = 3
                        return False

            state[recipe] = 2
            have.add(recipe)
            return True

        for recipe in recipes:
            if dfs(recipe):
                ans.append(recipe)

        return ans