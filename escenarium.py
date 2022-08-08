import copy

if __name__ == "__main__":
    print("Este archivo no se puede utilizar tal cual. Debes importarlo en navecitas.py")

class GeneradorDeEscenarios():
    filaConParedes = list("#####################")
    filaConLaterales = list("#                   #")
    filaConLateralescortina = list("#                 #")
    escenario = (
        filaConParedes.copy(),
        filaConLateralescortina.copy(),
        filaConLaterales.copy(),
        filaConLaterales.copy(),
        filaConLaterales.copy(),
        filaConLaterales.copy(),
        filaConLaterales.copy(),
        filaConLaterales.copy(),
        filaConLateralescortina.copy(),
        filaConParedes.copy(),
    )

    def generarEscenario(self):
        return copy.deepcopy(self.escenario)
