"""Prediction model"""

import pandas as pd
import pickle
from joblib import dump, load


def ks_model(blurb, category, country, goal, location, name, state, usd_type, days_allotted, days_before_launch):
    """Receives KS info, returns 0 or 1"""
    input = pd.DataFrame({'blurb':[blurb],
                          'category':[category],
                          'country':[country],
                          'goal':[goal],
                          'location':[location],
                          'name':[name],
                          'state':[state],
                          'usd_type':[usd_type],
                          'days_allotted':[days_allotted],
                          'days_before_launch':[days_before_launch]})
    
    ks_file = "ks/ks_model.sav"
    
    # loaded_model = load(ks_file)
    model = pickle.load(open(ks_file, 'rb'))

    outcome = loaded_model.predict(input)

    return outcome
