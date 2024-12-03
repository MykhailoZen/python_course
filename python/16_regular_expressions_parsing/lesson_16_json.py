# JSON & YAML: given two files, devices.yaml & lab_envs.json, parse and combine them into one YAML file, which has "lab_env" attribute filled for each device. If there is no such env in the lab_envs.json, set it for the corresponding device to None.
import json
import yaml

def new_device_func(lab_envs, devices):
    for device_name in devices:
        device = devices[device_name]
        env = device['lab_env']
        device['lab_env'] = None

        for envs in lab_envs:
            if env in envs:
                device['lab_env'] = lab_envs[env]
                break

        devices[device_name] = device

    return devices


if __name__ == "__main__":
    with open("lab_envs.json", mode="r", encoding="utf-8") as f:
        lab_envs = json.load(f)

    with open("devices.yaml", mode="r", encoding="utf-8") as f:
        devices = yaml.safe_load(f)

    new_dev_config = new_device_func(lab_envs, devices)

    with open("new_devices.yaml", mode="w", encoding="utf-8") as f:
        yaml.dump(new_dev_config, f)
