import requests
import json
from workutil.config import (
    API_KEY, MAP_SECTION, HOME_ID, WORK_ID, WorkUtilConfig
)
from workutil.utils import color_text


class GoogleMap(object):
    def __init__(self, config=WorkUtilConfig().config):
        self.api_key = config[MAP_SECTION][API_KEY]
        self.home = config[MAP_SECTION][HOME_ID]
        self.work = config[MAP_SECTION][WORK_ID]

    def _from_a_to_b(self, a_location, b_location):
        request_url = "https://maps.googleapis.com/maps/api/" + \
                      "distancematrix/json?origins=place_id:{}&" + \
                      "destinations=place_id:{}&departure_time=now&key={}"
        response = requests.get(request_url.format(
            a_location, b_location, self.api_key
        ))
        r = json.loads(response.text)
        info = r['rows'][0]['elements'][0]
        duration = info['duration']['text']
        duration_in_traffic = info['duration_in_traffic']['text']

        d_float = float(duration.split(" ")[0])
        dit_float = float(duration_in_traffic.split(" ")[0])
        if dit_float < d_float * 1.2:
            color = "GREEN"
        elif dit_float < d_float * 1.6:
            color = "YELLOW"
        else:
            color = "RED"

        colored_duration = color_text(duration_in_traffic, color, "BOLD")
        return colored_duration

    def from_work_to_home(self):
        return self._from_a_to_b(self.work, self.home)

    def from_home_to_work(self):
        return self._from_a_to_b(self.home, self.work)


if __name__ == '__main__':
    gm = GoogleMap()
    go_home_time = gm.from_work_to_home()
    print(go_home_time)
    go_work_time = gm.from_home_to_work()
    print(go_work_time)
