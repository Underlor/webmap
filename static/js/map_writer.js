objs = [];
var last_added_id = -1;
var type_name = ['ПК', 'Свитч', 'Комутатор', 'Роутер']

class Item {
    constructor(name, ip, parent, type) {
        this.name = name;
        this.ip = ip;
        this.parent = parent;
        this.type = type;

        var size = {};
        if (this.type == 0) {
            this.img = "imgs/PC.png";
            size = {x: 100, y: 80};
        }
        else if (this.type == 1) {
            this.img = "imgs/ne.png";
            size = {x: 120, y: 50};
        }
        else if (this.type == 2) {
            this.img = "imgs/sw.png";
            size = {x: 100, y: 50};
        }
        else if (this.type == 3) {
            this.img = "imgs/router.png";
            size = {x: 100, y: 110};
        }
        var name_text = new fabric.Text(name, {
            fontSize: 20,
            originX: 'center',
            left: size.x / 2,
            top: size.y - 16
        });
        var ip_text = new fabric.Text(ip, {
            fontSize: 20,
            originX: 'center',
            left: size.x / 2,
            top: size.y + 4
        });
        fabric.Image.fromURL(this.img, (oImg) => {

            oImg.scaleToHeight(size.y);
            oImg.scaleToWidth(size.x);

            oImg.hasControls = false;
            this.group = new fabric.Group([oImg, name_text, ip_text]);
            this.group.left = canvas.width / 2;
            this.group.top = canvas.height / 2;
            this.group.line1 = [];
            this.group.line2 = [];
            if (parent != 0) {

                var parent_item = getItemByIp(parent);
                var line = makeLine([parent_item.group.left + parent_item.group.width / 2, parent_item.group.top + parent_item.group.height / 2, this.group.left + this.group.width / 2, this.group.top + this.group.height / 2]);
                canvas.add(line);
                parent_item.group.line1.push(null);
                parent_item.group.line2.push(line);
                this.group.line1.push(line);
                this.group.line2.push(null);
                line.sendBackwards();
            }
            canvas.add(this.group);

        });
    }
}

function getItemByIp(ip) {
    var find = null;
    objs.forEach(function (item) {
        if (item.ip == ip) {
            find = item;
        }
    });
    return find;
}

fabric.Group.prototype.hasControls = false;

function findIP(ip, parent) {
    var find = false;
    objs.forEach(function (item) {
        if (item.ip == ip) {
            find = true;
        }

    })
    return find;
}

function AddConfirm() {

    if ($('#DeviceName').val() == "") {
        $('#EmptyName').show();
        return;
    }
    $('#EmptyName').hide();
    if ($('#DeviceIP').val() == "") {
        $('#EmptyIP').show();
        return;
    }
    $('#EmptyIP').hide();
    if (!/((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)/.test($('#DeviceIP').val())) {
        $('#BadIP').show();
        return;
    }
    $('#BadIP').hide();
    if (findIP($('#DeviceIP').val(), $('#MainConnect').val()) && $('#MainConnect').val() != 0) {
        $('#ExistIP').show();
        return;
    }
    $('#ExistIP').hide();


    temp = new Item($('#DeviceName').val(), $('#DeviceIP').val(), $('#MainConnect').val(), $('#DeviceType').val());
    var ip_list = $('#DeviceIP').val().split('.');
    ip_list[ip_list.length - 1] = (parseInt(ip_list[ip_list.length - 1]) + 1).toString();
    $('#DeviceIP').val(ip_list.join('.'));
    if (temp.type > 0) {
        last_added_id = objs.push(temp);
        $('#MainConnect').find("option").removeAttr("selected");
        $('#MainConnect').append("<option value=\"" + temp.ip + "\" selected='1'>" + temp.name + " (" + temp.ip + ")" + " [" + type_name[temp.type] + "]" + "</option>");
    }

    $('#exampleModal').modal('hide');
}

var canvas = new fabric.Canvas('map_canvas', {selection: false});
canvas.setWidth(window.innerWidth);
canvas.setHeight(window.innerHeight);


function makeLine(coords) {
    return new fabric.Line(coords, {
        fill: 'red',
        stroke: 'gray',
        strokeWidth: 5,
        selectable: false
    });
}

canvas.on('object:moving', function (e) {
    var p = e.target;
    p.line1.forEach((item) => {
        item && item.set({'x2': p.left + p.width / 2, 'y2': p.top + p.height / 2});
    });
    p.line2.forEach((item) => {
        item && item.set({'x1': p.left + p.width / 2, 'y1': p.top + p.height / 2});
    });
    canvas.renderAll();
});