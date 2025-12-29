def printer_error(s):
    return f"{sum(c > 'm' for c in s)}/{len(s)}"


#Alternativa de código visando manutenibilidade

def printer_error(s):
    max_valid_color = 'm'
    return f"{sum(c > max_valid_color for c in s)}/{len(s)}"