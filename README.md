# Storm Status

Storm Status is a web app that shows current thunderstorm situation for a given city.
The app is powered by [burze.dzis.net] WSDL API.

## How to get up and running locally

#### Checkout the repository

```bash
$ git clone https://github.com/mockshox/storm_app.git
```

#### Configure application with config.json
Example configuration
```json
{
    "wsdl_file": "https://burze.dzis.net/soap.php?WSDL",
    "city": "Wrocław",
    "range_detect": 1
}
```

#### Setup burze.dzis.net API key
Once you obtain your API key from https://burze.dzis.net/?page=api_interfejs, make sure to expose it with the `STORM_INFO_API_KEY` environment variable
```bash
$ export STORM_INFO_API_KEY=your_api_key
```


##### Run the code in development mode
```bash
$ FLASK_ENV=development cd storm_app/app/ && flask run
```
