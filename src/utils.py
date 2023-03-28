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
                match the_important_frame.f_code.co_name:
                    # looking at the name of the function
                    case '__init__':
                        # this is being called from the constructor, so the tier list is 
                        # in the attributes dictionary
                        tier = the_important_frame.f_locals.get('attributes',{'tier':None})
                        return helper(tier.get("tier"))
                    case '_container_deserialize':
                        # this is being called when retrieved from a query
                        return None
                    case _:
                        return None
            except KeyError:
                _log.error(traceback.format_exc())
            finally:
                del frame
            return None
        return helper(self.tier)
