const menu = [{
    "name": "首页",
    "icon": "&#xe68e;",
    "url": "index.html",
    "hidden": false,
    "list": []
}, {
    "name": "学生管理",
    "icon": "&#xe612;",
    "url": "",
    "hidden": false,
    "list": [{
        "name": "学生列表",
        "url": "user_index.html"

    }, {
        "name": "添加学生",
        "url": "user_add.html"
    }]
}, {
    "name": "系统设置",
    "icon": "&#xe620;",
    "url": "",
    "hidden": false,
    "list": [{
        "name": "网站设置",
        "url": "web_index.html"
    }, {
        "name": "友情连接",
        "url": "flink_index.html"
    }, {
        "name": "导航管理",
        "url": "nav_index.html"
    }, {
        "name": "修改密码",
        "url": "web_pwd.html"
    }, {
        "name": "清除缓存",
        "url": "web_cache.html"
    }, {
        "name": "登录页",
        "url": "login.html"
    }]
}, {
    "name": "数据库",
    "icon": "&#xe857;",
    "url": "",
    "hidden": false,
    "list": [{
        "name": "备份数据库",
        "url": "db_backup.html"
    }, {
        "name": "还原数据库",
        "url": "db_reduction.html"
    }]
}, {
    "name": "退出登录",
    "icon": "&#xe65c;",
    "url": "out.html",
    "list": []
}];

const config = {
    name: "就业信息",
    menu: menu,
    version: 'v1.6',
    official: 'http://www.qadmin.net'
};

try {
    module.exports.name = "就业信息";
    module.exports.menu = menu;
} catch (e) {

}
