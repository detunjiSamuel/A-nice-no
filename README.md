# Nice No

A simple script to automatically kick off anyone using a Covenant University student internet credential from the campus network.

## Why
Every student is given internet credentials that are attached to their matriculation numbers and this can only be used on one device at a time. Recently, students have complained about not being able to access the internet because someone gained access to these details illegitimately.

## How it works
The script obtains the MAC address of the intruder and the masks as the system to disconnect the individual from the internet. 
The school's networking team will pick multiple systems with the same MAC address as an anomaly.


## Usage

### Install All Dependencies

```bash
pip3 install -r requirements.txt 
```


### Run
```bash
python3 kick_user.py 
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)