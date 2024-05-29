odoo.define("wb_pos.WBSampleButton", function(require){
    "use strict";


var pos_screens = require('point_of_sale.screens');

var DashboardButton = pos_screens.ActionButtonWidget.extend(
{
templete: 'DashboardButton',
button_click: function(){
alert("Dashboard button cliked");
},
});

pos_screens.define_action_button(
{
'name': 'Dashboard',
'widget': DashboardButton,
'condition': function(){
return this.pos;
},
});

});
