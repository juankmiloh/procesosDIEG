import pandas as pd
import numpy as np
import datetime
from flask import abort
from ..repository import InformeRepository
from ..util.web_util import to_date
from ..util.web_util import add_wrapper

class InformeService:

    def get_informe(self, informe_repository: InformeRepository):
        informe = []
        data = informe_repository.get_informe_bd()
        for result in data:
            informe.append(
                {
                    'idempresa': result[0],
                    'name': result[1],
                    'value': result[2],
                }
            )
        return informe