import json
import os
import subprocess
from pathlib import Path
import qcodes as qc


def get_data_path():
    path = Path('~/.leklab/leklab.json')
    with open(path.expanduser()) as f:
        leklabsetup = json.load(f)
    return Path(leklabsetup['data_path']).expanduser()


def connect_to_database(*, db_name, sample_name, experiment_name=None,\
                        station_file=None):
    db_folder_path = get_data_path() / db_name
    Path(db_folder_path).mkdir(parents=True, exist_ok=True)
    db_path = db_folder_path / (db_folder_path.stem + '.db')
    qc.initialise_or_create_database_at(db_path)
    print(f'Connected to {db_path}')
    experiment_name = experiment_name if experiment_name is not None else db_name
    exp = qc.load_or_create_experiment(experiment_name=experiment_name,
                                       sample_name=sample_name)
    if station_file is None:
        return None
    return exp, qc.Station(config_file=station_file)


def live_plot():
    db_path = qc.dataset.sqlite.database.get_DB_location()
    with open(os.devnull, 'w') as out:
        subprocess.Popen(['plottr-inspectr', '--dbpath', db_path],\
                         stdout=out, stderr=out)