"""
Copyright (C) 2013-2017 Calliope contributors listed in AUTHORS.
Licensed under the Apache 2.0 License (see LICENSE file).

objective.py
~~~~~~~~~~~~

Objective functions.

"""

import pyomo.core as po  # pylint: disable=import-error


def cost_minimization(backend_model):
    """
    Minimizes total system monetary cost.

    """
    def obj_rule(backend_model):
        return sum(
            backend_model.cost[loc_tech, 'monetary']
            for loc_tech in backend_model.loc_techs_cost
        )

    backend_model.obj = po.Objective(sense=po.minimize, rule=obj_rule)
    backend_model.obj.domain = po.Reals
