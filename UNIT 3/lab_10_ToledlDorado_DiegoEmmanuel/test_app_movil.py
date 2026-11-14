import pytest

from app_movil import (
    PerfilMovil,
    PerfilPro,
    PuntosInsuficientesError,
    SuscripcionExpiradaError,
)



@pytest.fixture
def perfil():
    """Instancia estándar de PerfilMovil para cada prueba."""
    return PerfilMovil("diego")


@pytest.fixture
def perfil_pro():
    """Instancia estándar de PerfilPro con 1 mes de suscripción."""
    return PerfilPro("diego_pro", meses_suscripcion=1)



def test_atributos_iniciales(perfil):
    assert perfil.username == "diego"
    assert perfil.gemas == 50
    assert perfil.racha_dias == 1
    assert perfil.notificaciones_activas is True


def test_ganar_gemas_suma_correctamente(perfil):
    assert perfil.ganar_gemas(25) == 75
    assert perfil.gemas == 75


def test_gastar_gemas_resta_correctamente(perfil):
    assert perfil.gastar_gemas(20) == 30
    assert perfil.gemas == 30


def test_gastar_todo_el_saldo(perfil):
    assert perfil.gastar_gemas(50) == 0


def test_transacciones_consecutivas(perfil):
    perfil.ganar_gemas(10)   
    perfil.gastar_gemas(15)  
    perfil.ganar_gemas(5)    
    assert perfil.gemas == 50



def test_gemas_iniciales_negativas():
    with pytest.raises(ValueError):
        PerfilMovil("error", gemas=-10)


def test_gastar_mas_de_lo_disponible(perfil):
    with pytest.raises(PuntosInsuficientesError):
        perfil.gastar_gemas(100)
    assert perfil.gemas == 50  


@pytest.mark.parametrize("cantidad", [0, -1, -50])
def test_gastar_cantidad_no_positiva(perfil, cantidad):
    with pytest.raises(ValueError):
        perfil.gastar_gemas(cantidad)


def test_pro_meses_invalidos():
    with pytest.raises(ValueError):
        PerfilPro("error", meses_suscripcion=0)


def test_descarga_con_suscripcion_expirada(perfil_pro):
    perfil_pro.pasar_mes()  
    with pytest.raises(SuscripcionExpiradaError):
        perfil_pro.descargar_contenido_offline()
    assert perfil_pro.es_pro is False



@pytest.mark.parametrize("cantidad, esperado", [
    (1, 51),        
    (10, 60),
    (50, 100),
    (1000, 1050),   
])
def test_ganar_gemas_validas(perfil, cantidad, esperado):
    assert perfil.ganar_gemas(cantidad) == esperado


@pytest.mark.parametrize("cantidad", [0, -1, -100])
def test_ganar_gemas_invalidas(perfil, cantidad):
    with pytest.raises(ValueError):
        perfil.ganar_gemas(cantidad)



def test_perfil_pro_hereda_de_perfil_movil(perfil_pro):
    assert isinstance(perfil_pro, PerfilPro)
    assert isinstance(perfil_pro, PerfilMovil)
    assert issubclass(PerfilPro, PerfilMovil)


def test_perfil_movil_no_es_pro(perfil):
    assert not isinstance(perfil, PerfilPro)


def test_excepciones_heredan_de_exception():
    assert issubclass(SuscripcionExpiradaError, Exception)
    assert issubclass(PuntosInsuficientesError, Exception)


def test_ciclo_de_vida_perfil_pro():
    pro = PerfilPro("ana", meses_suscripcion=2)
    assert pro.es_pro is True
    assert pro.gemas == 50  
    assert pro.descargar_contenido_offline() == "Descarga completada con éxito."

    pro.pasar_mes()  
    assert pro.descargar_contenido_offline() == "Descarga completada con éxito."

    pro.pasar_mes()  
    with pytest.raises(SuscripcionExpiradaError):
        pro.descargar_contenido_offline()
    assert pro.es_pro is False


def test_pro_hereda_metodos_de_gemas(perfil_pro):
    assert perfil_pro.ganar_gemas(10) == 60
    assert perfil_pro.gastar_gemas(60) == 0
