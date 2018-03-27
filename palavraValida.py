#89453 - Guilherme Peixoto
def artigo_def(letra):
    return letra == "A" or letra == "O"

def vogal_palavra(letra):
    return artigo_def(letra) or letra == "E"

def vogal(letra):
    return letra == "I" or letra == "U" or vogal_palavra(letra)

def ditongo_palavra(letras):
    lista = ["AI", "AO", "EU", "OU"]
    return letras in lista

def ditongo(letras):
    lista = ["AE", "AU", "EI", "OE", "OI", "IU"]
    return letras in lista or ditongo_palavra(letras)

def par_vogais(letras):
    return ditongo(letras) or letras == "IA" or letras == "IO"

def consoante_freq(letra):
    lista = ["D", "L", "M", "N", "P", "R", "S", "T", "V"]
    return letra in lista

def consoante_terminal(letra):
    lista = ["L", "M", "R", "S", "X", "Z"]
    return letra in lista

def consoante_final(letra):
    return letra == "N" or letra == "P" or consoante_terminal(letra)

def consoante(letra):
    lista = ["B", "C", "D", "F", "G", "H", "J", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "X", "Z"]
    return letra in lista

def par_consoantes(letras):
    lista = ["BR", "CR", "FR", "GR", "PR", "TR", "VR", "BL", "CL", "FL", "GL", "PL"]
    return letras in lista

def monossilabo_2(letras):
	if len(letras) == 2:    
	    lista = ["AR", "IR", "EM", "UM"]
	    return (letras in lista) \
	    or (vogal_palavra(letras[0]) and letras[1] == "S") \
	    or ditongo_palavra(letras) \
	    or (consoante_freq(letras[0]) and vogal(letras[1]))
	else:
		return False

def monossilabo_3(letras):
    if len(letras) == 3:	
    	return (consoante(letras[0]) and vogal(letras[1]) and consoante_terminal(letras[2])) \
    	or (consoante(letras[0]) and ditongo(letras[1:])) \
    	or (par_vogais(letras[:2]) and consoante_terminal(letras[2]))
    else:
    	return False

def e_monossilabo(letras):
    if not isinstance(letras, str):
        raise ValueError("e_monossilabo:argumento invalido")
    else:
        tamanho = len(letras)
        if tamanho == 1:
            return vogal_palavra(letras)
        elif tamanho == 2:
            return monossilabo_2(letras)
        elif tamanho == 3:
            return monossilabo_3(letras)
        else:
            return False

def silaba_2(letras):
    if len(letras) == 2:	
    	return par_vogais(letras) \
    	or (consoante(letras[0]) and vogal(letras[1])) \
    	or (vogal(letras[0]) and consoante_final(letras[1]))
    else:
    	return False

def silaba_3(letras):
    if len(letras) == 3:	
    	lista = ["QUA", "QUE", "QUI", "GUE", "GUI"]
    	return letras in lista or (vogal(letras[0]) and letras[1:] == "NS") \
    	or (consoante(letras[0]) and par_vogais(letras[1:])) \
    	or (consoante(letras[0]) and vogal(letras[1]) and consoante_final(letras[2])) \
    	or (par_vogais(letras[:2]) and consoante_final(letras[2])) \
    	or (par_consoantes(letras[:2]) and vogal(letras[2]))
    else:
    	return False

def silaba_4(letras):
	if len(letras) == 4:
		return (par_vogais(letras[:2]) and letras[2:] == "NS") \
		or (consoante(letras[0]) and vogal(letras[1]) and letras[2:] == "NS") \
		or (consoante(letras[0]) and vogal(letras[1]) and letras[2:] == "IS") \
		or (par_consoantes(letras[:2]) and par_vogais(letras[2:]) \
		or (consoante(letras[0]) and par_vogais(letras[1:3]) and consoante_final(letras[3])))
	else:
		return False

def silaba_5(letras):
    if len(letras) == 5:
        return par_consoantes(letras[:2]) and vogal(letras[2]) and letras[3:] == "NS"
    else:
        return False

def silaba_final(letras):
    return monossilabo_2(letras) or monossilabo_3(letras) or silaba_4(letras) or silaba_5(letras)

def e_silaba(letras):
    if isinstance(letras, str):
        return vogal(letras) or silaba_2(letras) or silaba_3(letras) or silaba_4(letras) or silaba_5(letras)
    else:
        raise ValueError("e_silaba:argumento invalido")

def e_palavra(palavra):
    def verificar_silabas(silabas):
        memo = {}
        if silaba_final(silabas):
            return True
        else:
            for i in range(min(len(palavra), 5)): #silabas so podem ter 5 caracteres
                silaba_atual = silabas[:i+1]
                if silaba_atual in memo or e_silaba(silaba_atual):
                    if silaba_atual not in memo: memo[silaba_atual] = 1
                    if verificar_silabas(silabas[i+1:]):
                        return True

            return False


    if not isinstance(palavra, str):
        raise ValueError("e_palavra:argumento invalido")
    else:
        if e_monossilabo(palavra):
            return True
        
        return verificar_silabas(palavra)
