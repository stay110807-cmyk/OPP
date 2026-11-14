class SuscripcionExpiradaError(Exception):
    pass


class PuntosInsuficientesError(Exception):
    pass


class PerfilMovil:
    def __init__(self, username: str, gemas: int = 50,
                 racha_dias: int = 1, notificaciones_activas: bool = True):
        if gemas < 0:
            raise ValueError("Las gemas no pueden ser negativas.")
        self.username = username
        self.gemas = gemas
        self.racha_dias = racha_dias
        self.notificaciones_activas = notificaciones_activas

    def ganar_gemas(self, cantidad: int) -> int:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser estrictamente positiva.")
        self.gemas += cantidad
        return self.gemas

    def gastar_gemas(self, cantidad: int) -> int:
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser estrictamente positiva.")
        if cantidad > self.gemas:
            raise PuntosInsuficientesError(
                f"Saldo insuficiente: tienes {self.gemas} gemas y "
                f"intentas gastar {cantidad}."
            )
        self.gemas -= cantidad
        return self.gemas



class PerfilPro(PerfilMovil):
    def __init__(self, username: str, meses_suscripcion: int, gemas: int = 50,
                 racha_dias: int = 1, notificaciones_activas: bool = True):
        super().__init__(username, gemas, racha_dias, notificaciones_activas)
        if meses_suscripcion <= 0:
            raise ValueError("El periodo de suscripción debe ser mayor que cero.")
        self.meses_suscripcion = meses_suscripcion
        self.es_pro = True

    def pasar_mes(self) -> int:
        if self.meses_suscripcion > 0:
            self.meses_suscripcion -= 1
        return self.meses_suscripcion

    def descargar_contenido_offline(self) -> str:
        if self.meses_suscripcion <= 0:
            self.es_pro = False
            raise SuscripcionExpiradaError(
                "Tu suscripción Pro ha expirado. Renueva para descargar contenido."
            )
        return "Descarga completada con éxito."
