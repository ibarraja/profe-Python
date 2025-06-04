import sys

class Conversiones: 
    
    def main():
        argumentos = sys.argv[1:]
        for arguemento in argumentos:
            num = int(arguemento)
            cadena_binaria = Conversiones.convertir_decimal_to_str_binaria(num)
            if cadena_binaria == None:
                print(f"Error > no se puede convertir {num}")
            else:
                # print(cadena_binaria)
                mascara_decimal = Conversiones.convertir_str_binaria_to_str_decimal(cadena_binaria)
                Conversiones.imprimir(num, cadena_binaria, mascara_decimal)            
            
    
    def convertir_decimal_to_str_binaria(num:int) -> str:
        """
        Comprueba si `num` está dentro del rango [0:32]
        Obtiene una cadena de texto con tantos '1' como se indican. 
        Se separa por '.' cada vez que se completa un octeto, excepto el último.

        Devuelve la cadena de texto 'mascara_binario' o mensaje de error.
        """
        if 0 <= num <= 32:
            cadena_binaria = ""
            
            # 11111111.10000000.00000000.0000000
            for i in range(32):
                if i < num:
                    cadena_binaria += "1"
                else:
                    cadena_binaria += "0"
                if i == 7 or i == 15 or i == 23:
                    cadena_binaria += "."
            
            return cadena_binaria
        


    def convertir_str_binaria_to_str_decimal(mascara_binario:str) -> str:
        """
        Convierte los octetos de una str en numeros decimales.

        Devuelve cadena de texto: 'mascara_decimal'.
        """
        octetos_binarios = mascara_binario.split(".")
        mascara_decimal = ""
        for octeto in octetos_binarios:
            num_decimal = int(octeto, 2)
            mascara_decimal += str(num_decimal)
            mascara_decimal += "."
        if mascara_decimal.endswith("."):
            mascara_decimal = mascara_decimal[:-1]
        return mascara_decimal
        
        

    def imprimir(num, mascara_binario, mascara_decimal) -> str:
        """
        Imprime el siguiente formato:
        num | mascara_binario | mascara_decimal
        """
        print(f"{num} | {mascara_binario} | {mascara_decimal}")


if __name__ == "__main__":
    Conversiones.main()