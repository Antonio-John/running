import pandas as pd
from src.read_and_merge_tools import get_dates_df


def test_get_dates_df():

    output_df=pd.DataFrame({'date':[pd.to_datetime('10/12/2019'),
                                    pd.to_datetime('10/13/2019'),
                                    pd.to_datetime('10/14/2019')]})

    result=get_dates_df("10/14/2019")

    pd.testing.assert_frame_equal(output_df,result)






