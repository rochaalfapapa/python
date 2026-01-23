def solution(text: str, ending: str) -> bool:
    return text.endswith(ending)

#Solução com slicing
def solution(text: str, ending: str) ->  bool:
    if not ending:
        return True
    return text[-len(ending):] == ending