"""Prediction model"""

import pandas as pd
import pickle

def ks_model(bl, cat, cy, gl, loc, name, st, ut, da, db4l):
    """Receives KS info, returns 0 or 1"""
    input = pd.DataFrame({'blurb': bl,
                          'category':cat,
                          'country':cy,
                          'goal':gl,
                          'location':loc,
                          'name':name,
                          'state':st,
                          'usd_type':ut,
                          'days_allotted':da,
                          'days_before_launch':db4l})
    
    ks_file = "ks_model.sav"
    model = pickle.load(open(ks_file, 'rb'))

    outcome = round(model.predict(input))
    
    return outcome
