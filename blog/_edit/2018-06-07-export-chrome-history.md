Grab `~/.config/google-chrome/History`, and `sqlite3 History`:

```sqlite
.headers on
.mode csv
.output history.csv
SELECT datetime(last_visit_time/1000000-11644473600,'unixepoch','localtime'), title, url FROM urls ORDER BY last_visit_time DESC;
```

To see if there are other columns, use `pragma table_info(urls);`
