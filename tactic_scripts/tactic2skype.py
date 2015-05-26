import datetime
from dateutil import parser
import time

start_time = time.time()
import sys
sys.path.append("//Art-1405260002/d/assets/client")

from tactic_client_lib import TacticServerStub
server = TacticServerStub()

server.set_server("192.168.201.10")
server.set_project("simpleslot")
ticket = server.get_ticket("julio", "1234")
server.set_ticket(ticket)

import Skype4Py

skype = Skype4Py.Skype()
client = skype.Client
if not client.IsRunning:
    client.Start()
skype = Skype4Py.Skype()
skype.Attach()

all_messages = []
departments = ['2d', '3d', 'technical_artist', 'sound']
dept_string = ""
for dept in departments:
    dept_string = dept_string + "['department','" + dept + "']"

expr = "@SOBJECT(sthpw/login['begin']" + dept_string + "['or'])"
logins = server.eval(expr)

for login in logins:
    
    name = login.get('login')
    skypeName = login.get('skype')

    expr = "@SOBJECT(sthpw/task['begin']['status','.In Progress']['status','.Ready']['or']['assigned','" + name + "'])"
    all_tasks = server.eval(expr)
    count = 0
    temp = []
    game_name = task_name = final = ""
    notification = '這是TACTIC系統工作自動提示\n完成的工作請把狀況設成 Review\n請登入TACTIC > 個人工作管理\n這是系統自動訊息, 請勿回復\n'
    #notification = '2015/4/9 系統測試\n'
    print skypeName
    for task in all_tasks:
        length = len(all_tasks)
        count = count + 1
        task_id = str(task.get('id'))
        st = task.get('search_type')
        bed = task.get('bid_end_date')
        bed = parser.parse(bed)
        bsd = task.get('bid_start_date')
        bsd = parser.parse(bsd)
        now = datetime.datetime.now()
        sound = []
        task_name = ""
        delta = bed - bsd
        duration = (delta.days + 1)
        duration = str(duration)
        delta = bed - now
        days_remaining = (delta.days + 1)
        process = task.get('process')
        if st == "simpleslot/technical_artist?project=simpleslot":
            expr = "@SOBJECT(sthpw/task['id'," + task_id + "].parent)"
            ta = server.eval(expr)

            if ta[0] is None:
                pass
            elif ta:
                task_name = ta[0].get('description')
                game_code = ta[0].get('game_code ')
                ta_proj_code = ta[0].get('ta_projects_code')

                if(game_code):
                    expr = "@SOBJECT(simpleslot/game['code','" + game_code + "'])"
                    parent = server.eval(expr)
                    game_name = parent[0].get('name')
                    game_name_chn = parent[0].get('name_chn')
                    game_name_chn = str(game_name_chn.encode('utf-8'))

                if(ta_proj_code):
                    expr = "@SOBJECT(simpleslot/ta_projects['code','" + ta_proj_code + "'])"
                    parent = server.eval(expr)
                    game_name = parent[0].get('name')
                    game_name_chn = parent[0].get('description')
                    game_name_chn = str(game_name_chn.encode('utf-8'))

                if not ta_proj_code and not game_code:
                    game_name = "Not Entered"
                    game_name_chn = "沒填"

        elif st == "simpleslot/package?project=simpleslot":

            expr = "@SOBJECT(sthpw/task['id'," + task_id + "].parent.parent)"
            twod = server.eval(expr)
            task_name = twod[0].get('description')

            if twod[0] is None:
                pass
            elif twod:
                game_name = twod[0].get('name')
                game_name_chn = twod[0].get('name_chn')
                game_name_chn = str(game_name_chn.encode('utf-8'))

        elif st == "simpleslot/sound?project=simpleslot":
            expr = "@SOBJECT(sthpw/task['id'," + task_id + "].parent.parent)"
            sound = server.eval(expr)

            if sound[0] is None:
                pass
            elif sound:
                game_name = sound[0].get('name')
                game_name_chn = sound[0].get('name_chn')
                game_name_chn = str(game_name_chn.encode('utf-8'))

        elif st == "simpleslot/game?project=simpleslot":
            expr = "@SOBJECT(sthpw/task['id'," + task_id + "].parent)"
            sound_game = server.eval(expr)

            if sound_game[0] is None:
                pass
            elif sound_game:
                game_name = sound_game[0].get('name')
                game_name_chn = sound_game[0].get('name_chn')
                game_name_chn = str(game_name_chn.encode('utf-8'))

        elif st == "simpleslot/3d?project=simpleslot" or st == "simpleslot/assets?project=simpleslot" or st == "simpleslot/shot?project=simpleslot":
            expr = "@SOBJECT(sthpw/task['id'," + task_id + "].parent)"
            threed = server.eval(expr)
            if threed[0] is None:
                pass
            elif threed:
                task_name = threed[0].get('name')
                task_name_chn = threed[0].get('description')
                task_name_chn = str(task_name_chn.encode('utf-8'))

                expr = "@SOBJECT(sthpw/task['id'," + task_id + "].parent.parent)"
                parent = server.eval(expr)
                if(parent):
                    game_name = parent[0].get('name')
                    game_name_chn = parent[0].get('name_chn')
                    game_name_chn = str(game_name_chn.encode('utf-8'))

                    game_code = parent[0].get('code')
                elif(not parent):
                    fullpath = "/assets/scripts/font-awesome-4.1.0/png/exclamation-triangle_ffd600_128.png"
                    game_name = "none"
                    game_name_chn = "none"

        if(game_name):
            title = '專案: '
            message = "(" + str(count) + "/" + str(length) + ") " + title.decode('utf-8') + game_name + " (" + game_name_chn.decode('utf-8') + ")\n"
            title = '工作: '
            message = message + " " + title.decode('utf-8') + process + " " + task_name + "\n"
            title = '開始:'
            message = message + title.decode('utf-8') + str(bsd.strftime('%m-%d')) + " "
            title = '結束:'
            message = message + title.decode('utf-8') + str(bed.strftime('%m-%d')) + " "
            title = '工期: '
            message = message + title.decode('utf-8') + duration + '天'.decode('utf-8') + "\n"
            if days_remaining > 0:
                title = '還剩: '
                message = message + title.decode('utf-8') + str(days_remaining) + '天'.decode('utf-8') + "\n\n"
            elif days_remaining < 0:
                title = '過期: '
                message = message + title.decode('utf-8') + str(days_remaining * (-1)) + '天'.decode('utf-8') + "(devil)\n\n"

            final = final + message

    if final != "":
        final = final + notification.decode('utf-8')
        
        print final
        #if skypeName == "m.3d.julio0303":
        #    pass
        #else:
        skype.SendMessage(skypeName, final)
        toinin = name + "\n" + "-----------------------------------\n" + final + "\n"
        skype.SendMessage("m.inin1001", toinin)
        #print toinin

skype.SendMessage("m.3d.julio0303", "script ok")

end_time = time.time()
diff = start_time - end_time
print("--- %s seconds ---" % diff)
