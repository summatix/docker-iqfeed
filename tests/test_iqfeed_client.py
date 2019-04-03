import datetime
import os
import pkgutil
import time

import pyiqfeed as iq
import pyiqfeed.service
import pytest


@pytest.fixture(scope="session", autouse=True)
@pytest.mark.timeout(60)
def wait_for_iqfeed():
    while not pyiqfeed.service._is_iqfeed_running(os.environ["IQFEED_HOST"]):
        time.sleep(1)


def test_can_pull_data_from_specific_time_period():
    results = pkgutil.get_data("tests.data", "SPY_20190311_to_20190318.txt").decode("utf-8")

    hist_conn = iq.HistoryConn(name="pyiqfeed-Example-historical-bars")
    hist_listener = iq.VerboseIQFeedListener("History Bar Listener")
    hist_conn.add_listener(hist_listener)

    with iq.ConnConnector([hist_conn]) as connector:
        data = hist_conn.request_bars_in_period(
            ticker="SPY",
            interval_len=14400,
            interval_type="s",
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
            )
        )

        print(data)
        assert results == str(data)
