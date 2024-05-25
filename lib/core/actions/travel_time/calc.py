from lib.core.actions.base import BaseAction
from lib.core.entities.travel_time import TravelTime

from typing import List
from obspy.taup import TauPyModel

calc_model = TauPyModel(model="iasp91")

class CalcTraveTimeAction(BaseAction):
    def __init__(self, depth_km, distance_degree):
        self.depth_km = depth_km
        self.distance_degree = distance_degree

        super().__init__()

    async def handle(self) -> List[TravelTime]:
        arrivals = calc_model.get_travel_times(source_depth_in_km=self.depth_km,

                                  distance_in_degree=self.distance_degree)
        res = []
        for arrival in arrivals:
            res.append(TravelTime(arrival.phase.name, arrival.time))
        return res
        