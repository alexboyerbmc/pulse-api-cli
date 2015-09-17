## Measurements

Commands to insert and extract measurements from a TrueSight Pulse account.


### measurement-create

**API Documentation**

[http://premium-documentation.boundary.com/v1/post/measurements](http://premium-documentation.boundary.com/v1/post/measurements)

**Usage**


```
usage: measurement-create [-h] [-l {debug,info,warning,error,critical}]
                          [-a api_host] [-e e_mail] [-t api_token] -n
                          metric_name -m measurement [-s source]
                          [-d timestamp]

Adds a measurement value to a TrueSight Pulse account

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
  -m measurement, --measurement measurement
                        Measurement value
  -s source, --source source
                        Source of measurement. Defaults to the host where the
                        command is run
  -d timestamp, --timestamp timestamp
                        Time of occurrence of the measurement in either epoch
                        seconds or epoch milliseconds. Defaults to the receipt
                        time at TrueSight Pulse

```

**Examples**

Send a measurement value of 100 for the metric `TRUESIGHT_PULSE_HELLO_WORLD`

```bash
$ measurement-create -n TRUESIGHT_PULSE_HELLO_WORLD -m 100
{
    "result": {
        "success": true
    }
}

```

### measurement-get

** API Documentation **

[http://premium-documentation.boundary.com/v1/get/measurements/:metric](http://premium-documentation.boundary.com/v1/get/measurements/:metric)

** Usage **

```bash
usage: measurement-get [-h] [-l {debug,info,warning,error,critical}]
                       [-a api_host] [-e e_mail] [-t api_token] -n metric_name
                       [-g aggregate] [-s source] -b start [-d end]

Retrieves measurement values from a metric in a TrueSight Pulse account

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
  -n metric_name, --name metric_name
                        Metric identifier
  -g aggregate, --aggregate aggregate
                        Metric default aggregate
  -s source, --source source
                        Source of measurement
  -b start, --start start
                        Start of time range as ISO 8601 string or epoch
                        seconds
  -d end, --end end     End of time range as ISO 8601 string or epoch seconds
```

**Examples**



```bash
measurement-get -n TRUESIGHT_PULSE_HELLO_WORLD -b 2015-06-10
{
    "result": {
        "aggregates": [
            [
                [
                    1433973154000,
                    null
                ],
                [
                    [
                        "lerma",
                        100
                    ]
                ]
            ]
        ],
        "timestamp": 1433973185845
    }
}
```


