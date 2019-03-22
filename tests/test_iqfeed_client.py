import datetime
import pkgutil
import time

import pyiqfeed as iq
import pyiqfeed.service
import pytest


@pytest.fixture(scope="session")
@pytest.mark.timeout(300)
def wait_for_iqfeed():
    while not pyiqfeed.service._is_iqfeed_running():
        time.sleep(1)


def test_can_pull_data_from_specific_time_period():
    results = pkgutil.get_data("tests.data", "SPY_20190311_to_20190318.txt").decode("utf-8")

    hist_conn = iq.HistoryConn(name="pyiqfeed-Example-tickdata")
    hist_listener = iq.VerboseIQFeedListener("History Tick Listener")
    hist_conn.add_listener(hist_listener)

    with iq.ConnConnector([hist_conn]) as connector:
        data = hist_conn.request_ticks_in_period(
            ticker="SPY",
            bgn_prd=datetime.datetime(
                year=2019,
                month=3,
                day=11,
                hour=9,
                minute=30
            ),
            end_prd=datetime.datetime(
                year=2019,
                month=3,
                day=18,
                hour=9,
                minute=30
            ),
            max_ticks=100
        )

        print(data)
        assert results == str(data)
