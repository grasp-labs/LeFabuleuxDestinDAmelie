"""
Python script example of using the Grasp Labs AS Stoa package.

The following example make use of what we call "rest" authentication, where
user credentials are used to authenticate the user.

Find more information here: https://pypi.org/project/ds-stoa/

Please update config.json with the correct values and run the script.

Example command: pipenv run python .\main.py --email <email> --password <password>
--config config.json
"""
import argparse
import json
import typing

import pandas as pd

from ds_stoa.manager import StoaClient


def fetch(email: str, password: str, config: typing.Dict) -> pd.DataFrame:
    """
    Function to fetch data from the API.
    @param email: User Email.
    @param password: User Password.
    @param config: Data requested object.
    @return: pd.DataFrame
    """
    stoa = StoaClient(
        authentication="rest",
        email=email,
        password=password,
        **config,
    )

    return stoa.fetch(format="dataframe")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch data from the API.")
    parser.add_argument("--email", type=str, help="Email", required=True)
    parser.add_argument(
        "--password", type=str, help="Password", required=True
    )
    parser.add_argument(
        "--config", type=str, help="Path to the config file", required=True
    )

    # Parse the arguments
    args = parser.parse_args()
    # Load the config file
    with open(args.config, "r") as f:
        config = json.load(f)

    data = fetch(args.email, args.password, config)
    print(data.head())
    print(type(data))
    data.to_csv("data.csv", index=False)