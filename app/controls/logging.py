import os, time

if not os.path.exists('storage'): os.mkdir('storage')

def write(msg, level = 'INFO'):
    with open(os.path.join('storage', 'run.log'), 'w+') as f:
        f.write('[%s-%s]%s'%(int(time.time()), (level + '    ')[:4], msg))
