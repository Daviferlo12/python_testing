import sys
import os

# Agregar la carpeta raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

class InsuficientFoundError(Exception):
    pass

class WithdrawalTimeRestrictionError(Exception):
    pass

class WithdrawalWeekendRestriccion(Exception):
    pass