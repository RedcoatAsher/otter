import sys, os, json
from workflow import Workflow, ICON_SETTINGS, web

def main(wf):
    settings = wf.datafile('servers.json')
    # os.remove(settings)
    if not os.path.isfile(settings):
        log.debug("file doesn't exist")
        data = [{
                    "group-name": "group-name",
                    "server-label": "label",
                    "host": "domain.com",
                    "username": "user.name",
                    "port": "22",
                    "key-path": "",
                    "more-options": ""
                }]
        with open(settings, 'w') as outfile:
          json.dump(data, outfile, indent=2, separators=(',', ': '))

    wf.add_item(
            title = "setup server(s)",
            subtitle = "",
            arg = wf.datafile('servers.json'),
            valid = True,
            type = 'file',
            icon = wf.workflowdir + '/' + 'editServers.png'
            )
    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
