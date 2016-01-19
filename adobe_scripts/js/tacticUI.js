    function mainWindow(){
        filter = 'inprogress';

        var self = this;
        self.asset_item_details = '';
        self.shot_item_details = '';
        self.server = '';
        self.item_tasks = '';

        self.game;
        self.projects_data = [];
        self.project_info = [];

        self.item_details = "";

        self.item_task_details = "";
    /*    self.item_process = '';
        self.item_code = '';
        self.assigned = '';
        self.bsd = '';
        self.bed = '';
        self.sk = '';
        self.processes = '';
    */
        self.asset_process_list = [];
        self.shot_process_list = [];

        self.cftype = ['sports', 'cf', 'video_conf', 'database'];

        self.getProjects = function(){
            $j('#projects').empty();

            if(filter == 'inprogress'){
                filter_id = "['id','8']";
            }
            else if(filter == 'standby'){
                filter_id = "['id','10']";
            }
            else if(filter == 'complete'){
                filter_id = "['id','11']";
            }
            else {
                filter_id = "";
            }

            expr = "@SOBJECT(simpleslot/plan['begin']" + filter_id + "['or'])"
            temp = server.eval(expr)[0];
            names = bsd = bed = names_chn = game_type = assigned = "";

            names = temp['name'].split('__');
            names.shift();
            bsd = temp['login'].split('__');
            bsd.shift();
            bed = temp['keywords'].split('__');
            bed.shift();
            names_chn = temp['game_name_chn'].split('__');
            names_chn.shift();
            game_type = temp['description'].split('__');
            game_type.shift();
            assigned = temp['process'].split('__');
            assigned.shift();


            for(x=0;x<names.length;x++){
                data = {'name': names[x], 'bsd': bsd[x], 'bed': bed[x], 'game_name_chn': names_chn[x], 'game_type': game_type[x], 'assgined': assigned[x]};
                self.projects_data.push(data);
            }

            names = names.sort();

            project_list = "";
            for(i=0;i<names.length;i++){
                project_list = project_list + "<li>" + names[i] + "</li>";
            }
            $j('ul.selectable#projects').append(project_list);

            /* bind behavior */
            $j('.selectable#projects li').on('click', function( event, ui ) {
                $j('.selectable li').removeClass("ui-selected");
                $j(this).addClass("ui-selected");
                self.game = $j(this).text();
                self.getItems();
            });

            /* select default */
            selected = $j('ul.selectable#projects li.ui-selected');
            if(selected.length == 0) {
                temp = $j("ul.selectable#projects li:contains('fishing_joy_cf')");
                $j(temp).addClass('ui-selected');
                self.game = $j(temp).text();
                self.getItems();
            }
        }

        self.getItems = function(){
            for(x=0;x<self.projects_data.length;x++){
                if(self.game == self.projects_data[x]['name']){
                    if(self.projects_data[x]['game_type'] == 'casino'){
                        self.project_info = self.projects_data[x];
                        self.updateAssetList(stype="3d");
                    }
                    else if(self.cftype.indexOf(self.projects_data[x]['game_type']) >= 0){
                        self.project_info = self.projects_data[x];
                        self.updateAssetList(stype="assets");
                        self.updateShotList(stype="shot");
                    }
                }
            }
        }

        self.updateAssetList = function(stype){
            self.stype = stype;
            $j('#assets').empty();
            $j('#shots').empty();

            assets = []; /*array for sorting*/
            asset_list = ""; /*long string for insertion into dom*/
            self.asset_item_details = [];

            expr = "@SOBJECT(simpleslot/game['name','" + self.game + "'].simpleslot/" + stype + ")";
            self.asset_item_details = server.eval(expr);

            for(y=0;y<self.asset_item_details.length;y++){
                assets.push(self.asset_item_details[y]['name']);
            }
            assets = assets.sort();

            for(y=0;y<assets.length;y++){
                asset_list = asset_list + "<li>" + assets[y] + "</li>";
            }

            $j('ul.selectable#assets').append(asset_list);

            $j('.selectable#assets li').on('click', function( event, ui ) {
                $j('.selectable#assets li').removeClass("ui-selected");
                $j(this).addClass("ui-selected");

                for(z=0;z<self.asset_item_details.length;z++){
                    if($j(this).text() == self.asset_item_details[z]['name']){
                        self.item_details = self.asset_item_details[z];
                    }
                }
                self.getAssetProcess();
            });
        }

        self.updateShotList = function(stype){
            $j('#shots').empty();

            shots = []; /*array for sorting*/
            shot_list = ""; /*long string for insertion into dom*/
            self.shot_item_details = [];

            expr = "@SOBJECT(simpleslot/game['name','" + self.game + "'].simpleslot/shot)";
            self.shot_item_details = server.eval(expr);

            for(y=0;y<self.shot_item_details.length;y++){
                shots.push(self.shot_item_details[y]['name']);
            }
            shots = shots.sort();

            for(y=0;y<shots.length;y++){
                shot_list = shot_list + "<li>" + shots[y] + "</li>";
            }

            $j('ul.selectable#shots').append(shot_list);

            $j('.selectable#shots li').on('click', function( event, ui ) {
                $j('.selectable#shots li').removeClass("ui-selected");
                $j(this).addClass("ui-selected");

                for(z=0;z<self.shot_item_details.length;z++){
                    if($j(this).text() == self.shot_item_details[z]['name']){
                        self.item_details = self.shot_item_details[z];
                    }
                }
                self.getShotProcess();
            });
        }

        self.getAssetProcess = function(){
            expr = "@SOBJECT(simpleslot/" + self.stype + "['code','" + self.item_details['code'] + "'].sthpw/task)";
            self.item_tasks = server.eval(expr);

            asset_process_list = ""; /* long string for insertion into dom */

            $j('.selectable#asset_process').empty();
            $j('.selectable#shot_process').empty();

            ordered = ['rough', 'concept', 'model','texture','rigging','animation','lighting','effects','layout','final']

            for(order=0;order<ordered.length;order++){
                for(task = 0; task < self.item_tasks.length; task++){
                    if(self.item_tasks[task]['process'] == ordered[order]){
                        self.item_task_details = self.item_tasks[task];
                        asset_process_list = asset_process_list + "<li>" + self.item_tasks[task]['process'] + "</li>";
                    }
                }
            }

            $j('ul.selectable#asset_process').append(asset_process_list);
            self.finalPath();
        }

        self.getShotProcess = function(){
            expr = "@SOBJECT(simpleslot/shot['code','" + self.item_details['code'] + "'].sthpw/task)";
            self.item_tasks = server.eval(expr);

            shot_process_list = ""; /* long string for insertion into dom */

            $j('.selectable#shot_process').empty();

            ordered = ['layout','animation','lighting','effects','final']

            for(order=0;order<ordered.length;order++){
                for(task = 0; task < self.item_tasks.length; task++){
                    if(self.item_tasks[task]['process'] == ordered[order]){
                        self.item_task_details = self.item_tasks[task];
                        shot_process_list = shot_process_list + "<li>" + self.item_tasks[task]['process'] + "</li>";
                    }
                }
            }

            $j('.selectable#shot_process').append(shot_process_list);
            self.finalPath();
        }

        self.assetTypeCode = function(code){
            if(code == "ASSET_TYPE00002"){
                asset_type = "character";
            }
            else if(code == "ASSET_TYPE00003"){
                asset_type = "vehicle";
            }
            else if(code == "ASSET_TYPE00004"){
                asset_type = "set";
            }
            else if(code == "ASSET_TYPE00005"){
                asset_type = "prop";
            }
            else if(code == "ASSET_TYPE00006"){
                asset_type = "other";
            }
            else if(code == "3D_TYPE00002"){
                asset_type = "character";
            }
            else if(code == "3D_TYPE00003"){
                asset_type = "symbol";
            }
            else if(code == "3D_TYPE00004"){
                asset_type = "user_interface";
            }
            else if(code == "3D_TYPE00005"){
                asset_type = "bonus01";
            }
            else if(code == "3D_TYPE00006"){
                asset_type = "bonus02";
            }
            else if(code == "3D_TYPE00007"){
                asset_type = "free_game";
            }
            else if(code == "3D_TYPE00008"){
                asset_type = "jackpot";
            }
            else if(code == "3D_TYPE00009"){
                asset_type = "introduction";
            }
            else {
                asset_type = "";
            }

            return asset_type;
        }

        self.finalPath = function(){
            $j('#final_path').empty();
            base_path = "//art-render/art_3d_project/";
            name = server.login;
            project_type = self.project_info['game_type'];

            item_type = self.assetTypeCode(self.item_details['asset_type_code']);

            if(self.cftype.indexOf(self.project_info['game_type']) >= 0){
                final_path = base_path + self.game + "/assets/" + item_type + "/" + self.item_details['name'] + "/" + self.item_task_details['process'] + "/scenes/";
                /*base_filename = jc.abbrName(project) + "_" + jc.abbrItemType(self.item_type) + "_" + self.item_name + "_" + jc.abbrName(self.item_process);*/
                $j('#final_path').text(final_path);
                /*self.saveFile();*/
            }
        }

        self.saveFile = function(){
            test_script = 'app.documents.add();';
            CSLibrary.evalScript(test_script);
        }
    }
