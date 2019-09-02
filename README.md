# Navigator

The Robot navigates through the city which is described in [city.txt](/data/city.txt) along the routes described in [routes.txt](/data/routes.txt)
To add an ability starting the robot on different machines I used docker.

*Note*: Requires python >= 3.7

## Commands

### Using Docker:
    $ make build - build the docker image
    $ make run - start the robot and navigate through all available routes
    $ make test - run project tests

### Using local env:
	$ python3 -m venv .env
	$ source .env/bin/activate
	$ python3 setup.py install
	$ DATA_PATH=data navigate

## Output
For the defined city and routes the output is:

    make run

    INFO : Running process...
    INFO : Investigating London city...

    NEW ROUTE

    INFO : Navigating 'To work' from the Position(130, 100)...
    INFO : > Go North 5 blocks
    INFO : Going 5 block(s) forward...
    INFO : > Turn right
    INFO : Changing direction to East
    INFO : > Go to landmark "Madame Tussauds Wax Museum"
    INFO : Heading for Position(200, 200)...
    INFO : Going 70 block(s) forward...
    INFO : Changing direction to North
    INFO : Going 95 block(s) forward...
    INFO : We're in place!
    INFO : > Go West 25 blocks
    INFO : Changing direction to West
    INFO : Going 25 block(s) forward...
    INFO : > Turn left
    INFO : Changing direction to South
    INFO : > Go 3 blocks
    INFO : Going 3 block(s) forward...
    INFO : Navigation 'To work' finished!

    NEW ROUTE

    INFO : Changing direction to North
    INFO : Navigating 'To home' from the Position(10, 10)...
    INFO : > Go North 25 blocks
    INFO : Going 25 block(s) forward...
    INFO : > Go East 15 blocks
    INFO : Changing direction to East
    INFO : Going 15 block(s) forward...
    INFO : > Turn right
    INFO : Changing direction to South
    INFO : > Go 5 blocks
    INFO : Going 5 block(s) forward...
    INFO : > Turn left
    INFO : Changing direction to East
    INFO : > Go to landmark "Hyde Park"
    INFO : Heading for Position(5, 25)...
    INFO : Changing direction to West
    INFO : Going 20 block(s) forward...
    INFO : Changing direction to South
    INFO : Going 5 block(s) forward...
    INFO : We're in place!
    INFO : > Turn right
    INFO : Changing direction to West
    INFO : > Go 3 blocks
    INFO : Going 3 block(s) forward...
    INFO : Navigation 'To home' finished!
    INFO : All routes are finished!
    INFO : Process finished!
