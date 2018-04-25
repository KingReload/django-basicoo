# BasicOO Project


You can use this project to start of with an object oriented environment.
This project is pure for helping myself and others get to know OOP within the Django Framework.
This project might not be entirely done yet, but it's a start.

This project uses `Django 1.11.5`.
The current project could still use an upgrade to `Django 2.x`, but at the moment I'm not interested in upgrading the project.


## Installation


1. Install `python 3.x`.
2. Make sure you have `virtualenv` and `psql / postgresql` installed.
3. Clone the project to a folder.
4. Make sure you run the commands from the `django-basicoo` folder.
5. Run the commands in the following order:
    - `virtualenv -p python3 .env`
    - `source .env/bin/activate`
    - `make install`
    - `make frontend`
    - `./manage.py collectstatic`
    - `createdb -h localhost -O postgres basicoo` however you can change your database name from `basicoo` to your own, but you'll need to read the `Note` below.
    - `./manage.py migrate`
    - `make exampledata`

Note: that if you want to use your own database name, you'll have to overwrite every `basicoo` within this project.

Note2: if you want to set up a gmail server go to the `settings` folder and then click on the `.env` file, there you can set your gmail account and password. Make sure you hash your password with utf-8 and then base64.

Make exampledata will give you a standard login:
- Admin
- ipasswordi


## Postgres


I stumbled against some issues with Postgres, so I will be posting answers to this as well.

If you have the error similar to:
> SQLSTATE[08006] [7] FATAL: password authentication failed for user "postgres" FATAL: password authentication failed for user "postgres"

- Then you will need to follow these steps:
    - `psql -h localhost <database>` where "database" is the name of your database.
    - `cd /etc/postgresql/<version>/main/` where "version" is your postgres version, I use postgres `9.5`.
    - `sudo nano pg_hba.conf`
    - After this you will need to put 3 things on `trust` from 2 of the `localhost` and 1 `host`.

        ```
        # Database administrative login by Unix domain socket
        local   all             postgres                                trust

        # TYPE  DATABASE        USER            ADDRESS                 METHOD

        # "local" is for Unix domain socket connections only
        local   all             all                                     trust

        # IPv4 local connections:
        host    all             all             127.0.0.1/32            trust
        ```

    - `sudo service postgres restart`
    - After this you can type `psql -h localhost <database>` to see if you can connect to the database.


## Windows


If you use windows I highly recommend you to install either "bash for windows" or dual boot Linux on your system.

How to install [Bash for Windows](https://www.windowscentral.com/how-install-bash-shell-command-line-windows-10)?

If the `bash.exe` doesn't work for you just install doing the following command:
- `lxrun /install`
