import re

class Lexer:
    def _init_(self, code):
        self.code = code
        self.position = 0
        self.tokens = []
        
        # Definición de las 8 categorías léxicas con sus expresiones regulares
        self.token_specs = [
            ('NUMBER',    r'\d+(\.\d+)?'),     # Números enteros y decimales
            ('IDENTIFIER', r'[a-zA-Z_]\w*'),  # Identificadores (variables)
            ('OPERATOR', r'[+\-*/=<>!&|]+'),   # Operadores
            ('STRING',    r'"[^"]"|\'[^\']\''), # Cadenas de texto
            ('COMMENT',   r'//.|/\.?\/'),  # Comentarios
            ('KEYWORD',   r'\b(if|else|while|for|return|function|var)\b'), # Palabras clave
            ('PUNCTUATION', r'[(),;:{}[\]]'),  # Signos de puntuación
            ('WHITESPACE', r'\s+')             # Espacios en blanco
        ]
        
        # Compilar todas las expresiones regulares
        self.token_regex = '|'.join('(?P<%s>%s)' % pair for pair in self.token_specs)
        self.re_token = re.compile(self.token_regex)
    
    def tokenize(self):
        for match in self.re_token.finditer(self.code):
            kind = match.lastgroup
            value = match.group()
            
            # Ignorar espacios en blanco y comentarios si lo deseas
            if kind == 'WHITESPACE' or kind == 'COMMENT':
                continue
                
            self.tokens.append((kind, value))
        
        return self.tokens

# Ejemplo de uso
code = """
function suma(a, b) {
    // Esto es un comentario
    if (a > 0 && b > 0) {
        return a + b;
    }
    return "Error: números deben ser positivos";
}

var resultado = suma(5, 3.14);
"""

lexer = Lexer(code)
tokens = lexer.tokenize()

# Mostrar los tokens encontrados
for token in tokens:
    print(f"{token[0]:<12} => {token[1]}")