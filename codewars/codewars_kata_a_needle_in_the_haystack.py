def find_needle(haystack):
    try:
        return f"found the needle at position {haystack.index('needle')}"
    except ValueError:
        return f'no needle found'




#Aplicação mais robusta sugerida pelo Gemini
def find_all_needles(haystack):
    return [item for item, valor in enumerate(haystack) if valor == 'needle']