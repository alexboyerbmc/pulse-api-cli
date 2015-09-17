## Metrics
Commands to administer metric definitions in a TrueSight Pulse account.


### metric-create

**API Documentation**

[http://premium-documentation.boundary.com/v1/post/metrics](http://premium-documentation.boundary.com/v1/post/metrics)

**Usage**

```bash
                     [-a api_host] [-e e_mail] [-t api_token] -n metric_name
                     -d display_name -s display_short_name [-i description] -g
                     {AVG,MAX,MIN,SUM} -u {percent,number,bytecount,duration}
                     [-r resolution] [-x {yes,no}]

Creates a new metric definition in an TrueSight Pulse account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical.Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        TrueSight Pulse API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the TrueSight Pulse account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access to the
                        TrueSight Pulse account
  -n metric_name, --metric-name metric_name
                        Metric identifier
  -d display_name, --display-name display_name
                        Metric display name
  -s display_short_name, --display-name-short display_short_name
                        Metric short display name
  -i description, --description description
                        Metric description
  -g {AVG,MAX,MIN,SUM}, --aggregate {AVG,MAX,MIN,SUM}
                        Metric default aggregate
  -u {percent,number,bytecount,duration}, --unit {percent,number,bytecount,duration}
                        Metric unit
  -r resolution, --resolution resolution
                        Metric default resolution
  -x {yes,no}, --is-disabled {yes,no}
                        Enable or disable the metric definition
```

**Examples**

Create a new metric, `TRUESIGHT_PULSE_CLI_METRIC` with a display name of _TrueSight Pulse CLI Metric_, a short display of _CLI Metric_,
default aggregate of _AVG_, and unit of _number_.

```bash
$ metric-create -n TRUESIGHT_PULSE_CLI_METRIC -d "TrueSight Pulse CLI Metric" -s "CLI Metric" -g AVG -u number
{
  "result": {
    "name": "TRUESIGHT_PULSE_CLI_METRIC",
    "displayName": "TrueSight Pulse CLI Metric",
    "displayNameShort": "CLI Metric",
    "unit": "number",
    "defaultAggregate": "AVG",
    "id": 151327
  }
}

```


### metric-delete

**API Documentation**

[http://premium-documentation.boundary.com/v1/delete/metrics/:metric](http://premium-documentation.boundary.com/v1/delete/metrics/:metric)

**Usage**

```bash
usage: metric-delete [-h] [-l {debug,info,warning,error,critical}]
                     [-a api_host] [-e e_mail] [-t api_token] -n metric_name

Deletes a metric definition from a TrueSight Pulse account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical.Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        TrueSight Pulse API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the TrueSight Pulse account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access to the
                        TrueSight Pulse account
  -n metric_name, --metric-name metric_name
                        Metric identifier
```

**Examples**

Delete a metric definition identified by a metric identifier of `TRUESIGHT_PULSE_DELETE_METRIC`

```bash
$ metric-delete -n TRUESIGHT_PULSE_DELETE_METRIC 
{
  "result": {
    "success": true
  }
}
```

### metric-export

**API Documentation**

[http://premium-documentation.boundary.com/v1/get/metrics](http://premium-documentation.boundary.com/v1/get/metrics)

**Usage**

```bash
usage: metric-export [-h] [-l {debug,info,warning,error,critical}]
                     [-a api_host] [-e e_mail] [-t api_token] [-p pattern]

Export the metric definitions from a TrueSight Pulse account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical.Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        TrueSight Pulse API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the TrueSight Pulse account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access to the
                        TrueSight Pulse account
  -p pattern, --pattern pattern
                        regular expression pattern to use search the name of
                        the metric
```

**Examples**

Export metric where the metric identifier begins with `TRUESIGHT_PULSE`

```bash
$ metric-export -p ^TRUESIGHT_PULSE
{
    "TRUESIGHT_PULSE_CPU_LOAD_15_MINUTE": {
        "defaultAggregate": "AVG",
        "defaultResolutionMS": null,
        "description": "CPU load in the last 15 minutes.",
        "displayName": "CPU Load 15 Minute",
        "displayNameShort": "Load 15 Minute",
        "isDisabled": false,
        "unit": "number"
    },
    "TRUESIGHT_PULSE_CPU_LOAD_1_MINUTE": {
        "defaultAggregate": "AVG",
        "defaultResolutionMS": null,
        "description": "Load on the CPU in the last minute.",
        "displayName": "CPU Load 1 Minute",
        "displayNameShort": "Load 1 Minute",
        "isDisabled": false,
        "unit": "number"
    },
    "TRUESIGHT_PULSE_CPU_LOAD_5_MINUTE": {
        "defaultAggregate": "AVG",
        "defaultResolutionMS": null,
        "description": "CPU load in the last 5 minutes.",
        "displayName": "CPU Load 5 Minute",
        "displayNameShort": "Load 5 Minute",
        "isDisabled": false,
        "unit": "number"
    },
    "TRUESIGHT_PULSE_FILE_SPACE_CAPACITY": {
        "defaultAggregate": "AVG",
        "defaultResolutionMS": null,
        "description": "Percentage used of a file system.",
        "displayName": "File Space Capacity",
        "displayNameShort": "File Space Capacity",
        "isDisabled": false,
        "unit": "percent"
    },
    "TRUESIGHT_PULSE_PORT_AVAILABILITY": {
        "defaultAggregate": "AVG",
        "defaultResolutionMS": null,
        "description": "Reports on the availability of TCP/IP port.",
        "displayName": "Port Availability",
        "displayNameShort": "Port Availability",
        "isDisabled": false,
        "unit": "number"
    },
    "TRUESIGHT_PULSE_PORT_RESPONSE": {
        "defaultAggregate": "AVG",
        "defaultResolutionMS": null,
        "description": "Port Response",
        "displayName": "Port Response",
        "displayNameShort": "Port Response",
        "isDisabled": false,
        "unit": "number"
    },
    "TRUESIGHT_PULSE_PROCESS_COUNT": {
        "defaultAggregate": "AVG",
        "defaultResolutionMS": null,
        "description": "Number of processes running on a host.",
        "displayName": "Process Count",
        "displayNameShort": "Process Count",
        "isDisabled": false,
        "unit": "number"
    },
    "TRUESIGHT_PULSE_RANDOM_NUMBER": {
        "defaultAggregate": "SUM",
        "defaultResolutionMS": null,
        "description": "An example metric definition for using the boundary plugin shell",
        "displayName": "Random Number",
        "displayNameShort": "Random Number",
        "isDisabled": false,
        "unit": "number"
    }
}
```

### metric-get

**API Documentation**

[http://premium-documentation.boundary.com/v1/get/metrics](http://premium-documentation.boundary.com/v1/get/metrics)

**Usage**

```bash
usage: metric-get [-h] [-l {debug,info,warning,error,critical}] [-a api_host]
                  [-e e_mail] [-t api_token] -n metric_name

Lists the defined metrics in a TrueSight Pulse account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical.Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        TrueSight Pulse API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the TrueSight Pulse account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access to the
                        TrueSight Pulse account
  -n metric_name, --metric-name metric_name
                        Metric identifier
```

**Examples**

Display the metric definition identified by the metric identifier `TRUESIGHT_PULSE_CLI_METRIC`

```bash
$ metric-get -n TRUESIGHT_PULSE_CLI_METRIC 
{
    "defaultAggregate": "AVG",
    "defaultResolutionMS": null,
    "description": null,
    "displayName": "TrueSight Pulse CLI Metric",
    "displayNameShort": "CLI Metric",
    "isDisabled": false,
    "name": "TRUESIGHT_PULSE_CLI_METRIC",
    "unit": "number"
}
```

### metric-import

**API Documentation**

[http://premium-documentation.boundary.com/v1/post/metrics](http://premium-documentation.boundary.com/v1/post/metrics)

**Usage**

```bash
usage: metric-import [-h] [-l {debug,info,warning,error,critical}]
                     [-a api_host] [-e e_mail] [-t api_token] -f path

Imports metric definitions from a file into a TrueSight Pulse account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical.Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        TrueSight Pulse API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the TrueSight Pulse account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access to the
                        TrueSight Pulse account
  -f path, --file path  Path to JSON file
```

**Examples**

Given the following JSON document of metric definitions in a file `metrics.json`:

```json
{
  "TRUESIGHT_PULSE_METRIC_CLI_ONE": {
    "defaultAggregate": "AVG",
    "defaultResolutionMS": 5000,
    "description": "Example metric TRUESIGHT_PULSE_METRIC_CLI_ONE",
    "displayName": "TrueSight Pulse CLI Metric One",
    "displayNameShort": "CLI Metric One",
    "isDisabled": false,
    "unit": "percent"
  },
  "TRUESIGHT_PULSE_METRIC_CLI_TWO": {
    "defaultAggregate": "SUM",
    "defaultResolutionMS": 5000,
    "description": "Example metric TRUESIGHT_PULSE_METRIC_CLI_TWO",
    "displayName": "TrueSight Pulse CLI Metric Two",
    "displayNameShort": "CLI Metric Two",
    "isDisabled": false,
    "unit": "number"
  },
  "TRUESIGHT_PULSE_METRIC_CLI_THREE": {
    "defaultAggregate": "MAX",
    "defaultResolutionMS": 5000,
    "description": "Example metric TRUESIGHT_PULSE_METRIC_CLI_THREE",
    "displayName": "TrueSight Pulse CLI Metric Three",
    "displayNameShort": "CLI Metric Three",
    "isDisabled": false,
    "unit": "number"
  }
}
```

Run the following command to import the metric definitions:

```bash
$ metric-import -f metrics.json
```

### metric-update

**API Documentation**

[http://premium-documentation.boundary.com/v1/put/metrics/:metricName](http://premium-documentation.boundary.com/v1/put/metrics/:metricName)

**Usage**

```bash
metric-update [-h] [-l {debug,info,warning,error,critical}]
                     [-a api_host] [-e e_mail] [-t api_token] -n metric_name
                     -d display_name -s display_short_name [-i description] -g
                     {AVG,MAX,MIN,SUM} -u {percent,number,bytecount,duration}
                     [-r resolution] [-x {yes,no}]

Updates a metric definition in an TrueSight Pulse account

optional arguments:
  -h, --help            show this help message and exit
  -l {debug,info,warning,error,critical}, --log-level {debug,info,warning,error,critical}
                        Sets logging level to one of
                        debug,info,warning,error,critical.Default is logging
                        is disabled
  -a api_host, --api-host api_host
                        TrueSight Pulse API host endpoint
  -e e_mail, --email e_mail
                        e-mail that has access to the TrueSight Pulse account
  -t api_token, --api-token api_token
                        API token for given e-mail that has access to the
                        TrueSight Pulse account
  -n metric_name, --metric-name metric_name
                        Metric identifier
  -d display_name, --display-name display_name
                        Metric display name
  -s display_short_name, --display-name-short display_short_name
                        Metric short display name
  -i description, --description description
                        Metric description
  -g {AVG,MAX,MIN,SUM}, --aggregate {AVG,MAX,MIN,SUM}
                        Metric default aggregate
  -u {percent,number,bytecount,duration}, --unit {percent,number,bytecount,duration}
                        Metric unit
  -r resolution, --resolution resolution
                        Metric default resolution
  -x {yes,no}, --is-disabled {yes,no}
                        Enable or disable the metric definition
```

**Examples**

Update a metric definition

```bash
$ metric-update -n TRUESIGHT_PULSE_TEST_METRIC -d "TrueSight Pulse Test Metric" -s "CLI Metric" -g AVG -u number -i 'New metric to update'
{
  "result": {
    "name": "TRUESIGHT_PULSE_TEST_METRIC",
    "description": "New metric to update",
    "displayName": "TrueSight Pulse Test Metric",
    "displayNameShort": "CLI Metric",
    "unit": "number",
    "defaultAggregate": "AVG",
    "id": 151332
  }
}
```