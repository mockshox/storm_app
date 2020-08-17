from zeep import Client, helpers

import os


def _get_storm_info(app, app_config):
    client = Client(app_config.wsdl_file)
    api_key = os.environ.get('STORM_INFO_API_KEY')
    
    app.logger.info('Fetching storm info')
    xy = client.service.miejscowosc(app_config.city, api_key)
    storm_data = client.service.szukaj_burzy(xy['y'], xy['x'],
                                             app_config.range_detect,
                                             api_key)
    return helpers.serialize_object(storm_data)


def is_storm_in_location(app, app_config):
    storm_info = _get_storm_info(app, app_config)
    return "NIE" if storm_info['liczba'] < 1 else "TAK"
