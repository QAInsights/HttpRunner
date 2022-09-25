# HttpRunner

## Installation

If below sh didn't work, follow the alternative steps.
```
bash -c "$(curl -ksSL https://httprunner.com/script/install.sh)"
```

### Alternative steps

```
wget https://github.com/httprunner/httprunner/releases/download/v4.2.0/hrp-v4.2.0-linux-amd64.tar.gz
```

```
tar -xf hrp-v4.2.0-linux-amd64.tar.gz
```

```
rm hrp-v4.2.0-linux-amd64.tar.gz
```

```
chmod +x hrp

sudo mv hrp /usr/bin
```

```
which hrp

hrp -v
```

## Scaffold a project

```
hrp startproject mytest
```

## Hello, Load Test!
```
hrp run example.yml 
```

```
hrp run example.yml --http-stat
```

```
hrp run example.yml --gen-html-report
```

> performance summary data is printed every 3 seconds
```
hrp boom example.yml --spawn-count 10 --spawn-rate 1
```
