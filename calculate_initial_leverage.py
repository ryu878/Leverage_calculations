def calculate_initial_leverage(final_leverage, n):
    """
    Calculates the initial leverage after n averaging steps (each doubling the position).
    Calcula el apalancamiento inicial después de n promedios (cada uno duplica la posición).
    
    :param final_leverage: The desired final leverage. / El apalancamiento final deseado.
    :param n: The number of averaging steps. / El número de promedios.
    :return: The initial leverage. / El apalancamiento inicial.
    """
    return final_leverage / (2 ** n)

# Parameters / Parámetros
final_leverage = 10  # Final leverage to achieve / Apalancamiento final a alcanzar
n = 8  # Number of averaging steps / Número de promedios

# Calculation / Cálculo
initial_leverage = calculate_initial_leverage(final_leverage, n)

# Output result / Imprimir resultado
print(f"Initial leverage: {initial_leverage:.6f}")  # Apalancamiento inicial
