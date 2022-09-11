# Zeddo

>News CLI for lazy people

Zeddo aggregates news from many different sources so you can stay up date
without leaving your terminal.

## Installation

```
pip install zeddo
```

## Set up

Create a [News API account](https://newsapi.org/register) and save the API key.
(You can choose the free plan.)

Then run `zeddo` and enter the API key when prompted.

## Usage

```
$ zeddo
[1] Public Protector finds procurement of 'scooter ambulances' was improper (News24)
[2] Businessinsider.co.za | Salaries for Ramaphosa, ministers set to remain unchanged – for the second year in a row (News24)
[3] JUST IN | SCA rules 2018 ANC Free State election 'unlawful and unconstitutional' (News24)
[4] Specialized's Turbo Como SL Is a Comfy, Lightweight Cruiser (Wired)
[5] 24 Times Teen Dramas Tried To Go Outside Their Genre And It Was Just So Weird (Buzzfeed)
Please enter an article number to open:
```

## Configuration

*Advanced usage:*

```
$ zeddo -h
Usage: zeddo [OPTIONS]

Options:
  -k, --api-key TEXT       API key for News API
  -l, --language TEXT      Filter articles by language
  -t, --category TEXT      Filter by category
  -s, --search TEXT        Search by key phrase
  -n, --max-count INTEGER  Limit number of articles
  -v, --version            Show the version and exit.
  -h, --help               Show this message and exit.
  -c, --config FILE        Read configuration from FILE.
```

*Example config file:*

```toml
api_key = "<News API key>"
language = "en"
```

The location of the config file depends on the operating system:
- Mac OS X (not POSIX): `~/Library/Application Support/zeddo/config`
- Unix (not POSIX): `~/.config/zeddo/config`
- Mac OS X and Unix (POSIX): `~/.zeddo/config`
- Windows
  - Roaming: `C:\Users\<user>\AppData\Roaming\Foo Bar\config`
  - Not roaming: `C:\Users\<user>\AppData\Local\Foo Bar\config`

## License

Licensed under the GNU Public License v3.0
