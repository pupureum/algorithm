def solution(nums):
    pokemons = set(nums)
    return min(len(nums)/2, len(pokemons))

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))