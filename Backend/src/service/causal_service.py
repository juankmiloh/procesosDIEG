import pandas as pd
import numpy as np
import datetime
from flask import abort
from ..repository import CausalRepository
from ..util.web_util import to_date
from ..util.web_util import add_wrapper

class CausalService:

    def get_causal(self, causal_repository: CausalRepository):
        causal = []
        data = causal_repository.get_causal_bd()
        for result in data:
            causal.append(
                {
                    'idcausal': result[0],
                    'nombre': result[1],
                }
            )
        return causal