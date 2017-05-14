# Otter
A simple, customized, easy to use `ssh` connection tool for Alfred 3.

Can be used with any of ther following server connection configs...
>  username | password 
>  username | private keyd


### Requirements
> Up-to-date **[PowerPack](https://www.alfredapp.com/powerpack/)** subscription


### Download

See the **[release list](https://github.com/AsherPeruscini/otter/releases)** for the lastest version, and all previous versions.


### Usage

+  [Download](https://github.com/AsherPeruscini/otter/releases) & Open
+  Setup your server(s) in the `servers.json` list... [check out the how-to](#)
+  "Call" Alfred and type `ssh`, then...
> select from the server names that appear
-or-
> continue typing the name of the server to filter the list


(###how-to)

###### `servers.json` examples
```json
{
    "group-name": "PROD",
    "server-label": "web01",
    "host": "domain.com",
    "username": "user.name",
    "password": "password",
    "key-path": "/Users/Otter/id_rsa",
    "port": "22",
    "more-options": ""
}
```
