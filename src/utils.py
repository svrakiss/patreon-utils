from enum import Enum
import inspect
import logging
import traceback
from typing import Optional

_log = logging.getLogger().getChild(__name__)

def generate_highest_tier(self=None):
        """Generate the highest tier"""
        def helper(my_tiers:Optional[list[str]]):
            if my_tiers and len(my_tiers)>0:
                tiers=['Supreme Kimochi Counsellor','Envoy of Lewdness','Minister of Joy']
                my_index = {val:i for i,val in enumerate(tiers)}
                return min( my_tiers,key=lambda x:my_index.get(x,10))
            return None

        if self is None:
            frame = inspect.currentframe()
            try:
                the_important_frame= frame.f_back.f_back
                if the_important_frame.f_code.co_name == '__init__':
                    # looking at the name of the function
                    # this is being called from the constructor, so the tier list is 
                    # in the attributes dictionary
                    tier = the_important_frame.f_locals.get('attributes',{'tier':None})
                    return helper(tier.get("tier"))
            except KeyError:
                _log.error(traceback.format_exc())
            finally:
                del frame
            return None
        return helper(self.tier)
class tier_enum(Enum):
    TIER_1 = (1, 'Supreme Kimochi Counsellor','SKC')
    TIER_2 = (2,'Envoy of Lewdness','EoL')
    TIER_3 = (3, 'Minister of Joy','MoJ')
    def __init__(self,order:int,name:str,code:str) -> None:
        self._order=order
        self._name=name
        self.code =code
    @property
    def order(self):
        return self._order
    @property
    def name(self):
        return self._name
    def __lt__(self,other):
        return self._order < other._order
    @classmethod
    def get(cls,name,default=None):
        try:
            return cls[name]
        except KeyError:
            return default
