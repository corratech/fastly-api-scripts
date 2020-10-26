# fastly-api-scripts
primitive, simple and basic fastly scripts

# Prerequisite

- GNU/Linux environment
- Python3
- Python3 Virtualenv
- Python3 ast module
- Python3 json module
- Python3 requests module
- Python3 configparser module

# First Steps

Clone the repository to your local.

```
git clone https://github.com/corratech/fastly-api-scripts.git
```

Navigate to the newly clonned directory.

```
cd fastly-api-scripts
```

Copy the `config.ini.sample` and create a new file `config.ini`

```
cp -ar config.ini.sample config.ini
```

Update the values of `config.ini`. For ex:

- Replace the value for `token` in `config.ini` file with your `FASTLY API TOKEN`
- Replace the value for `service_id` in `config.ini` file with your `FASTLY SERVICE ID`

save `config.ini` once chnages are made.

Now, setup the python3 `VIRTUALENV` for `fastly-api-scripts`.

```
python3 -m venv .venv
```

This will created a new directoey named `.venv/` in the current directory. Now Activate the `VIRTUALENV`.

```
source .venv/bin/activate
```

Now you should be in the `(.venv)` prompt in your bash terminal.

Once the `VIRTUALENV` is created, Lets install the dependencies.

```
pip install -r requirements.txt
```

This would conclude the First Steps.


# Usage

This repo contains a few fastly python scipts. I will be describing the steps to invoke them from command line.

## Get The List of FASTLY VCL Versions

script filename : `get_versions_list.py`

### Invocation

```
./get_versions_list.py | jq '.[]'
```

this shoud print out the list of versions.

### To Find the active version use

```
./get_versions_list.py | jq '.[] | select(.active == true)'
```

### Only active version number?

```
./get_versions_list.py | jq '.[] | select(.active == true) | {number}'
```

## Get the List of ACL's Created

script filename : `get_list_of_acls.py`

### Invocation

Before we can invoke the command, we need to set an `ENVIRONMENT VARIABLE` named `CURRENT_VCL_VERSION` without it this command would fail.

The environment variable `CURRENT_VCL_VERSION` is used to store the current active VCL version number which we found with `get_versions_list.py`.

to set environment variable `CURRENT_VCL_VERSION` use: (for ex: `10` - chnage it with your actual version number)

```
export CURRENT_VCL_VERSION=10
```

### To Find all ACL's

```
./get_list_of_acls.py | jq '.[]'
```

Here you should see an ACL with name as `whitelist` which is created by default by Fastly.
You will be able to see a corresponding `id` for the ACL `whitelist`. Keep it handly, we may require it later.

## List all Entries in a Specific ACL

script file : `list_entries_of_specific_acl.py`

### Invocation

Before we can invoke the command, we need to set an `ENVIRONMENT VARIABLE` named `REQ_ACL_ID` without it this command would fail.

The environment variable `REQ_ACL_ID` is used to store the ACL ID of the specif ACL for which we nned to find all entries (IP Addresses).

We use the `id` which we found from using `get_list_of_acls` in the previous step.

to set environment variable `REQ_ACL_ID` use: (for ex: `xxxyyxxxyyy` - chnage it with your actual ACL ID for `whitelist` ACL or the one which you plan to use)

```
export REQ_ACL_ID='xxxxyyyyzzzzaaaabbbb'
```

### To List all Entries in the ACL

```
./list_entries_of_specific_acl.py | jq '.[]'
```

### To view only IP and Comments entries from ACL.

```
./list_entries_of_specific_acl.py | jq '.[] | {ip,comment}'
```


# Todo

- Add new entries to an existing ACL

# Credits

- [a.asokan](https://github.com/anishcorratech)