var fs = require('fs');
var path = require('path');
var redis = require("../frappe/node_modules/redis");
var { get_conf, get_redis_subscriber } = require('../frappe/node_utils');

var conf = get_conf();

var subscriber = redis.createClient(conf.redis_socketio || conf.redis_async_broker_port);
// alternatively one can try:
//var subscriber = get_redis_subscriber();

 subscriber.on("custom_connector", function (channel, message) {
   // message = JSON.parse(message);

    console.log("####### Message:");

});


