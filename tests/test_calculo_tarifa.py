def test_calculo_tarifa():
    # Definir los datos de entrada
    distancia = 10
    tarifa_por_km = 2

    # Ejecutar el cálculo
    tarifa_total = distancia * tarifa_por_km

    # Verificar el resultado
    assert tarifa_total == 20