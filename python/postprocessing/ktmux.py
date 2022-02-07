import os
import sys
import optparse
import time

usage = 'python3 ktmux.py'
parser = optparse.OptionParser(usage)

parser.add_option('-n', '--new', dest='new', type=str, default = '', help='Please enter a tmux session name')
parser.add_option('-a', '--attach', dest = 'attach', default = False, action = 'store_true', help = 'Open an existing session')
parser.add_option('--McM', dest='forMcM', type=str, default = '', help='Please enter the last three number of McM request')
(opt, args) = parser.parse_args()

if opt.new != '' and opt.attach:
    raise RuntimeError("You cannot create a new tmux session and attach a new one at the same time! Please decide what you really want to do.")
elif opt.new == '' and not opt.attach:
    raise RuntimeError("This macro is not very useful if you do not want to neither create nor attach a tmux session...")

### if tmux session is for validating McM request, a new folder is created"
if opt.forMcM != '':
    dir_name = 'SMP-RunIISummer20UL16wmLHEGEN-00' + opt.forMcM
    os.makedirs(dir_name)
    os.system('cd ' + dir_name)

### get username and first letter of it from environment variables
username = str(os.environ.get('USER'))
inituser = str(os.environ.get('USER')[0])
keytab_path = '/afs/cern.ch/user/' + inituser + '/' + username + '/keytab'

### initialize kerberos
os.system('kinit -k -t ' + keytab_path + ' ' + username + '@CERN.CH')

### get a list of existing tmux sessions
lscommand = 'tmux ls'
outls = list(filter(lambda x : x != '\n', os.popen(lscommand).readlines()))

session_names = [s.split(":")[0] for s in outls]

### in case a new session is desiderd
if opt.new != "":
    newname = opt.new
    ### check if already exists a tmux session with the same desired one
    print('\n')
    while newname in session_names:
        newname = str(input('A session with the same name indicated by you already exists, please enter a new name (be creative!):\t'))

    ### once a (real) new name is obtained, going on with creating a new tmux session with permanent kerberos
    ktmux_command = 'k5reauth -f -i 3600 -p ' + username + ' -k ' + keytab_path + ' -- tmux new-session -s ' + newname
    os.system(ktmux_command)
### in case attaching an existing session is desidered
elif opt.attach:
    ### printing out existing sessions
    print("Existing tmux sessions:\t")
    for ts in session_names:
        print(ts+'\t')
    ### waiting for user to pick an existing session
    exname = ''
    print('\n')
    while exname == '' or exname not in session_names:
        exname = str(input('Which tmux session do you want to attach?\t'))

    att_command = 'tmux attach-session -t ' + exname
    print("Let's attach tmux session " + exname +"!")
    os.system(att_command)
