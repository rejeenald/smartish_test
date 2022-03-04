import argparse
from argument_parser import KeyValueArgumentParser
from api_settings import * 
import datetime
import json
import pandas as pd
import requests
import sys
import time

PARAMETERS = ['creation_date_range',  'article_id']


class APIDataScript:
    def __init__(self, filters:dict={}, save_to:str='', *args, **kwargs) -> None:
        self.api_data = self._extract_api_data()
        self.filters = filters
        self.supported_filter_parameters = PARAMETERS

    @property
    def clean_data(self):
        items_df= pd.DataFrame(self.api_data)
        return self._clean_data(items_df, self.filters)

    def _extract_api_data(self):
        api_data = self._request_api_data()
        if api_data:
            return api_data.get('items')
        return

    def _request_api_data(self):
        response = requests.get(API_URL)
        return response.json()

    def _clean_data(self, api_df, filters):
        final_data = pd.DataFrame()
        for filter_param, filter_value in filters.items():
            if filter_param in self.supported_filter_parameters:
                api_df = self._process_clean_data_by_filter(api_df, filter_param, filter_value)
            else:
                print(f"Error: '{filter_param}' is not on the list of valid filter parameters: {self.supported_filter_parameters}")
                print(f"Error: Please select valid filter parameters in this list:{self.supported_filter_parameters}.")
        return api_df

    def _process_clean_data_by_filter(self, api_df, filter_param, filter_value):
        if filter_param == 'creation_date_range':
            api_df['creation_date'] = api_df.apply(lambda x: self._convert_to_readable_date(x.creation_date), axis=1)
            date_range = filter_value.split("-")
            start_date, end_date = self._format_dates(date_range)
            return api_df[(api_df.creation_date >= start_date) & (api_df.creation_date <= end_date)]
        elif filter_param == 'article_id':
            return api_df[api_df.article_id == int(filter_value)]
        else:
            print("Filter parameter is not yet supported.")
            return

    def _format_dates(self, date_range):
        sd = "-".join(date_range[0].split("/"))
        ed = "-".join(date_range[1].split("/"))
        return sd, ed

    def _convert_to_readable_date(Self, epoch_date):
        return time.strftime('%Y-%m-%d', time.localtime(epoch_date))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--kwargs', nargs='*', action = KeyValueArgumentParser)
    args = parser.parse_args()
    save_to = args.kwargs.pop('save_to')
    filter_params = args.kwargs
    s = APIDataScript(filters=filter_params, save_to=save_to)
    clean_data = s.clean_data
    clean_data.to_csv(save_to, index=False)
    
