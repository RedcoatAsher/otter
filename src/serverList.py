import sys, os, json
from workflow import Workflow, ICON_WEB, web
from operator import itemgetter
log = None

def keyForServer(server):
    log.debug(server)
    return '{} {}'.format(server['server-label'], server['group-name'])

def main(wf):

    if len(wf.args):
        query = wf.args[0]
    else:
        query = None

    settings = wf.datafile('servers.json')
    if os.path.isfile(settings):
        jsonData = open(settings).read()
        servers = json.loads(jsonData)
        servers = sorted(servers, key = itemgetter('server-label'))

        if query:
            filtered = wf.filter(query, servers, keyForServer)
            log.debug(filtered)
        else:
            filtered = servers

        for s in filtered:
            keyPath = "" if ("key-path" not in s or s['key-path'] == "") else " -i %s" % s['key-path']
            port = "" if ("port" not in s or s['port'] == "") else " -p %s" % s['port']
            wf.add_item(
                title = "%s" % (s['server-label']),
                subtitle = "%s | %s@%s" % (s['group-name'], s['username'], s['host']),
                arg = "%s@%s %s %s" % (s['username'], s['host'], port, keyPath),
                valid = True,
                icon = wf.workflowdir + '/' + 'callServer.png'
            )

        # Send the results to Alfred as XML
        wf.send_feedback()
if __name__ == u"__main__":
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
